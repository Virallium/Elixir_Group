from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name="home"), 
    path('apropos/', views.about, name='about'),
    path('carriere/', views.carriere, name='carriere'),
    path('contact/', views.contact, name='contact'),
    path('ecosysème/', views.ecosysteme, name='ecosysteme'),
    path('interventions/', views.intervention,name='interventions'),
    path('solutions/',views.solutions, name='solutions'),
    path('offres/', views.offres,name='offres'),
    path('projets/',views.projets_realisations, name='projets')
    ,path('datalive/evenements/', views.evenements, name='evenements')
    ,path('datalive/interviews/', views.interviews, name='interviews'),
    path('datalive/analyses/', views.analyses, name='analyses'),
    path('datalive/articles/', views.articles, name='articles'),
    path('datalive/opportunites/', views.opportunites, name='opportunites'),
    path('datalive/publications/', views.publications, name='publications'),
    path('datalive/evenements/<int:evenement_id>/', views.evenements_detail, name='evenements_detail'),
]