from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DrinksSerializer
from .models import Drinks


@api_view(["GET", "POST"])
def drinks_list(request):
    if request.method == "GET":
        drinks = Drinks.objects.all()
        serializers = DrinksSerializer(drinks, many=True)
        return Response({"drinks": serializers.data})
    if request.method == "POST":
        serializers = DrinksSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def drinks_detail(request, id):
    try:
        drinks = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = DrinksSerializer(drinks)
        return Response(serializers.data)
    elif request.method == "PUT":
        serializers = DrinksSerializer(drinks, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
