from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View
from posts.models import Posts,PostsForm

def cbview(request):
    return render(request,"cbview.html")

class CbView(TemplateView):
    template_name="CbView1.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context={
            "object_list":Posts.objects.all(),
            "form":PostsForm,
        }



class Post_Table(ListView):
    model=Posts
    template_name="Table.html"


class View_based(View):
    #we need to define get method there
    def get(self,request):
        self.template_name="Table.html"
        data=Posts.objects.all()
        return render(request,self.template_name,{"object_list":data})
    def post(self,request):
        pass
