from django.shortcuts import render
from django.http  import HttpResponse
# from blog import forms
from .forms import StudentForm, CreateForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form)
            print("Name :" + form.cleaned_data['name'])
            print("Email :" + form.cleaned_data['email'])
            print("Roll :" + form.cleaned_data['role'])
            
    form = StudentForm()
    return render(request, 'blog/index.html', {'form': form})
def new(request):
    # form=CreateForm()
    # form_data ={"form":form}
    if request.method == "POST":
        form = CreateForm(request.POST)
        # print('Stop')
        if form.is_valid():
            # print('form valid')
            print("Name :" + form.cleaned_data['name'])
            print("Email :" + form.cleaned_data['email'])
            print("Roll :" + str(form.cleaned_data['roll_no']))
            return render(request, 'blog/index.html', {'form': form})
              
    else:
        form = CreateForm()
        # form_data = {"form": form}
    return render(request,"blog/index.html",{'form': form})