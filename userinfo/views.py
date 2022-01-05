from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userinfo.models import UserInfo
from userinfo.serializers import UserSerializer


class UserInfoList(APIView):

    def get(self, request, format=None):
        if len(request.GET) == 0:
            userinfo = UserInfo.objects.all()
            serializer = UserSerializer(userinfo, many=True)
        else:
            username = request.GET.get('username')
            email = request.GET.get('email')

            if not username and email:
                userinfo = UserInfo.objects.get(email=email)

            elif not email and username:
                userinfo = UserInfo.objects.get(username=username)

            elif username and email:
                userinfo = UserInfo.objects.get(username=username, email=email)
            
            serializer = UserSerializer(userinfo, many=False)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoDetail(APIView):
    """
    Retrieve, update or delete a userinfo instance.
    """

    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserSerializer(userinfo)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserSerializer(userinfo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserSerializer(userinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserSerializer(userinfo)
        
        output = serializer.data
        output['message']='Delete Succeeded'
        userinfo.delete()
        return Response(output, status=status.HTTP_200_OK)


# Create your views here.
# @csrf_exempt
# def userinfo_list(request):
#     if request.method == 'GET':
#         userinfo = UserInfo.objects.all()
#         serializer = UserSerializer(userinfo, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def userinfo_detail(request, pk):
#     """Retrieve, update or delete

#     Args:
#         request ([type]):
#         pk ([type]): id
#     """
#     try:
#         userinfo = UserInfo.objects.get(pk=pk)
#     except UserInfo.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UserSerializer(userinfo)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(userinfo, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         userinfo.delete()
#         return HttpResponse(status=204)
