from django.shortcuts import render, get_object_or_404

from books.models import Book


# Create your views here.

def index(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list
    }
    return render(request, "books/index.html", context)

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/details.html", {'book': book})