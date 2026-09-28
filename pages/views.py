from django.shortcuts import render, get_object_or_404
from manage_Admin.models import Evenements, Evenements_Partenaires, Interview, Partenaires
from .models import *
from pathlib import Path

from django.conf import settings
from django.http import FileResponse
def notfound(request, exception):
    return render(request, 'pages/404.html', status=404)

def home(request):
    partenaires = Partenaires.objects.all().order_by('idPart')
    evenements = Evenements.objects.select_related('idInt').order_by('-date')[:3]  # Get the latest 3 events
    return render(request, 'pages/index.html', {'partenaires': partenaires, 'evenements': evenements})

def about(request):
    return render(request, 'pages/about.html')

def carriere(request):
    return render(request, 'pages/carriere.html')

def contact(request):
    return render(request, 'pages/contact.html')

def policy_page(request, policy_key):
    policies = {
        'mentions-legales': {
            'eyebrow': 'Informations de l’entreprise',
            'title': 'Mentions légales',
            'intro': 'Les informations relatives à l’éditeur de ce site et à ses conditions de consultation.',
            'sections': [
                {
                    'title': 'Éditeur du site',
                    'paragraphs': [
                        'Le présent site est édité par ELIXIR GROUP, entreprise établie à Kinshasa, en République démocratique du Congo.',
                        'Adresse du siège : N°45, avenue Kasa-Vubu, commune de Ngiri-Ngiri, Kinshasa, RDC.',
                        'RCCM : CD/KNG/RCCM/25-B02810. ID NAT : 01-F4200-N79274E. NIF : A256471Q.',
                        'Téléphone : +243 828 126 851. E-mail : elixirgroup@gmail.com.',
                    ],
                },
                {
                    'title': 'Publication et hébergement',
                    'paragraphs': [
                        'Pour toute question concernant le site ou une demande relative à son contenu, contactez Elixir Group à l’adresse elixirgroup@gmail.com.',
                        'Les coordonnées du prestataire d’hébergement peuvent être obtenues auprès de l’éditeur du site.',
                    ],
                },
                {
                    'title': 'Propriété intellectuelle',
                    'paragraphs': [
                        'Sauf indication contraire, les textes, visuels, marques et éléments de présentation publiés sur ce site sont protégés et demeurent la propriété de leurs titulaires. Toute reproduction ou réutilisation substantielle nécessite leur autorisation préalable.',
                    ],
                },
            ],
        },
        'confidentialite': {
            'eyebrow': 'Vie privée',
            'title': 'Politique de confidentialité',
            'intro': 'Cette politique explique comment Elixir Group traite les informations communiquées lors de l’utilisation du site.',
            'sections': [
                {
                    'title': 'Informations concernées et finalités',
                    'paragraphs': [
                        'Lorsque vous préparez un message depuis le formulaire de contact, les informations saisies (nom, adresse e-mail et message) sont utilisées pour préparer une conversation WhatsApp avec Elixir Group. Le site ne transmet pas lui-même ce formulaire à une base de données.',
                        'Si vous choisissez d’envoyer le message dans WhatsApp, les informations sont alors traitées par WhatsApp, service exploité par Meta, selon ses propres conditions et règles de confidentialité.',
                        'Les échanges reçus par e-mail, téléphone ou messagerie sont utilisés pour répondre à votre demande et assurer le suivi de la relation.',
                    ],
                },
                {
                    'title': 'Services tiers et données techniques',
                    'paragraphs': [
                        'Certaines ressources du site, notamment des polices ou bibliothèques d’interface, peuvent être chargées depuis des services tiers. La connexion à ces services peut entraîner le traitement de données techniques telles que votre adresse IP par leurs opérateurs, conformément à leurs propres politiques.',
                        'Votre navigateur peut également échanger les données techniques nécessaires à l’affichage et à la sécurité du site avec son hébergeur.',
                    ],
                },
                {
                    'title': 'Conservation, accès et demandes',
                    'paragraphs': [
                        'Elixir Group limite l’utilisation des informations aux finalités décrites ci-dessus et les conserve pendant la durée nécessaire au traitement de la demande et au suivi correspondant, sous réserve des obligations applicables.',
                        'Pour demander l’accès, la rectification ou la suppression d’informations vous concernant, ou poser une question sur leur traitement, écrivez à elixirgroup@gmail.com. Une vérification raisonnable de votre identité pourra être nécessaire.',
                    ],
                },
            ],
        },
        'conditions-generales': {
            'eyebrow': 'Utilisation du site',
            'title': 'Conditions générales',
            'intro': 'Les règles ci-dessous s’appliquent à la consultation et à l’utilisation du site d’Elixir Group.',
            'sections': [
                {
                    'title': 'Objet du site',
                    'paragraphs': [
                        'Le site présente Elixir Group, ses pôles, ses domaines d’intervention, ses actualités et ses moyens de contact. Les informations publiées sont fournies à titre informatif et ne constituent pas, à elles seules, une offre contractuelle ou un conseil professionnel.',
                    ],
                },
                {
                    'title': 'Utilisation et disponibilité',
                    'paragraphs': [
                        'Vous vous engagez à utiliser le site conformément aux lois applicables, à ne pas perturber son fonctionnement et à ne pas tenter d’accéder sans autorisation à ses systèmes ou aux données d’autrui.',
                        'Elixir Group s’efforce de maintenir des informations utiles et un accès au site, sans garantir l’absence d’erreurs, l’exhaustivité permanente des contenus ou une disponibilité ininterrompue. Les contenus peuvent être modifiés ou retirés.',
                    ],
                },
                {
                    'title': 'Contenus et liens externes',
                    'paragraphs': [
                        'Les contenus du site restent soumis aux droits de propriété intellectuelle de leurs titulaires. Les liens vers des services tiers sont proposés pour faciliter la navigation ; Elixir Group ne contrôle pas leurs contenus ni leurs pratiques.',
                    ],
                },
                {
                    'title': 'Droit applicable et contact',
                    'paragraphs': [
                        'Les présentes conditions sont interprétées conformément aux règles applicables en République démocratique du Congo. Toute question concernant leur application peut être adressée à elixirgroup@gmail.com.',
                    ],
                },
            ],
        },
        'protection-donnees': {
            'eyebrow': 'Données personnelles',
            'title': 'Politique de protection des données',
            'intro': 'Elixir Group veille à ce que les informations personnelles soient utilisées avec discernement et uniquement pour des besoins identifiés.',
            'sections': [
                {
                    'title': 'Principes de traitement',
                    'paragraphs': [
                        'Les informations personnelles sont traitées pour répondre aux demandes adressées à Elixir Group, communiquer avec les personnes qui prennent contact et assurer le suivi utile de ces échanges. Elles ne doivent pas être réutilisées à des fins incompatibles avec ces objectifs.',
                        'Le formulaire de contact prépare un message WhatsApp à partir du nom, de l’adresse e-mail et du texte saisis. L’envoi dépend ensuite de votre action dans WhatsApp ; le site ne conserve pas lui-même les données du formulaire.',
                    ],
                },
                {
                    'title': 'Accès et partage',
                    'paragraphs': [
                        'L’accès aux informations reçues par Elixir Group est limité aux personnes qui en ont besoin pour traiter la demande. Elles ne sont pas destinées à être vendues. Les prestataires techniques et services externes éventuellement utilisés peuvent traiter certaines données nécessaires à leur fonctionnement selon leurs propres conditions.',
                    ],
                },
                {
                    'title': 'Sécurité et durée de conservation',
                    'paragraphs': [
                        'Elixir Group prend des mesures adaptées pour limiter les accès non autorisés et protéger les informations qui lui sont confiées. Aucune transmission sur Internet ni mesure de sécurité ne peut toutefois être garantie comme absolument infaillible.',
                        'Les informations sont conservées le temps nécessaire à la demande et à son suivi, puis supprimées ou conservées uniquement lorsqu’une obligation applicable le justifie.',
                    ],
                },
                {
                    'title': 'Exercer vos droits',
                    'paragraphs': [
                        'Pour toute question ou demande d’accès, de rectification ou de suppression concernant vos informations, contactez Elixir Group à elixirgroup@gmail.com ou au +243 828 126 851. Les demandes sont examinées au regard des règles applicables.',
                    ],
                },
            ],
        },
    }
    return render(request, 'pages/policy.html', {'policy': policies[policy_key]})

def ecosysteme(request):
    
    return render(request, 'pages/ecosysteme.html')

def intervention(request):
    return render(request, 'pages/intervention.html')

def solutions(request):
    return render(request, 'pages/nos_solutions.html')

def offres(request):
    return render(request, 'pages/offres.html')


def projets_realisations(request):
    return render(request, 'pages/projets_realisation.html')

def evenements(request):
    evenements = Evenements.objects.select_related('idInt').order_by('-date')
    return render(request, 'pages/datalive/evenements.html', {'evenements': evenements})

def interviews(request):
    interviews = Interview.objects.select_related('evenement', 'evenement__idInt').order_by('-evenement__date')
    return render(request, 'pages/datalive/interviews.html', {'interviews': interviews})



def articles(request):
    actualites = Actualites.objects.all().order_by('-date_publiee')
    return render(request, 'pages/datalive/articles.html', {'actualites': actualites})

def opportunites(request):
    opportunites = Opportunites.objects.all().order_by('-date')
    return render(request, 'pages/datalive/opportunites.html', {'opportunites': opportunites})

def publications(request):
    publications = Publication.objects.all().order_by('-date')
    return render(request, 'pages/datalive/publications.html', {'publications': publications})

def evenements_detail(request, evenement_id):
    evenement = get_object_or_404(
        Evenements.objects.select_related('idInt'),
        id=evenement_id,
    )
    partenaire_ids = Evenements_Partenaires.objects.filter(
        evenement=evenement,
    ).values('partenaire_id')
    partenaires = Partenaires.objects.filter(pk__in=partenaire_ids)
    interviews = Interview.objects.filter(evenement=evenement)
    return render(request, 'pages/datalive/evenements_detail.html', {
        'evenement': evenement,
        'partenaires': partenaires,
        'interviews': interviews,
    })

def service_worker(request):
    worker_path = Path(settings.BASE_DIR) / 'static' / 'pwa-build' / 'sw.js'
    if not worker_path.exists():
        worker_path = Path(settings.BASE_DIR) / 'static' / 'js' / 'sw.js'
    response = FileResponse(
        worker_path.open('rb'),
        content_type='application/javascript',
    )
    response['Service-Worker-Allowed'] = '/'
    response['Cache-Control'] = 'no-cache'
    return response