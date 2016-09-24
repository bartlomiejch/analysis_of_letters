import string
from collections import Counter
from django.shortcuts import render_to_response
from letters_app.models import Letter
from letters_app.forms import LetterForm
from django.core.context_processors import csrf


def analize(text):
    my_list = text.split()
    words_only_list = [word.strip(string.punctuation) for word in my_list]
    amount = Counter(words_only_list)
    return amount.most_common(3)


def get_letter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            my_model = Letter()
            my_model.title = form.cleaned_data['title']
            my_model.text = form.cleaned_data['text']
            my_model.author = form.cleaned_data['author']
            my_model.save()
            words = analize(form.cleaned_data['text'])
            first = words[0][0]
            first_amount = words[0][1]
            second = words[1][0]
            second_amount = words[1][1]
            third = words[2][0]
            third_amount = words[2][1]
            args = {}
            args['first'] = first
            args['first_amount'] = first_amount
            args['second'] = second
            args['second_amount'] = second_amount
            args['third'] = third
            args['third_amount'] = third_amount
            return render_to_response('result.html', args)
    else:
        form = LetterForm
        context = {'form': form}
        context.update(csrf(request))
    return render_to_response('index.html', context)
