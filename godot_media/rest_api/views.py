from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from partner.models import Partners
from rest_api.serializers import PartnerSerializer


@api_view(['GET', 'POST'])
def partner_list(request):

    if request.method == 'GET':
        partners = Partners.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
