from django.urls import path
from . import views
urlpatterns =[
    path('Dasboard/', views.Admin_view, name='dashboard'),
    path('ajouter/<slug:resource>/', views.create_item, name='create-item'),
    path('<slug:resource>/<int:object_id>/modifier/', views.update_item, name='update-item'),
    path('<slug:resource>/<int:object_id>/supprimer/', views.delete_item, name='delete-item'),
    path('Ajout-Actualites/', views.create_item, {'resource': 'actualite'}, name="Aj-Actualites"),
    path('Ajout-Intervenants/', views.create_item, {'resource': 'intervenant'}, name='Aj-Intervenants'),
    path('Ajout-Evenements/', views.create_item, {'resource': 'evenement'}, name="Aj-Evenements"),
    path('Ajout-Opportunites/', views.create_item, {'resource': 'opportunite'}, name="Aj-Opportunites"),
    path('Ajout-Publications/', views.create_item, {'resource': 'publication'}, name="Aj-Publications")
    ,path('Ajout-Partenaires/', views.create_item, {'resource': 'partenaire'}, name="Aj-Partenaires")
    ,path('Ajout-Interviews/', views.create_item, {'resource': 'interview'}, name="Aj-Interviews")
]