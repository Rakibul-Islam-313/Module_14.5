from django.shortcuts import render
from . forms import contact_Form
from pra_app.forms import My_form
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, 'about.html',{'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')

def submit_form(request):
    return render(request, 'form.html')

def contact_form(request):
    if request.method == 'POST':
        form = contact_Form(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contact_Form()

    return render(request, 'Contact.html', {'form' : form})

def Model_form(request):
    if request.method == 'post':
        result = My_form(request.POST)
        if result.is_valid():
            result.save(commit = True)
    else:
        result = My_form()
        
    return render(request,'model.html', {'form' : result})