from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Canal(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	slug   = models.SlugField(unique=True)

	def __unicode__(self):
		return '%s' % self.nombre

	def clean(self):
		if not self.slug:
			self.slug = slugify(self.nombre)

	@property
	def total_mensajes(self):
		return self.mensajes.all().count()
	

class Mensaje(models.Model):
	canal     = models.ForeignKey(Canal, related_name='mensajes')
	usuario   = models.ForeignKey(User, related_name='mensajes')
	fecha     = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()

	class Meta:
		ordering = ['-fecha', ]

	def __unicode__(self):
		return '%s' % self.contenido