from django.shortcuts import render
from django import forms

from datetime import datetime
from course.models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

def submit_course(request):
    if request.method == 'POST': 
        form = CourseForm(request.POST, request.FILES) 

        if form.is_valid():
            form.save()
            return render(request, 'course/thank_you.html')
    else:
        form = CourseForm()

    return render(request, 'course/add_course.html', {'form': form})