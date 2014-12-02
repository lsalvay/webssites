from django.db import models
from clientes.models import Cliente

class Portfolio(models.Model):
	titulo = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	image = models.ImageField(upload_to='portfolios')
	descripcion = models.TextField(blank=True)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.titulo
