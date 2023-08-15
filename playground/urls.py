from django.urls import include,path
from . import views

#url conf module
urlpatterns = [
    path('hello/', views.say_hello),
    path("__debug__/", include("debug_toolbar.urls"))
]