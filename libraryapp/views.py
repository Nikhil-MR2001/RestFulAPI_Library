from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializers


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers





'''

                testing in postman
                
List - http://localhost:8000/api/books/,    -------------- ----------- -----------> GET
Retrieve  - http://localhost:8000/api/books/{id}/,      -------------- ----------- -----------> GET    
Create - http://localhost:8000/api/books/ ,      -------------- ----------- -----------> POST
Update  -  http://localhost:8000/api/books/{id}/        -------------- ----------- -----------> PUT / PATCH

'''