from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home_page'),
    path('about/', views.about, name = 'about_page'),
    path('form/', views.submit_form, name = 'form_page'),
    path('Contact/', views.contact_form, name = 'contact_page'),
    path('model/', views.Model_form, name = 'model_page'),
]
