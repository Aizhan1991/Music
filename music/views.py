from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import  Music
from music.serializers import MusicSerializer
#пишем на функциях


@api_view(['GET'])
def get_hello(request): #базовая логика
    # print(dir(request))
    # print(request.user)
    return Response('Hello world')



@api_view(['GET'])
def get_musics(requests,id):
    music = Music.objects.get(id=id)
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)
    # print(music)
    # return Response(music)


@api_view(['GET'])
def get_song(request, id):
        try:
            song= Music.objects.get(id=id)
        except Music.DoesNotExist:
            serializer = MusicSerializer(song, many=False)
        return Response

@api_view(['POST'])
def post_music(request):
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


#DELETE, PUT, PATCH
#    @api_view(['PUT', 'PATCH'])