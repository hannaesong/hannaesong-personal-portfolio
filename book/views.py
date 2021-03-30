from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    book_count = Book.objects.count
    books = Book.objects.order_by('-start_date')
    return render(request, 'book/all_books.html', {'books':books})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/detail.html', {'book':book})