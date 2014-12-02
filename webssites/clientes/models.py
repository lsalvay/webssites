from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255, blank=True)
	telefono = models.CharField(max_length=255, blank=True)
	email = models.EmailField(blank=True)
	web = models.CharField(max_length=150, blank=True)
	precio_hosting = models.FloatField(blank=True)
	precio_web = models.FloatField(blank=True)
	fecha_pago_Web = models.DateField(blank=True)
	fecha_pago_dominio = models.DateField(blank=True)
	fecha_pago_hosting = models.DateField(blank=True)
	observaciones = models.TextField(blank=True)
	# favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite_of')

	def __unicode__(self):
		return self.nombre