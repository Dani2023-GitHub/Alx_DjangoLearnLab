from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# Create your views here.
def list_books(request):
    books=Book.objects.all()

    return render(request, template_name='relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    model = Library
    template_name="relationship_app/library_detail.html"
    context_object_name = 'library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect("home")  # Redirect to home or any page you specify
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin-only view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian-only view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member-only view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
