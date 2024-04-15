from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Category
from django.core.files.storage import FileSystemStorage
# Create your views here.

# def index(request):
#     return render(request, 'china/index.html')

# def upload(request):
#     fs = FileSystemStorage
#     uploaded_file = request.FILES['file']
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = url(name)

def index(request):
    # Get방식으로 들어오면 입력 폼을 보내주고
    if request.method=='GET':
        return render(request=request, template_name='china/index.html')
    # Post 방식으로 들어오면 저장하기
    elif request.method=='POST':
        # Category 모델에서 가져오기
        category=Category.objects.get(name=request.POST['category'])
        # Food 모델
        food_name=request.POST.get('name')
        food_price=request.POST.get('price')
        food_description=request.POST.get('description')
        # 파일 업로드
        fs = FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(name=food_name, price=food_price, category=category, description=food_description, url=url).save()
        
        return redirect('home')


def detail(request, pk):
    food = Food.objects.get(id=pk)
    context = {
        'food':food
    }
    return render(request=request, context=context, template_name='china/detail.html')


def delete(request, pk):
    food = Food.objects.get(id=pk)
    food.delete()
    return redirect('home')

