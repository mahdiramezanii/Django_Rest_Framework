from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

@api_view(["POST","GET"])
def Home(request):

    return Response({"message":"Hello world"})


class HomeClass(APIView):

    def get(self,request):
        name=request.GET.get("name")
        last=request.GET.get("last")
        return Response({f"message":f"HI {name} {last}"})

    def post(self,request):
        name = request.POST.get("name")
        last = request.POST.get("last")
        return Response({f"message": f" HI {name} {last}"})

@api_view(["GET","POST"])
def test(request):


    return Response({"message":"Hi im test"})
