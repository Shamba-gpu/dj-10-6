from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    is_review_exist = False

    reviewed_products = request.session.get('reviewed_products', [])
    print(reviewed_products)

    if (request.method == 'POST') and (pk not in reviewed_products):
        # логика для добавления отзыва
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Review.objects.create(text=text, product=product)
            reviewed_products.append(pk)
            request.session['reviewed_products'] = reviewed_products
            is_review_exist = True
    else:
        form = ReviewForm
        if pk in reviewed_products:
            is_review_exist = True

    reviews = Review.objects.filter(product__id=pk)

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
