<!-- updating the data -->

x = Book.objects.all()[0]
x.title = "Nineteen Eighty-Four"
x.save()
