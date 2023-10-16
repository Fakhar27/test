from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dash/',views.dash,name="dash"),
    path('medicine/',views.addmedicine,name="medicine"),
    # path('addmedicine/',views.addmedicine,name="addmedicine"),
    path('record/',views.record,name="record"),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('issue/',views.issue,name="issue"),
    path('issuedmedicine/',views.issuedmedicine,name='issuedmedicine'),
    path('delete_issuedmedicine/<int:medicine_id>/', views.delete_issuedmedicine, name='delete_issuedmedicine'),
    path('logout/', views.logout_view, name='logout'),
    path('recordsmall/<int:medicine_id>/', views.recordsmall, name='recordsmall'),
    path('issuedmedsmall/<int:medicine_id>/', views.issuedmedsmall, name='issuedmedsmall'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
# path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
#     path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password_reset_complete', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)