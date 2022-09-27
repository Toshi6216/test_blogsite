from .models import Category, Post

def common(request):
    category_data = Category.objects.all()
    posts_data = Post.objects.all()
#    titles = Post.objects.get('title')
    context = {
        'category_data' : category_data,
        'posts_data' : posts_data,
#        'titles' : titles
    }
    return context