from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Canal, Mensaje

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', )

class CanalSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Canal
		fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
	usuario = UsuarioSerializer(required=False, read_only=True)

	class Meta:
		model   = Mensaje
		exclude = ('canal', )