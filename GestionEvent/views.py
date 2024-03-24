from django.shortcuts import render , HttpResponseRedirect,redirect, get_object_or_404
from .models import  Utilisateur,Event
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm,EventForm
from django.utils import timezone
import datetime
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def search_event(request):
    if 'q' in request.GET:
        query = request.GET['q']
        events = Event.objects.filter(title__icontains=query)
    else:
        events = Event.objects.none()  # Retourne une queryset vide si aucun terme de recherche n'est fourni
    return render(request, 'search_results.html', {'events': events, 'query': query})


def paiment(request, event_id):
    # Récupérer l'événement spécifique selon l'ID fourni
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        # Traitement de l'achat de tickets ici
        ticket_quantity = int(request.POST.get('ticket_quantity'))
        if ticket_quantity <= event.ticket_quantity:
            # Réduire le stock disponible
            event.ticket_quantity -= ticket_quantity
            event.save()
            # Rediriger vers une page de confirmation ou une autre vue
            return redirect('confirmation_achat')
        else:
            # Gérer le cas où le stock est insuffisant
            return render(request, 'insufficient_stock.html', {'event': event})

    return render(request, 'paiment.html', {'event': event})


def insufficient_stock(request):
    return render(request,'insufficient_stock.html')

# Create your views here.

def inscription(request):
    submitted = False
    form = CustomUserCreationForm(request.POST)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('connexion/')
    else:
        if request.GET.get('submitted'):
            submitted = True
            form=CustomUserCreationForm()

    return render(request, 'register.html', {'form': form, 'submitted': submitted})
    


def delete_event(request, event_id):
    # Récupérer l'événement à supprimer
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        # Supprimer l'événement
        event.delete()
        return redirect('home')  # Rediriger vers la page d'accueil après la suppression de l'événement

    return render(request, 'delete_event.html', {'event': event})


def home(request):
    recent_events = Event.objects.filter(date__gte=timezone.now() - datetime.timedelta(days=7))
   
    return render(request, 'home.html', {'recent_events': recent_events})

def imersion(request):
   return render(request,'imersion.html')

def contact_success(request):
   return render(reverse(request,'contact_success.html'))


def contacter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Logique d'envoi de l'e-mail
        send_mail(
            'Message de contact',  # Sujet du mail
            message,  # Contenu du mail
            settings.EMAIL_HOST_USER,  # Adresse e-mail de l'expéditeur
            [settings.EMAIL_HOST_USER],  # Liste des destinataires (peut être remplacée par une autre adresse e-mail)
            fail_silently=False,  # Ne pas échouer silencieusement en cas d'erreur d'envoi
        )
        
        # Rediriger ou afficher un message de confirmation
        return render(request, 'contact_success.html')  # Créez un template pour afficher un message de confirmation
    
    # Si la méthode de requête n'est pas POST, afficher simplement le formulaire
      # Créez un template pour afficher le formulaire de contact
    return render(request,'contacter.html')

def creation(request):
    return render(request,'creation.html')

def projet(request):
    return render(request,'projet.html')




def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la page d'accueil après la création de l'événement
    else:
        form = EventForm()
    return render(request, 'event.html', {'form': form})




@login_required(login_url="login")

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return HttpResponseRedirect('home')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'login.html', { 'error_message': error_message})

            
def mail(request):
    return render(request,'mail.html') 



def send_invitation(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Récupérer les données du formulaire d'invitation
        invite_name = request.POST.get('invite_name')
        invite_email = request.POST.get('invite_email')
        
        # Logique d'envoi de l'e-mail d'invitation
        # Exemple avec EmailMessage
        subject = 'Invitation à un événement'
        message = f'Bonjour {invite_name}, vous êtes invité à participer à notre événement.'
        sender = 'tarnaguedac@gmail.com'
        recipient = [invite_email]
        
        email = EmailMessage(subject, message, sender, recipient)
        email.send()
        
        # Réponse JSON pour indiquer que l'invitation a été envoyée avec succès
        return JsonResponse({'message': 'Invitation envoyée avec succès'})
    else:
        # Réponse JSON en cas de méthode non autorisée ou non-AJAX
        return JsonResponse({'error': 'Une erreur est survenue'}, status=400)






