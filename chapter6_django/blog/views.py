from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Author

def index(request):
    authors = Author.objects.all()
    return render(request, 'blog/index.html', {'authors': authors})

def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if request.method == 'POST':
        author.name = request.POST.get('name')
        author.description = request.POST.get('description')
        author.save()
        
    # Always return a form template, passing the author object
    return render(request, 'blog/edit_author.html', {'author': author})

def update_user(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        # Update the author's details
        name = request.POST.get('name')
        description = request.POST.get('description')

        if not name or not description:
            return HttpResponse("Missing required fields", status=400)

        author.name = name
        author.description = description
        author.save()

        # Return the updated HTML
        return HttpResponse(f"""
        <div class="card" style="width: 18rem;"
        hx-target="this"
        hx-swap="outerHTML"
        >
            <div class="card-body">
                <h5 class="card-title">{name}</h5>
                <p class="card-text">
                    {description}
                </p>
                <button href="#" class="btn btn-primary"
                hx-get="/user/{id}/edit">
                    Click To Edit
                </button>
            </div>
        </div>
        """)

    return HttpResponse("Invalid request", status=405)  # Method Not Allowed
