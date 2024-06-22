from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book, Category


# Create your views here.
def index(request):
    books_on_sale = Book.objects.filter(is_on_sale=True)
    context = {
        'books_on_sale': books_on_sale,
    }
    return render(request, 'index.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    context = {
        'category': category,
        'books': books
    }
    return render(request, 'category_detail.html', context)
