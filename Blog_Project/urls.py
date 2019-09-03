"""Blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import  LogoutView,LoginView,PasswordResetForm,PasswordResetConfirmView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordChangeView

from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',include("apps.blog.urls"),name="blogPrincipal"),
    path(r'usuario/',include('apps.users.urls'),name='usuarios'),
    url(r'accounts/login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'logout',LogoutView.as_view(template_name='principal/base.html',next_page='listar'),name='logout'),
    url(r'reset/password_reset', PasswordResetView.as_view(template_name='ResetPassword/password_reset_form.html',html_email_template_name='ResetPassword/password_reset_email.html'), name='password_reset'),
    url(r'reset/password_reset_done', PasswordResetDoneView.as_view(template_name='ResetPassword/password_reset_done.html'), name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='ResetPassword/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'reset/done', PasswordResetCompleteView.as_view(template_name='ResetPassword/password_reset_complete.html'), name='password_reset_complete'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
