from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import DemandeFinancement, Contact
from datetime import datetime
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def formulaire(request):
    if request.method == 'POST':
        # Récupérer les données soumises via le formulaire
        civilite = request.POST.get('civilite')
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        revenu = request.POST.get('revenu')
        montant_financement = request.POST.get('montant_financement')
        projet = request.POST.get('projet')

        # Validation des champs revenu et montant_financement
        errors = False  # Flag pour indiquer si une erreur s'est produite

        if not revenu.isnumeric():
            messages.error(request, _("Le champ revenu doit contenir uniquement des chiffres."))
            errors = True

        if not montant_financement.isnumeric():
            messages.error(request, _("Le champ montant de financement doit contenir uniquement des chiffres."))
            errors = True

        # Si des erreurs existent, ne pas sauvegarder et renvoyer le formulaire avec les données saisies
        if errors:
            return render(request, 'one-page.html', {
                'civilite': civilite,
                'nom': nom,
                'telephone': telephone,
                'pays': pays,
                'ville': ville,
                'email': email,
                'adresse': adresse,
                'revenu': revenu,
                'montant_financement': montant_financement,
                'projet': projet,
            })

        # Créer une nouvelle instance de DemandeFinancement si tout est valide
        demande = DemandeFinancement(
            civilite=civilite,
            nom=nom,
            telephone=telephone,
            pays=pays,
            ville=ville,
            email=email,
            adresse=adresse,
            revenu=revenu,
            montant_financement=montant_financement,
            projet=projet
        )

        # Enregistrer l'objet dans la base de données
        demande.save()

        # Envoyer un email de confirmation
        envoyer_email_confirmation(demande)

        # Rediriger vers une page de confirmation après l'enregistrement
        return redirect('confirmation')

    return render(request, 'one-page.html')

def envoyer_email_confirmation(demande):
    # Charger le template HTML pour l'email avec les données dynamiques
    contenu_email = render_to_string('email.html', {
        'nom': demande.nom,
        'telephone': demande.telephone,
        'email': demande.email,
        'pays': demande.pays,
        'ville': demande.ville,
        'adresse': demande.adresse,
        'revenu': demande.revenu,
        'montant_financement': demande.montant_financement,
        'projet': demande.projet,
        'date': datetime.today().date()  # Date actuelle
    })

    # Créer l'objet EmailMessage
    email = EmailMessage(
        subject='Pro-Fund',  # Sujet de l'email
        body=contenu_email,  # Contenu de l'email
        from_email='contact.profond@gmail.com',  # Adresse de l'expéditeur
        to=[demande.email],  # Destinataire
    )
    email.content_subtype = 'html'  # Indique que le corps de l'email est du HTML

    # Envoyer l'email
    email.send()

def confirmation(request):
    return render(request, 'mention.html')

def contact(request):
    if request.method == 'POST':
        # Récupérer les données envoyées par le formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Enregistrer les données dans la base de données
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        # Rediriger vers une page de remerciement ou confirmation
        return redirect('merci')

    return render(request, 'contact.html')

def mention(request):
    return render(request, 'mentionlegale.html')

def merci(request):
    return render(request, 'merci.html')

def email(request):
    return render(request, 'email.html')
