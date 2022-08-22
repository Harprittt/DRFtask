from django.contrib import admin
from .models import Course, CourseChapter, Assignment,User
from django.contrib import admin
# from .forms import CustomUserProfileForm
from django.contrib.auth.admin import UserAdmin





# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserProfileForm
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'is_staff', 'is_superuser')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User type',
            {
                'fields':('type',)
            }
        )
    )


admin.site.register(User, CustomUserAdmin)



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'order', 'created_utc', 'modified_utc']


@admin.register(CourseChapter)
class CourseChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'name', 'order', 'created_utc', 'modified_utc']    



@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'course', 'course_chapter']  