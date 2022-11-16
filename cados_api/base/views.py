from django.db.models import Q  # type: ignore
from rest_framework.response import Response  # type: ignore
from django.http import JsonResponse  # type: ignore
from rest_framework.decorators import api_view, permission_classes  # type: ignore
from rest_framework.views import APIView  # type: ignore
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.shortcuts import redirect  # type: ignore
from rest_framework.permissions import IsAuthenticated # type:ignore


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    if request.method=='GET':
        query = request.GET.get(('query'))
        if query ==None:
            query = ''

        advocate = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocate, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        advocate=Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


class AdvocateDetail(APIView):

    def get_object(self,username):
        try:
            return Advocate.objects.get(Q(username__icontains=username))
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate does not exist') # type: ignore

    def get(self,request,username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)

    def put(self,request,username):
        advocate = self.get_object(username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate)

        return Response(serializer.data)

    def delete(self,request,username):
        advocate = self.get_object(username)
        advocate.delete()

        return Response('user deleted')


# @api_view(['GET', 'PUT','DELETE'])
# def advocate_detail(request, username):
#     advocate = Advocate.objects.get(username=username)

#     if request.method=='GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method=='PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user Deleted')

@api_view(['GET'])

def companyList(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)

    return Response(serializer.data)

