from django.shortcuts import render, render_to_response
from django.template import RequestContext
from home.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
def index(request):

	return render(request, 'index.html')

def empresa(request):

	return render(request, 'empresa.html')

def disenoweb(request):

	return render(request, 'disenoweb.html')

def marketing(request):

	return render(request, 'marketing.html')

def servicios(request):

	return render(request, 'servicios.html')

def contacto(request):

	info_enviado = False
	nombre = ""
	email = ""
	asunto = ""
	mensaje = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			nombre = formulario.cleaned_data['Nombre']
			email = formulario.cleaned_data['Email']
			asunto = formulario.cleaned_data['Asunto']
			mensaje = formulario.cleaned_data['Mensaje']

			to_admin = 'ventas@webssites.com.ar'
			html_content = "<h1>Informacion recibida</h1> <br><br>Nombre: %s <br><br>Email: %s <br><br>Asunto: %s<br><br>***Mensaje***<br><br>%s"%(nombre, email, asunto, mensaje)
			msg = EmailMultiAlternatives('Consulta Webssites.com.ar',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()



	else:
		formulario = ContactForm()
	ctx = {'form':formulario, 'nombre':nombre, 'email':email, 'asunto':asunto, 'mensaje':mensaje, 'info_enviado':info_enviado}
	return render_to_response('contacto.html',ctx,context_instance=RequestContext(request))


