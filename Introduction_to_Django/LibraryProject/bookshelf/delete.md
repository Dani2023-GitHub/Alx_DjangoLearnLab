<!-- Deletion on instance of book-->

book = Book.objects.all[0]
book.delete()
