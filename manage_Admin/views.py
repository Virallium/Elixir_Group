from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from .models import Evenements, Intervenants, Interview, Partenaires
from pages.models import Publication, Opportunites
from .forms import (
    Add_Actualites, Add_Evenements, Add_Intervenants, Add_Interview,
    Add_Opportunites, Add_Partenaires, Add_Publication,
)
from django.contrib import messages
from pages.models import Actualites

FORM_CONFIG = {
    'evenement': (Evenements, Add_Evenements, 'Événement'),
    'intervenant': (Intervenants, Add_Intervenants, 'Intervenant'),
    'actualite': (Actualites, Add_Actualites, 'Actualité'),
    'publication': (Publication, Add_Publication, 'Publication'),
    'opportunite': (Opportunites, Add_Opportunites, 'Opportunité'),
    'partenaire': (Partenaires, Add_Partenaires, 'Partenaire'),
    'interview': (Interview, Add_Interview, 'Interview'),
}


staff_required = user_passes_test(
    lambda user: user.is_authenticated and user.is_staff,
    login_url='personnels',
)

@staff_required
def Admin_view(request):
    intervenants = Intervenants.objects.all().order_by('nom', 'prenom')
    evenements = Evenements.objects.select_related('idInt').order_by('-date')
    partenaires = Partenaires.objects.all().order_by('idPart')
    interviews = Interview.objects.select_related('evenement').order_by('-evenement__date')
    opportunites = Opportunites.objects.all().order_by('-date')
    Publications = Publication.objects.all().order_by('-date')
    actualites = Actualites.objects.all().order_by('-date_publiee')
    context = {
        'intervenants': intervenants,
        'evenements': evenements,
        'partenaires': partenaires,
        'interviews': interviews,
        'opportunites': opportunites,
        'publications': Publications,
        'actualites': actualites,
        'stats': {
            'intervenants': intervenants.count(),
            'evenements': evenements.count(),
            'partenaires': partenaires.count(),
            'interviews': interviews.count(),
            'opportunites': opportunites.count(),
            'publications': Publications.count()
            , 'actualites': actualites.count()
        },
    }
    return render(request, 'admin/pages/dashboard.html', context)


def _crud_form(request, resource, object_id=None):
    model, form_class, label = FORM_CONFIG[resource]
    instance = get_object_or_404(model, pk=object_id) if object_id else None
    form = form_class(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'{label} enregistré avec succès.')
        return redirect('dashboard')
    return render(request, 'admin/pages/form.html', {
        'form': form,
        'resource': resource,
        'label': label,
        'object': instance,
    })


@staff_required
def create_item(request, resource):
    if resource not in FORM_CONFIG:
        return redirect('dashboard')
    return _crud_form(request, resource)


@staff_required
def update_item(request, resource, object_id):
    if resource not in FORM_CONFIG:
        return redirect('dashboard')
    return _crud_form(request, resource, object_id)


@staff_required
def delete_item(request, resource, object_id):
    if resource not in FORM_CONFIG:
        return redirect('dashboard')
    model, _, label = FORM_CONFIG[resource]
    instance = get_object_or_404(model, pk=object_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, f'{label} supprimé avec succès.')
        return redirect('dashboard')
    return render(request, 'admin/pages/delete.html', {
        'object': instance,
        'resource': resource,
        'label': label,
    })

