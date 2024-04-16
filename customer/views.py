from django.shortcuts import render
from china.models import Category, Food

# Create your views here.
def index(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request=request, context=context, template_name='customer/index.html')

def detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request=request, context=context, template_name='customer/detail.html')
