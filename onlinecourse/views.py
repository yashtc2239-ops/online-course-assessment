from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Enrollment, Submission


def course_list(request):
    return render(request, "onlinecourse/course_list.html", {"course_list": Course.objects.all()})


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


@login_required
def submit(request, course_id):
    """Create a submission from the selected answer choices for one course."""
    course = get_object_or_404(Course, pk=course_id)
    enrollment, _ = Enrollment.objects.get_or_create(user=request.user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    selected_choices = Choice.objects.filter(id__in=request.POST.getlist("choice"))
    submission.choices.set(selected_choices)
    return redirect("onlinecourse:show_exam_result", course_id=course.id, submission_id=submission.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    """Evaluate a submission and present its score and answer-by-answer feedback."""
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, enrollment__user=request.user, enrollment__course=course)
    total_score = sum(question.grade for question in course.question_set.all())
    earned_score = submission.get_grade()
    score = int(earned_score / total_score * 100) if total_score else 0
    return render(request, "onlinecourse/exam_result_bootstrap.html", {
        "course": course,
        "submission": submission,
        "score": score,
        "passed": score >= 80,
    })
