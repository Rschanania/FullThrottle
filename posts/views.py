
from posts.models import Posts,PostsForm,Category,Gallery
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail,send_mass_mail,mail_admins,mail_managers
from django.dispatch import Signal





class index(FormView):
    template_name="cindex.html"
    form_class=PostsForm
    success_url="/"

class Post_Detail(DetailView):
    model=Posts

class show(TemplateView):
    template_name="posts/list_posts.html"
    model=Posts
    success_url="/"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['object_list'] = Posts.objects.all()#context_object_name="post"
        return context

class add(CreateView):
    model=Posts
    fields="__all__"
    



class edit(UpdateView):
    model=Posts
    fields="__all__"
    success_url="/posts/"


class delete(DeleteView):
    model=Posts
    success_url=reverse_lazy('show')

def mail(request):
    mail1=send_mail("New Year","Hell good wishes from the Ravi","chananias1@gmail.com",["vjy@gmail.com",],fail_silently=False,html_message="Hello Text here")
    if mail1:
        return HttpResponse(mail1)
    else:
        raise Exception("Error occuree")
def massmail(request):
    mail1=("New Year","Hell good wishes from the Ravi","chananias1@gmail.com",["vjy@gmail.com",])
    mail2=("New Year","Hell good wishes from the Vijay","chananias1@gmail.com",["vjy@gmail.com",])
    mail=send_mass_mail((mail1,mail2),fail_silently=False)
    if mail:
        return HttpResponse(mail)
    else:
        raise Exception("Error Ocuuce in mass mail")
    
def mail_admin(request):
    mail_admins("BUGS","hello admin we found many error in website",fail_silently=False)
    return  HttpResponse("Email send successfully")

def mail_manager(request):
    mail_managers("Manager List","We are lisiting the time for all the manager",fail_silently=False)
    return HttpResponse("Email send to Manager")
