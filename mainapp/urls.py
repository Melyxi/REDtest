from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('developer/', mainapp.dev, name="dev"),
    path('administrator/', mainapp.admin, name="admin"),
    path('user/', mainapp.user, name="user"),
    path('administrator/edit/<int:pk>/', mainapp.AdminUpdateView.as_view(), name='editadmin'),
    path('developer/edit/<int:pk>/', mainapp.DevUpdateView.as_view(), name='editdev')
]