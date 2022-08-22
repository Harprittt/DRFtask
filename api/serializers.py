from django.db.models import fields
from .models import Course, CourseChapter, Assignment, User
from rest_framework import serializers
from .models import User



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email','type')




# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')










class AssignmentSerializer(serializers.ModelSerializer):
    # course = serializers.HyperlinkedIdentityField(
    #     many=True, read_only=True, view_name='course_assignments')

    class Meta:
        model = Assignment
        fields = '__all__'





class CourseChapterSerializer(serializers.ModelSerializer):
    course_chapter_assignments = AssignmentSerializer(many=True, read_only=True)
    

    class Meta:
        model = CourseChapter
        fields = ['id', 'course', 'name', 'course_chapter_assignments']




class CourseSerializer(serializers.ModelSerializer):
    course_chapter = CourseChapterSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'course_chapter']











