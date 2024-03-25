from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer,LoginSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User




@api_view(['POST'])
def login(request):
    data=request.data
    serializer= LoginSerializer(data =data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message':"successfuly"})
    return Response(serializer.errors)


@api_view(['GET','POST'])
def index(request):
    course={'course_name':'python',
            'learn':['flask','django','tor','FASTAPI'],'cours':'ddd'}
    
    if request.method == 'GET':
        return Response(course)    
    elif request.method == 'POST':
        data = request.data

    return Response(course)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer  = PeopleSerializer(objs,many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
    
        data=request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    elif request.method == 'PATCH':
        data=request.data
        obj = Person.objects.get(id = data ['id'])
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id= data['id'])
        obj.delete()
        return Response({'message':'person deleted'})
    

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class=PeopleSerializer
    queryset=Person.objects.all()
    

