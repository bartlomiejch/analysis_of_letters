from django.shortcuts import render_to_response
from letters_app.models import Letter


def get_letter(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        letter = Letter.objects.create(title=title, text=text, author=author)
        return render_to_response('result.html')
    return render_to_response('index.html')
