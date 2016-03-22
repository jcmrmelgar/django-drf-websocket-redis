# Django + Rest Framework DRF + Websockets + Redis

Project home: https://github.com/ikcam/django-drf-websocket-redis

# Detalles
El proyecto es una aplación de **chat de múltiples canales** usando Django como framework (así que puedes usar la base de datos de tu preferencia), además la aplicación cuenta con API creado con [Django Rest Framework](http://www.django-rest-framework.org/) y el websocket ha sido creado usando [Django Websocket Redis](https://github.com/jrief/django-websocket-redis), el front-end del canal está escrito en [AngularJS](https://angularjs.org/).

Disclamer: No se ha realizado ninguna prueba de stress.

# Características
- Todos los mensajes son almacenados en la base de datos.
- Seguridad del lado del servidor pues.
- Únicamente usuarios registrados pueden escribir mensajes.
- Incluye la vista de lista de canales y la vista de detalle del canal

# Uso
1. Descarga este repositorio
2. Ejecuta los siguiente comandos
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```
3. Ingresa al **admin** del proyecto y crea tu primer canal
4. En la página principal del proyecto verás los canales de chat que has creado.

# Preguntas
Por favor usa el "issue tracker" para preguntas.

# Licencia
Copyright © 2016 Irving Kcam.

MIT licensed.