import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import FaceEmbade
from .serializers import FaceEmbadeSerializer
from .pagination import get_paginated_queryset
# Create your views here.


class FaceEmbedListView(APIView):
    pagination_class = [PageNumberPagination]
    def dispatch(self,request,*args,**kwargs):
        self.model = FaceEmbade
        self.queryset = self.model.objects.all()
        self.serializer_class = FaceEmbadeSerializer
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        data = get_paginated_queryset(self.queryset,request,self.serializer_class)
        return data
