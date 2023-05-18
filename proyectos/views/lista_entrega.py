from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.contrib.auth.models import User
from proyectos.models import Entrega, Proyecto,Inscrito, Perfil
from proyectos.views.funciones import *



# # @login_required
@require_GET
def entregas_por_usuario_proyecto(request, user_id):

    perfil_inscrito = perfil_conectado(user_id) #objeto
    # entregas_por_usuario = Entrega.objects.filter(aprendiz=perfil_inscrito, )[:10]  # limitamos a 10 entregas

    inscrito = Inscrito.objects.filter(perfil = perfil_inscrito) #lista

    proyecto = Proyecto.objects.filter(aprendiz = perfil_inscrito) #lista
    

    # user = get_object_or_404(Inscrito, id=user_id)
    # proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    # entregas = Entrega.objects.filter(aprendiz=inscrito, proyecto=proyecto)[:10]  # limitamos a 10 entregas

    data = {
        # 'entregas': list(entregas_por_usuario.values()),
        
        'proyectos': list(proyecto.values())
    }

    return JsonResponse(data)

# def entregas_por_usuario_proyecto(request, user_id, proyecto_id):

#     user = get_object_or_404(User, id=user_id)
#     perfil = get_object_or_404(Perfil, usuario=user)
#     proyecto = get_object_or_404(Proyecto, id=proyecto_id)
#     inscrito = Inscrito.objects.filter(perfil = perfil) #lista
#     entregas = Entrega.objects.filter(aprendiz=inscrito, proyecto=proyecto)[:10]  # limitamos a 10 entregas

#     data = {
#         'inscritos': list(inscrito.values()),
#         'entregas': list(entregas.values()),


#     }

#     return JsonResponse(data)