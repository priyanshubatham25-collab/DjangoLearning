from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('id')
    paginator = Paginator(post,3) #diaplay  5 post per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'testing.html',{'page_obj':page_obj})