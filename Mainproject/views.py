from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
#from django.shortcuts import get_object_or_404
from.models import *
# Create your views here.

def product_list(request, category_slug=None):
    category=None
    product_list=Product.objects.all()
    category_list=Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category=Category.objects.get(slug=category_slug)
        product_list=product_list.filter(category=category)

    search_query=request.GET.get('q')
    if search_query:
        product_list=product_list.filter(
            Q(name__icontains=search_query)|
            Q(description__icontains=search_query)|
            Q(condition__icontains=search_query)|
            Q(brand__brand_name__icontains=search_query)|
            Q(category__category_name__icontains=search_query)
        )

    paginator = Paginator(product_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    template='Product/product_list.html'
    context={'product_list':product_list, 'category_list':category_list,'category':category}
    return render(request,template,context)


def product_detail(request,product_slug):
	product_detail=Product.objects.get(slug=product_slug)

	template='Product/product_detail.html'
	context={'product_detail':product_detail}

	return render(request,template,context)
