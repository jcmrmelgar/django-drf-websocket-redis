import json
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework_nested import routers

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

from . import serializers
from .models import Canal, Mensaje

class CanalViewSet(viewsets.ReadOnlyModelViewSet):
	model            = Canal
	queryset         = Canal.objects.all()
	serializer_class = serializers.CanalSerializer

class MensajeViewSet(viewsets.ModelViewSet):
	model            = Mensaje
	queryset         = Mensaje.objects.all()
	serializer_class = serializers.MensajeSerializer

	def get_queryset(self):
		queryset = self.queryset
		return queryset.filter(canal__pk=self.kwargs.get('canal_pk'))

	def perform_create(self, serializer):
		canal = get_object_or_404(Canal, pk=self.kwargs.get('canal_pk'))
		
		serializer.save(usuario=self.request.user, canal=canal)

		data = {
			'method': 'POST',
			'resource': self.model._meta.verbose_name.capitalize(),
			'data': serializer.data,
		}

		message = RedisMessage( json.dumps(data) )
		RedisPublisher(facility='canal-' + str( canal.id ), broadcast=True).publish_message(message)

router = routers.DefaultRouter()
router.register(r'canales', CanalViewSet)

canal_router = routers.NestedSimpleRouter(router, r'canales', lookup='canal')
canal_router.register(r'mensajes', MensajeViewSet, base_name='canal-mensajes')