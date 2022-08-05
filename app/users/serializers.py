"""Serializers for the user API View"""

from django.contrib.auth import (
    get_user_model,
    authenticate
)
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user, instance is model
        instance and validated_data is the data passed
        in request by the user.
        """

        password = validated_data.pop('password',None)
        """
        Above we removed password from request
        data that we got validated by serializer and saved
        it in password variable. It is not required to
        change password in every request so we are
        providing None as a default password if user
        haven't provided it [May be he wants to change name]
        """

        user = super().update(instance, validated_data)
        """Calling ModelSerializer class's update method
        to update all the details without password"""

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False,
    )

    def validate(self, attr):
        """Validate and authenticate the user."""

        email = attr.get('email')
        password = attr.get('password')
        """authenticate() will do the model's work
        and it will authenticate the user based on email and pass"""

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attr['user'] = user
        return attr
