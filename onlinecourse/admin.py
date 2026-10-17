from django.contrib import admin
from .models import Choice, Course, Enrollment, Instructor, Learner, Lesson, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ("name", "pub_date", "total_enrollment")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course")


admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
