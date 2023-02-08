from django.shortcuts import (
    render,
    get_object_or_404
)
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.

# Handles the starting page.
def index(request):
    # Querys the database and orders it by the title.
    books = Book.objects.all().order_by("title")
    # Stores the  amount of items and the  avarage of a  particular value in two 
    # variables.
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "avarage_rating": avg_rating
    })

# Handles the detailed pages for the books.
def book_detail(request, slug):
    #try:
        #book = Book.objects.get(id=id)
    #except:
        #raise Http404
    # A simpler and more common way to achieve the same as above.
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "reting": book.rating,
        "is_bestseller": book.is_bestselling
    })