from django.shortcuts import render,HttpResponseRedirect

from posts.models import Posts,PostsForm,Category,Gallery

def index(request):
    form=PostsForm()
    categories=Category.objects.all()
    data=Posts.objects.all()
   
    if request.method=="POST":
        form=PostsForm(request.POST,request.FILES)
        files=request.FILES.getlist('thumbnail')
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            for f in files:
                gallery=Gallery(post=post,images=f)
                gallery.save()

            return HttpResponseRedirect('/posts/')
    

    return render(request,'index.html',{'form':form,'title':"welcome to index ",'rows':data,'categories':categories})
