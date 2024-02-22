from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RagisterSerializer


@api_view(["POST"])
def home(request):
    data = request.data
    serializer = RagisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({"status": 201, "massage": "you are wrong"})
    return Response({"status": 200, "payload": serializer.data, "massage": "you send"})
