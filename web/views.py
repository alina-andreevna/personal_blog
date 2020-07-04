from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.settings import PASSWORD, AUTHORIZED
from web.models import Publication, Feedback, Comments



def status(request):
    return HttpResponse("Status OK <a href = '/'> index</a>")


def index(request):
    global AUTHORIZED

    if request.method == 'POST':
        password = request.POST.get('password')

        if password == PASSWORD:
            AUTHORIZED = True
        else:
            AUTHORIZED = False

    response = render(request, 'main.html', {
                    'autorized': AUTHORIZED})
    return HttpResponse(response)


def page404(request):
    global AUTHORIZED
    response = render(request, 'page404.html', {
                    'autorized': AUTHORIZED})
    return HttpResponse(response)


def contact(request):
    global AUTHORIZED
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
                    'color': 'green',
                    'autorized': AUTHORIZED})
            else:
                return render(request, 'contacts.html', {
                    'send_status': 'Not sended. Enter your name',
                    'color': 'red',
                    'autorized': AUTHORIZED})
        else:
            return render(request, 'contacts.html', {
                    'send_status': 'Not sended. Both email and phone shouldnt be empty',
                    'color': 'red',
                    'autorized': AUTHORIZED})

    response = render(request, 'contacts.html', {
                    'send_status': '',
                    'color': 'red',
                    'autorized': AUTHORIZED})
    return HttpResponse(response)


def publications(request):
    global AUTHORIZED

    publications_sorted = Publication.objects.order_by('-date')

    response = render(request, 'publications.html', {
                    'publications':  publications_sorted,
                    'title': 'ALL',
                    'autorized': AUTHORIZED})
    return HttpResponse(response)


def publication(request, pub_id):
    global AUTHORIZED

    try:
        comments = Comments.objects.filter(pub=pub_id)
    except Comments.DoesNotExist:
        return redirect('/page404/', {
                    'autorized': AUTHORIZED})

    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/page404/', {
                    'autorized': AUTHORIZED})

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
                'comments': comments,
                'autorized': AUTHORIZED})

        else:
            return render(request, 'publication.html', {
                'publication': publication,
                'pub_id': pub_id,
                'comments': comments,
                'autorized': AUTHORIZED})

    response = render(request, 'publication.html', {
        'publication': publication,
        'pub_id': pub_id,
        'comments': comments,
        'autorized': AUTHORIZED})
    return HttpResponse(response)


def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        password = request.POST.get('password')
        if password != PASSWORD:
            return render(request, 'post.html', {
                        'error': 'wrong password',
                        'autorized': AUTHORIZED})

        if title and text and password:
            Publication.objects.create(title=title, text=text)
            return redirect('/publications/', {
                        'autorized': AUTHORIZED})
        else:
            return render(request, 'post.html', {
                        'error': 'title and text should not be empty',
                        'autorized': AUTHORIZED})
    response = render(request, 'post.html', {
                        'autorized': AUTHORIZED})
    return HttpResponse(response)

