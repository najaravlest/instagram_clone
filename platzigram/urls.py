# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.decorators import login_required


# views
# from platzigram.views import hello_world,hi,say_hi
# or
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

# Para poder visualizar las imgs durante desarrollo se agrega el mas y la linea
# Ademas se deben cambiar la mediaurl y media root en settings
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # main
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('hi/', local_views.hi, name='hi'),
    path('say_hi/<str:name>/<int:age>/', local_views.say_hi, name='say_hi'),
    # Users
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout', login_required(users_views.logout_view), name='logout'),
    path('users/me/profile/', login_required(users_views.update_profile), name='update_profile'),
    # posts
    path('', login_required(posts_views.list_posts), name='feed'),
    path('posts/new/', login_required(posts_views.create_post), name='create_post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
