from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# Configuration des URL
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Ajout de l'internationalisation avec i18n_patterns
urlpatterns += i18n_patterns(
    path('', include('financements.urls')),  # Tes URLs de l'application sont maintenant sous les préfixes de langue
)
