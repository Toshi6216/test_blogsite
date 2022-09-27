from .models import Category, Post

def common(request):
    category_data = Category.objects.all()
#    posts_data = Post.objects.all()
    posts_data = Post.objects.order_by('-id')

    context = {
        'category_data' : category_data,
        'posts_data' : posts_data,
        

    }
    return context