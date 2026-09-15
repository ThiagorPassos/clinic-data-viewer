from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),
    path('cadastro/', views.cadastro_usuario_view, name='cadastro_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('formulario/', views.formulario_clinico_view, name='formulario_clinico'),
    path('emergencia/<int:perfil_id>/', views.emergencia_view, name='emergencia'),
    path('excluir-conta/', views.excluir_conta_view, name='excluir_conta'),
]
