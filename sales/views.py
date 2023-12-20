from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sale, Person
from .forms import SaleForm, SaleModelForm

# Create your views here.
def 교육목록(request):
    # return HttpResponse("yes sir")
    
    사람 = Sale.objects.all()
    context = {
        "사람키" : 사람
    }
    return render(request, "folder/교육목록.html", context)

def 세일상세(request, pk):

    사람 = Sale.objects.get(id=pk)
    
    context = {
        "사람키" : 사람
    }

    return render(request, "folder/세일상세.html", context)

def 세일_입력(request):
    폼 = SaleModelForm()
    if request.method == "POST":

        폼 = SaleModelForm(request.POST)
        if 폼.is_valid():
            폼.save()

            """ 
            print(폼.cleaned_data)
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']    
            person = 폼.cleaned_data['person']

            Sale.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                person = person            
            )

            print("신청이 입력되었습니다") """

            return redirect('/홈페이지')

    context = {
        "폼키" : 폼
    }

    return render(request, "folder/세일_입력.html", context)



def 세일_업데이트(request, pk):
    사람 = Sale.objects.get(id=pk)

    폼 = SaleModelForm(instance=사람)
    if request.method == "POST":

        폼 = SaleModelForm(request.POST, instance=사람)
        if 폼.is_valid():

            폼.save()

            return redirect('/홈페이지')

    context = {
        "폼키" : 폼,
        "사람키" : 사람
    }

    return render(request, "folder/세일_업데이트.html", context)



def 세일_지우기(request, pk):
    사람 = Sale.objects.get(id=pk)
    사람.delete()
    return redirect('/홈페이지')


""" def 세일_업데이트(request, pk):
    사람 = Sale.objects.get(id=pk)

    폼 = SaleForm()
    if request.method == "POST":

        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']    
            person = Person.objects.first()

            사람.first_name = first_name
            사람.last_name = last_name
            사람.age = age
            사람.save()

            return redirect('/홈페이지')

    context = {
        "폼키" : 폼,
        "사람키" : 사람
    }

    return render(request, "folder/세일_업데이트.html", context) """


""" def 세일_입력(request):
    폼 = SaleForm()
    if request.method == "POST":
        print("포스트 메소드로 왔네요")
        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            print("유효하네요")
            print(폼.cleaned_data)
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']    
            person = Person.objects.first()

            Sale.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                person = person            
            )

            print("신청이 입력되었습니다")

            return redirect('/홈페이지')

    context = {
        "폼키" : 폼
    }

    return render(request, "folder/세일_입력.html", context) """