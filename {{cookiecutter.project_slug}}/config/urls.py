from django.conf import settings
from django.conf.urls import include, url
# from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.http import last_modified
from django.views.i18n import JavaScriptCatalog
# from django.views.generic import TemplateView
# from django.views import defaults as default_views

from misago.users.forms.auth import AdminAuthenticationForm

admin.autodiscover()
admin.site.login_form = AdminAuthenticationForm

urlpatterns = [
    url(r'^', include('misago.urls', namespace='misago')),
    url(r'^', include('social_django.urls', namespace='social')),

    # JavaScript Translations
    url(r'django-i18n.js$', last_modified(lambda req, **kw: timezone.now())(
        cache_page(86400 * 2, key_prefix='misagojsi18n')(
            JavaScriptCatalog.as_view(
                packages=['misago'],
            ),
        ),
    ),
        name='django-i18n', ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

# Use static file server for static and media files (debug only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error Handlers
# Misago needs those handlers to deal with errors raised by it's middlewares
# If you replace those handlers with custom ones, make sure you decorate them
# with shared_403_exception_handler or shared_404_exception_handler
# decorators that are defined in misago.views.errorpages module!
handler403 = 'misago.core.errorpages.permission_denied'
handler404 = 'misago.core.errorpages.page_not_found'
