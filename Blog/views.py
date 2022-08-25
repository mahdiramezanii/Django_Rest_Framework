from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import requests
from .serializers import ArticleSerializers
from .models import Article

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
        response=requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}")
        result=response.json()

        data={
            "symbol":result["symbol"],
            "price":result["price"]
        }

        return Response(data=data)

class ArticleView(APIView):


    def get(self,request):

        queryset=Article.objects.all()
        data=ArticleSerializers(instance=queryset,many=True)

        return Response(data=data.data)

class ArticleDetail(APIView):

    def get(self,request,pk):

        queryset=Article.objects.get(id=pk)

        serialaizer=ArticleSerializers(instance=queryset)

        return Response(data=serialaizer.data)


class AddArticle(APIView):

    def post(self,request):
        ser=ArticleSerializers(data=request.POST)

        if ser.is_valid():
            instance=ser.save()
            instance.status=True
            instance.save()
            return Response({"Response":"Done"})

        return Response(ser.errors)

class UpdateArticle(APIView):

    def put(self,request,pk):
        instance=Article.objects.get(id=pk)
        serializer=ArticleSerializers(instance=instance,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({"response":"Updated"})

        else:
            return Response(serializer.errors)

class DeletArticle(APIView):

    def delete(self,request,pk):
        instance=Article.objects.get(id=pk)
        instance.delete()
        return Response({"response":"deleted"})




