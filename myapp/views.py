from django.shortcuts import render
from .models import form_table
from .forms import FormForm

# Create your views here.

def Htmlform(request):
    if request.method == "GET":
        name1 = request.GET.get('name')
        age1 = request.GET.get('age')
        data = form_table.objects.create(name=name1,age=age1)
        data.save()
    return render (request,'htmlform.html')

def Pform(request):
    if request.method == "GET":
        name1 = request.GET.get('name')
        age1 = request.GET.get('age')
        data = form_table.objects.create(name=name1,age=age1)
        data.save()
        fm = FormForm()
    else:
        fm = FormForm()
    return render(request,'pform.html',{'form':fm})

def Condtion(request):
    a = {'value':22,'value1':10,'value2':33,'list1':['xyz','a','b','c',1,2,3],'bool':False}
    return render(request,'conditions.html',a)

def Loop(request):
    a = {'value1':[1,2,3,4,5,6,7,8,9,0], 'value2':{'name':'ABC','age':34,'city':'Thane'}}
    return render(request,'loop.html',a)
