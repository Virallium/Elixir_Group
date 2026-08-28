from django.contrib import admin
from .models import Evenements, Evenements_Partenaires, Intervenants, Interview, Partenaires

admin.site.register(Intervenants)
admin.site.register(Evenements)
admin.site.register(Interview)
admin.site.register(Partenaires)
admin.site.register(Evenements_Partenaires)
