from django.shortcuts import render
from person.models import Person
from rest_framework import viewsets
from person.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from person.services.person_service import PersonService    

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        try:
            person_data = request.data
            person_dto = PersonService.create(person_data)
            return Response(person_dto.to_dict(), status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        try:
            params = request.query_params
            persons_dto = PersonService.list(params)
            serializer = self.get_serializer(persons_dto, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            person_id = kwargs.get('pk')
            person_dto = PersonService.get_by_id(person_id)
            return Response(person_dto.to_dict())
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            person_id = kwargs.get('pk')
            person_data = request.data
            person_dto = PersonService.update(person_id, person_data)
            return Response(person_dto.to_dict())
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            person_id = kwargs.get('pk')
            PersonService.delete(person_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True, url_path='ideal-weight')
    def ideal_weight(self, request, *args, **kwargs):
        try:
            person_id = kwargs.get('pk')
            ideal_weight = PersonService.get_ideal_weight(person_id)
            return Response(data={'ideal_weight': ideal_weight}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
