<!-- CRUD operation -->

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year= 1949)

Book.objects.get(title="1984")
<Book: Book object (1)>

Book.objects.all().values()
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

y = Book.objects.all()[0]
y.title= "Nineteen Eighty-Four"
y.save

x = Book.objects.all()[0]
x.delete()
(1, {'bookshelf.Book': 1})
