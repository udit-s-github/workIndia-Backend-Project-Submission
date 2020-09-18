from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, NoteSerializer
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Users, UserNotes


@api_view(['POST'])
def users_create(request):
    if request.method == 'POST':
        users_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=users_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(dict(status="account created"), status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def users_login(request):
    if request.method == 'POST':
        users_data = JSONParser().parse(request)
        username_req, password_req = users_data.get("username"), users_data.get("password")
        users_db = Users.objects.filter(username=username_req)
        if password_req == users_db[0].password:
            return JsonResponse(dict(status="success",userId=users_db[0].id), status=status.HTTP_200_OK)
        return JsonResponse(dict(status="Failure. Unauthorized"), status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def users_notes(request,pk):

    title = request.GET.get('user', None)
    print(title)
    user_note = UserNotes(pk=pk)
    if request.method == 'GET':
        note_data = NoteSerializer(user_note)
        return JsonResponse(note_data.data, status=status.HTTP_200_OK)

