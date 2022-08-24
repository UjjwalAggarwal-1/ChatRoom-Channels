from email.mime import application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing as crt


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            crt.websocket_urlpatterns
        )
    ),
})