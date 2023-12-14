from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404, JsonResponse

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.scan()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            appointment = Article(**serializer.validated_data)
            appointment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            appointment = Article.get(hash_key=pk)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        serializer = ArticleSerializer(appointment, data=request.data)
        if serializer.is_valid():
            for attr, value in serializer.validated_data.items():
                setattr(appointment, attr, value)
            appointment.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            appointment = Article.get(hash_key=pk)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        appointment.delete()
        return JsonResponse({'message': 'Article deleted successfully.'}, status=200)
