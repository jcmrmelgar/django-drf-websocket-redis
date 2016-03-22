from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from .models import Canal, Mensaje

from ws4redis.publisher import RedisPublisher

class Canales(ListView):
	model = Canal

class Canal(DetailView):
	model = Canal

	def get(self, request, *args, **kwargs):
		instance = self.get_object()

		RedisPublisher(facility='canal-' + str(instance.id) , broadcast=True)

		return super(Canal, self).get(request, *args, **kwargs)