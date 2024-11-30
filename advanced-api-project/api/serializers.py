from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#class to serialize Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
#validate publication year is not a future time
    def validate_publication_year(self, data):
        current_year = int(datetime.now().year)
        if data > current_year:
            raise serializers.ValidationError('publication can not be future year.')
        return data
    
 #class to serialize the Author model and Book written by that author   
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
