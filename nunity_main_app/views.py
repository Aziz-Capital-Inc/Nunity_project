from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentDats
from .forms import StudentForm2
from django.contrib.auth.decorators import login_required

@login_required
def view_form(request):
    student_form = StudentForm2()
    if request.method == 'POST':
        form_data = StudentForm2(request.POST)
        if form_data.is_valid():
            form_data.save()
    students=StudentDats.objects.all()
    context={
        "students":students,
        "forms":student_form
        }

    return render(request, 'main/index.html', context)

def delete_post(request, post_id):
    post = StudentDats.objects.get(id=post_id)
    post.delete()
    return redirect('home')

@login_required
def edit_post(request, post_id):
    post_object=get_object_or_404(StudentDats, id=post_id)
    edit_form = StudentForm2(instance=post_object)
    if request.method == 'POST':
        form_data = StudentForm2(request.POST, instance=post_object)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    context ={
        'form_edit' : edit_form
    }
    return render(request, 'main/edit.html', context)