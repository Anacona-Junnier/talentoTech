from django.urls import path

from . import views

app_name = "encuestas"
urlpatterns = [
    #/encuestas/
    path("", views.index, name="index"),
    #/encuestas/detalle/5/
    path("detalle/<str:question_id>/", views.detalle, name="detalle"),
    #/encuestas/5/resultado/
    path("<int:question_id>/resultado/", views.resultado, name="resultado"),
    #/encuestas/5/voto/
    path("<int:question_id>/voto/", views.voto, name="voto")
]