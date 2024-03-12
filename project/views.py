from django.shortcuts import render

# Create your views here.

posts = [
    {
        'title': ' تقرير الالتزام الأول ',
        'content': ' نتائج حالة التزام الجهة بالضوابط، وتقرير الالتزام المقترح',
        'post_date':'15-2-2024', 
    },
    
    {
        'title': ' تقرير الالتزام الثاني ',
        'content': ' نتائج حالة التزام الجهة بالضوابط، وتقرير الالتزام المقترح',
        'post_date':'15-3-2024', 
    },
    
    {
        'title': ' تقرير الالتزام الثالث ',
        'content': ' نتائج حالة التزام الجهة بالضوابط، وتقرير الالتزام المقترح',
        'post_date':'15-4-2024', 
    },
    
    ]

def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        }
    return render (request, 'project/index.html', context)


def about(request): 
    return render(request, 'project/about.html', {'title': 'من نحن'})