from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from .forms import CreateBlogForm

# Create your views her
def home(request):
    posts_list = Blog.objects.all()
    return render(request, 'index.html',{
        'blogs':posts_list,
    }
    )
def detail(request,blog_id):
    post_detail = Blog.objects.get(id=blog_id)
    print(post_detail.title)

    return render(request, 'detail.html',{
                  "object":post_detail,
                  }
    ) 
def landing(request):
    return render(request, 'landing.html'
    )           
def createView(request):
    if request.method == 'POST':
         form = CreateBlogForm(request.POST)
         if form.is_valid():
             form_obj = form.save(commit=False)
             form_obj.author = request.user
             form_obj.save()
             return redirect(form_obj.get_absolute_url())
    else:
        form = CreateBlogForm()

    return render(request,"create.html",{
        "form":form
    })
def update_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def delete_item(request, item_id):
    item = get_object_or_404(Blog, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')  # Redirect to your item list page or another appropriate page
    return render(request, 'delete.html', {'item': item})

