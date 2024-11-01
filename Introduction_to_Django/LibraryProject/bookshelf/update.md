<!-- updating the data -->

book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()
