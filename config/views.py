from django.shortcuts import render
from china.models import Food, Category


def home(request):
    category = Category.objects.all()
    food = Food.objects.all()
    context = {
        'category':category,
        'food':food
    }
    return render(request=request, context=context, template_name='home.html')



