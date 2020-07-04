from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.settings import PASSWORD
from web.models import Publication, Feedback, Comments


def status(request):
    return HttpResponse("Status OK <a href = '/'> index</a>")


def index(request):
    response = render(request, 'main.html')
    return HttpResponse(response)


def page404(request):
    response = render(request, 'page404.html')
    return HttpResponse(response)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')

        if email or phone:
            if name:
                Feedback.objects.create(name=name,
                                        email=email,
                                        phone=phone,
                                        text=text)
                return render(request, 'contacts.html', {
                    'send_status': 'Sended. Thanks for feedback.',
                    'color': 'green'
                })
            else:
                return render(request, 'contacts.html', {
                    'send_status': 'Not sended. Enter your name',
                    'color': 'red'
                })
        else:
            return render(request, 'contacts.html', {
                    'send_status': 'Not sended. Both email and phone shouldnt be empty',
                    'color': 'red'
            })

    response = render(request, 'contacts.html', {
                    'send_status': '',
                    'color': 'red'
            })
    return HttpResponse(response)


def publications(request):
    publications_sorted = Publication.objects.order_by('-date')

    response = render(request, 'publications.html', {
        'publications':  publications_sorted,
        'title': 'ALL'
    })
    return HttpResponse(response)


def publication(request, pub_id):

    try:
        comments = Comments.objects.filter(pub=pub_id)
    except Comments.DoesNotExist:
        return redirect('/page404/')

    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/page404/')

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        if name and text:

            Comments.objects.create(name=name,
                                    text=text,
                                    pub=pub_id)

            return render(request, 'publication.html', {
                'publication': publication,
                'pub_id': pub_id,
                'comments': comments
            })

        else:
            return render(request, 'publication.html', {
                'publication': publication,
                'pub_id': pub_id,
                'comments': comments
            })

    response = render(request, 'publication.html', {
        'publication': publication,
        'pub_id': pub_id,
        'comments': comments
    })
    return HttpResponse(response)


def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        password = request.POST.get('password')
        if password != PASSWORD:
            return render(request, 'post.html', {
                'error': 'wrong password'
            })

        if title and text and password:
            Publication.objects.create(title=title, text=text)
            return redirect('/publications/')
        else:
            return render(request, 'post.html', {
                          'error': 'title and text should not be empty'
            })
    response = render(request, 'post.html')
    return HttpResponse(response)

