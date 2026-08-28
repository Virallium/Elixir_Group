from django.shortcuts import render, get_object_or_404
from manage_Admin.models import Evenements, Evenements_Partenaires, Interview, Partenaires
from .models import *

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

def analyses(request):
    return render(request, 'pages/datalive/analyses.html')

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




