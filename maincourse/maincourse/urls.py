"""maincourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from mainapp.views import *
from mainapp.templatetags import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', hello, name='hello'),
    # path('hello', views.hello, name='hello2'),
    # path('',views.hello, name='index'),
    # path('', include('user_admin.urls')),
    # path('hello/?name=<str:user_name>', hello, name='hello'),
    # path('hello/', GreetingView.as_view(), name='greeting'),
    # path('', feedback, name='feedback'),
    path('home/', home, name='My dictionary'),
    path('', home, name='My dictionary'),
    path('words_list/', words_reading, name='words_reading'),
    path('add_word/', add_word, name='add_word'),
    # path('', new1, name='feedback'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
