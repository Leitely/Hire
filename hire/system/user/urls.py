from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static

from .registration.views        import RegisterView


app_name = 'user_login'

urlpatterns = [
    path("register/",      RegisterView.as_view(),      name='register')

]
