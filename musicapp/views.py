from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import SongSerializer, UpdateSongSerializer
from django.shortcuts import get_object_or_404


class SongViewSet(viewsets.ModelViewSet):
    serializer_class =SongSerializer

    #to get all the queryset
    def get_queryset(self):
        return song.objects.all()

    #to get a particular id
    def get_object(self):
        id = self.kwargs.get('pk')
        song = get_object_or_404(song, pk=id)
        return song

    def update(self, request, *args, **kwargs):
        song = self.get_object()
        serializer = UpdateSongSerializer(instance=song, data=request.data, partial=True)

        serializer .is_valid(raise_exception=True)

        song_instance = serializer.update(song, serializer.validated_data)
        response_data = self.get_serializer(song_instance).data
        return Response(response_data, status=status. HTTP_200_OK)


    def destroy(self, request, *args, **kwargs):
        song = self.get_object()
        song.delete()
        deleted = f"{song} has been deleted"
        return Response(deleted, status=status.HTTP_204_NO_CONTENT)
             


    

    

    


