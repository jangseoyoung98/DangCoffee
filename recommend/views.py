from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Q함수를 통해 상품의 이름이나 설명을 OR이나 AND 조건으로 데이터 검색 가능


def home(request):
    return render(request, 'base.html')


def recommend1(request):
    return render(request, 'recommend/recommend1.html')


def recommend2(request):
    return render(request, 'recommend/recommend2.html')


<<<<<<< HEAD
def search(request):
    if request.method == "POST":
        product = Product()
        if product.is_valid():
            product.cafe = request.POST.getlist('cafe', None)
            product.category = request.POST.getlist('drink', None)
            product.image = request.FILES['image']
            query = product.cafe and product.category
            if product:
                products = Product.objects.all().filter(
                    Q(cafe=product.cafe) &
                    Q(category=product.category)
                )

    else:
        query = request.GET.get('keyword')

        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(cafe__icontains=query)
        )
    return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})
=======
def search(request, priceRangeMin=None, priceRangeMax=None, ordering=None):
    if request.method == "POST":

        cafe = request.POST.getlist('cafe', None)
        category = request.POST.getlist('category', None)
        maxvalue = request.GET.get('priceRangeMax')
        minvalue = request.GET.get('priceRangeMin')
        query = "Tag List"

        q = Q()
        if cafe:
            q &= Q(cafe__icontain=cafe)
        if category:
            q &= Q(category__icontain=category)
        if maxvalue and minvalue:
            q &= Product.objects.filter(price__range=[minvalue, maxvalue])

        q &= Q(price__range=(minvalue, maxvalue))

        products = Product.objects.filter(q)

    else:

        query = request.GET.get('keyword')

        j = Q()
        if query:
            j |= Q(name__icontains=query)
            j |= Q(description__icontains=query)
            j |= Q(cafe__icontains=query)
        products = Product.objects.filter(j)
>>>>>>> 54e81e6ee915ecbe6e3c8e8faa0a873ddecd8551

    return render(request, 'recommend/recommend2.html', {'query': query, 'products': products})

def input_test(request):
    if request.POST:
        list_item = request.POST.getlist('test')
        print(list_item)

