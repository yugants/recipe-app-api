"""
URL mappings for the user API.
"""

from django.urls import path

from users import views

'''In test_user_api we are refering this app_name.'''

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
