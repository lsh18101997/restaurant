from django.shortcuts import render
from china.models import Category, Food
from .models import Cart

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

from django.http import JsonResponse
def modify_cart(request):
    food_id= request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, _ = Cart.objects.get_or_create(food=food)    
    cart.amount+=int(request.POST['amountChange'])
    if cart.amount>0:
        cart.save()
    # 변경된 최종 결과를 반환(JSON)
    context = {
        'newQuantity':cart.amount, 
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)
