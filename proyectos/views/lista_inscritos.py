from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.lista_inscritos import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

from proyectos.views.funciones import *

class ListaInscritosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inscrito.objects.all()
    serializer_class = ListaInscritoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_inscritos(self, request, *args, **kwargs):

        perfil_id =  kwargs['id_user']
        p=Inscrito.objects.get(perfil =perfil_id)
        inscrito = Inscrito.objects.filter(ficha__id=p.ficha.id)
        print(p.ficha.id)
        serializer = self.get_serializer(inscrito, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['get'])
    # def get_inscritos(self, request, *args, **kwargs):
    #     id_user= kwargs['id_user']
    #     perfil_inscrito = perfil_conectado(id_user) 
    #     inscrito = Inscrito.objects.filter(perfil = perfil_inscrito)
         
    #     # inscritos = Inscrito.objects.filter(ficha=inscrito.ficha)
    #     serializer = ListaInscritoSerializer(inscrito, many=True)
    #     return Response(serializer.data)