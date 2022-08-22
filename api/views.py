from re import search
from .models import User
from django.shortcuts import render
# from rest_framework import authentication
from .serializers import CourseSerializer, AssignmentSerializer, CourseChapterSerializer
from .models import  Course, CourseChapter, Assignment
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .permissions import WriteByAdminOnlyPermission




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": "Your Account Has Been Created Successfully !!"
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })

   






#-------------ListCreateAPIView---------------------

class CourseListCreate(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    


class CourseChapterListCreate(generics.ListCreateAPIView):
    serializer_class = CourseChapterSerializer
    queryset = CourseChapter.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    
    



class AssignmentListCreate(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    


#-------------ListCreateAPIView ---------------------





#-------------------RetrieveUpdateDestroyAPIView------------

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    



class CourseChapterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CourseChapterSerializer
    queryset = CourseChapter.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    



class AssignmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    

#-------------------RetrieveUpdateDestroyAPIView------------







