from django import forms

class ContactForm(forms.Form):
	Nombre = forms.CharField(widget=forms.TextInput({ "placeholder": "Ingrese su nombre"}))
	Email = forms.EmailField(widget=forms.TextInput({ "placeholder": "Ingrese su correo"}))
	Asunto = forms.CharField(widget=forms.TextInput({ "placeholder": "Ingrese un asunto"}))
	Mensaje = forms.CharField(widget=forms.Textarea({ "placeholder": "Ingrese un comentario"}))