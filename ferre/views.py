from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import manuales, electricas, neumaticas
from .forms import ManForm, EleForm, NeuForm , CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

#---------------------------------------------------------------
# VISTAS DE LAS TEMPLATES PRINCIPALES
#---------------------------------------------------------------

class HomePageView(ListView):
	model = electricas
	template_name = 'home.html'
	context_object_name = 'docs_list'

class ProductosPageView(ListView):
	model = manuales
	template_name = 'productos.html'
	context_object_name = 'docs_list'

class ElectricasPageView(ListView):
	model = electricas
	template_name = 'electricas.html'
	context_object_name = 'docs_list'

class NeumaticasPageView(ListView):
	model = neumaticas
	template_name = 'neumaticas.html'
	context_object_name = 'docs_list'


class AcercaPageView(ListView):
	model = electricas
	template_name = 'acercade.html'
	context_object_name = 'docs_list'


#---------------------------------------------------------------
# VISTAS PARA EL CONTROL DE CUENTAS DE USUARIOS
#---------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = electricas
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})



#---------------------------------------------------------------
# VISTAS PARA LA MANIPULACION DE LOS MODELOS
#---------------------------------------------------------------
# MODELO MANUALES
#---------------------------------------------------------------

@permission_required('ferre.add_manuales')
def agregarMan (request):

	if request.method == "GET":
		form = ManForm()
	else:
		form = ManForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Anadido con exito")
			return redirect('productos')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarMan.html', {"form": form})


@permission_required('ferre.change_manuales')
def modificarMan (request, id):

	Man = get_object_or_404(manuales, id=id)

	data = {
		'form': ManForm(instance=Man)
	}

	if request.method == "GET":
		form = ManForm()
	else:
		form = ManForm(request.POST,request.FILES, instance=Man)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('productos')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('ferre.delete_manuales')
def eliminarMan (request, id):
	Man = get_object_or_404(manuales, id=id)
	Man.delete()

	return redirect(to = "productos")

#---------------------------------------------------------------
# MODELO ELECTRICAS
#---------------------------------------------------------------

@permission_required('ferre.add_electricas')
def agregarEle (request):

	if request.method == "GET":
		form = EleForm()
	else:
		form = EleForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('electricas')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarEle.html', {"form": form})


	# data = {
	# 	'form':EleForm()
	# }

	# if request.method == 'POST':
	# 	formulario = EleForm(data=request.POST)
	# 	if formulario.is_valid():
	# 		formulario.save()
	# 		data['mensaje'] = 'Guardado correctamente'
	# 		return redirect(to='electricas')
	# 	else:
	# 		data['form'] = formulario

	# return render(request, 'agregarEle.html',data)


@permission_required('ferre.change_electricas')
def modificarEle (request, id):

	Ele = get_object_or_404(electricas, id=id)

	data = {
		'form': EleForm(instance=Ele)
	}

	if request.method == "GET":
		form = EleForm()
	else:
		form = EleForm(request.POST,request.FILES, instance=Ele)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('electricas')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('ferre.delete_electricas')
def eliminarEle (request, id):
	Ele = get_object_or_404(electricas, id=id)
	Ele.delete()

	return redirect(to = "electricas")


#---------------------------------------------------------------
# MODELO NEUMATICAS
#---------------------------------------------------------------


@permission_required('ferre.add_neumaticas')
def agregarNeu (request):

	if request.method == "GET":
		form = NeuForm()
	else:
		form = NeuForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('neumaticas')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'agregarNeu.html', {"form": form})


@permission_required('ferre.change_neumaticas')
def modificarNeu (request, id):

	Neu = get_object_or_404(neumaticas, id=id)

	data = {
		'form': NeuForm(instance=Neu)
	}

	if request.method == "GET":
		form = NeuForm()
	else:
		form = NeuForm(request.POST,request.FILES, instance=Neu)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully added!")
			return redirect('neumaticas')
		else:
			messages.error(request, "Por favor rellene todos los campos")
	return render(request, 'modificar.html', data)


@permission_required('ferre.delete_neumaticas')
def eliminarNeu (request, id):
	Neu = get_object_or_404(neumaticas, id=id)
	Neu.delete()

	return redirect(to = "neumaticas")

#--------------------------------------------------------------------
