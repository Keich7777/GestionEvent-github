from django.urls import path,include
from .views import home, inscription, login_view,contacter,imersion,creation,projet,paiment,event,delete_event,insufficient_stock,send_invitation,contact_success,search_event
from GestionEvent import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('connexion/home/', home, name="home"),
     path('search/', search_event, name='search_event'),
    path('',inscription, name ="register"),
    path('connexion/', login_view, name='login'),
    path('connexion/home/contacter/', views.contacter, name='contacter'),
     path('connexion/home/contacter/contact_success/', contact_success, name='contact_success'),
    path('connexion/home/imersion/', imersion, name='imersion'),
    path('connexion/home/creation/', creation, name='creation'),
    path('connexion/home/projet/', projet, name='projet'),
    path('connexion/home/paiment/<int:event_id>/', paiment, name='paiment'),
    path('connexion/home/event/', event, name='event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('connexion/home/send_invitation/', send_invitation, name='send_invitation'),
    path('connexion/home/paiment/insufficient_stock/', insufficient_stock, name='insufficient_stock'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)