#from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# def index(request):
#     lista_ultimas_preguntas = Question.objects.order_by("-pub_date")[:5]
#     plantilla = loader.get_template("encuestas/index.html")
#     contexto = {
#         "lista_ultimas_preguntas": lista_ultimas_preguntas,
#     }
#     return HttpResponse(plantilla.render(contexto, request))

# def index(request):
    #return HttpResponse("Hola, mundo. Tú estas en el indice de encuestas.")

# def index(request):
    # lista_ultimas_preguntas = Question.objects.order_by("-pub_date")[:5]
    #salida = ", ".join([q.question_text for q in lista_ultimas_preguntas])
    #return HttpResponse(salida)

# def detalle(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("EL CUESTIONARIO NO EXISTE!")
#     return render(request, "encuestas/detalle.html", {"question": question})

    #return HttpResponse("Estas mirando los detalles de la pregunta %s." % question_id)

def index(request):
    lista_ultimas_preguntas = Question.objects.order_by("-pub_date")[:5]
    contexto = {"lista_ultimas_preguntas":lista_ultimas_preguntas}
    return render(request, "encuestas/index.html", contexto)

def detalle(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "encuestas/detalle.html", {"question": question})

def resultado(request, question_id):
    respuesta = "Estas viendo los resultados de la pregunta %s"
    return HttpResponse(respuesta % question_id)

def voto(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    try:
        opcion_seleccionada = pregunta.choice_set.get(pk=request.POST["opcion"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,"encuestas/detalle.html",{"question": pregunta,"error_message": "NO SELECCIONASTE UNA OPCIÓN",},)
    else:
        opcion_seleccionada.votes +=1
        opcion_seleccionada.save()
        #siempre usar HttpResponseRedirect despues de trabajar exitosamente con POST para evitar que los datos se publiquen dos veces si un usuario presiona el boton atras
        return HttpResponseRedirect(reverse("encuestas:resultado", args=(pregunta.id,)))
    #return HttpResponse("Estas votando en la pregunta %s" % question_id)