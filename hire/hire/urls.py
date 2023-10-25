from django.contrib          import admin
from django.urls             import path, include

from django.conf             import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/",      admin.site.urls),
    path("",            include("system.home.urls")),
    path("user/",       include("system.user.urls")),
    path("",            include("django.contrib.auth.urls")),

    path("__reload__/", include("django_browser_reload.urls")),
]


# tells Django where to save the documents.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# tells Django where to get the files in production.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
