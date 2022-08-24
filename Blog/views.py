from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import requests

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

    if request.method == "GET":
        name=request.GET.get("name")

        return Response({f"hello{name}"})


    return Response({"message":"Hi im test"})



class GetCriptoPrice(APIView):

    def get(self,request):
        url="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        coin=request.GET.get("coin")
        response=requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}")
        result=response.json()

        data={
            "symbol":result["symbol"],
            "price":result["price"]
        }

        return Response(data=data)