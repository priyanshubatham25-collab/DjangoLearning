from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_create(request):
    form  = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'student_sucess.html')
    return render(request,'student_form.html',{'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})


def student_details(request,pk):
    students = get_object_or_404(Student,pk=pk)
    return render(request, 'student_details.html',{'student':students})

def student_edit(request,pk):   
    students = get_object_or_404(Student,pk=pk)
    if request.method =='POST': 
        form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save() 
            return redirect('student_list')
    else:
        form = StudentForm(instance=students)
    return render(request, 'student_form.html',{'form':form})
    
def student_delete(request,pk):
    students = get_object_or_404(Student, pk=pk)
    if request.method =='POST':
        students.delete()
        return redirect('student_list')
    return render(request,'student_confirm_delete.html',{'student':students})
