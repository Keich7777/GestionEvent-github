
from django import forms 
from .models import Utilisateur as CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Utilisateur,Event


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.EmailField(label="Mail")
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    

    class Meta(UserCreationForm.Meta):
        model=Utilisateur
        fields = UserCreationForm.Meta.fields + ("username","email","password1", "password2")


def save(self, commit=True):
        user = save(commit=False)
        if commit:
            user.save()

            # Envoi d'un e-mail de confirmation
            subject = "Confirmation d'inscription"
            html_message = render_to_string('mail.html', {'user': user})
            plain_message = strip_tags(html_message)
            from_email = 'tarnaguedac@gmail.com'
            to_email = user.email
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

        return user


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'date','lieu', 'ticket_quantity', 'description']