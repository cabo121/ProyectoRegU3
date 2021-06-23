from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from .views import password_reset_request,eliminarMan,agregarMan,modificarMan,eliminarNeu,modificarNeu,agregarNeu,eliminarEle,modificarEle,agregarEle,ElectricasPageView,NeumaticasPageView,AcercaPageView,ProductosPageView,HomePageView,RegistroPageView,registro_usuario,changePassword

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('registration/registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registration/registrar', registro_usuario, name='registrar'),	
	path('change_password/', changePassword, name = 'change_password' ),
	path("password_reset", password_reset_request, name="password_reset"),
	path('productos/',ProductosPageView.as_view(), name = 'productos'),
	path('acercade/', AcercaPageView.as_view(), name = 'acerca'),
	path('electricas/',ElectricasPageView.as_view(), name = 'electricas'),
	path('neumaticas/',NeumaticasPageView.as_view(), name = 'neumaticas'),
	path('modificarEle/<id>/',modificarEle, name = 'modificarEle'),
	path('eliminarEle/<id>/',eliminarEle, name = 'eliminarEle'),
	path('agregarEle/',agregarEle, name = 'agregarEle'),
	path('modificarMan/<id>/',modificarMan, name = 'modificarMan'),
	path('eliminarMan/<id>/',eliminarMan, name = 'eliminarMan'),
	path('agregarMan/',agregarMan, name = 'agregarMan'),
	path('eliminarNeu/<id>/',eliminarNeu, name = 'eliminarNeu'),
	path('modificarNeu/<id>/',modificarNeu, name = 'modificarNeu'),
	path('agregarNeu/',agregarNeu, name = 'agregarNeu'),
]