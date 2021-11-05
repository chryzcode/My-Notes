from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of your notes notes'
        },
        {
            'Endpoint': '/note/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/add-note/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/edit-note/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update an existing note '
        },
        {
            'Endpoint': '/delete-note/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
        {
            'Endpoint': '/delete-user',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes Authenticated User'
        },
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    notes = Note.objects.filter(user=request.user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editNote(request, pk):
    note = Note.objects.get(pk=pk)
    if request.user.id == note.user.id:
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    if request.user.id == note.user.id:
        note = Note.objects.get(pk=pk)
        note.delete()
        return Response("Note deleted")
    else:
        return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request):
    request.user.delete()
    return Response("User deleted")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewNote(request, pk):
    if request.user.id == note.user.id:
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    else:
        return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)
