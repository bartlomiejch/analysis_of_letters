from django.shortcuts import render_to_response
from letters_app.models import Letter
from letters_app.forms import LetterForm
from django.core.context_processors import csrf


def get_letter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            my_model = Letter()
            my_model.title = form.cleaned_data['title']
            my_model.text = form.cleaned_data['text']
            my_model.author = form.cleaned_data['author']
            my_model.save()
            letters = Letter.objects.all()
            args = {'letters': letters}
            return render_to_response('result.html', args)
    else:
        form = LetterForm
        context = {'form': form}
        context.update(csrf(request))
    return render_to_response('index.html', context)
