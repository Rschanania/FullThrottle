from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return render(request, 'pages/contact.html',{'title':"Contact page"})

def about(request):
    return render(request,'pages/about.html',{'title':"About page"})

def member(request,cat_id,team_id):
    print(request.GET)
    return HttpResponse(f"hello team cat is {cat_id} and team id is {team_id}")

# def team(request):
#     return  HttpResponse("All team")
def team(request):
    if request.GET and 'c_id' in request.GET and 't_id' in request.GET:
        print(request.GET.get('c_id'))
        return HttpResponse(f" c_id is {request.GET.get('c_id')} and t_id is {request.GET.get('t_id')}")
    else:
        return HttpResponse("none hai")


def re(request,c_id):
    print(request.GET.get('c_id'))
    return HttpResponse(f"hello c_id is {c_id}")
def Hr(request):
    return HttpResponse(f"Hello Hr id is {request.GET.get('hr_id')}")



# Create your views here.
