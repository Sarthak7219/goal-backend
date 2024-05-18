from django.shortcuts import render

def index_view(request):
    context = {}
    return render(request, 'index.html', context)


def workshops_view(request):
    context = {}
    return render(request, 'workshops.html', context)


def workshop_detail_view(request, workshop_id):
    context = {
        'workshop_id':workshop_id
    }
    return render(request, 'workshop_detail.html', context)


def about_view(request):
    context = {}
    return render(request, 'about.html', context)


def gallery_view(request):
    context = {}
    return render(request, 'gallery.html', context)


def team_view(request):
    context = {}
    return render(request, 'team.html', context)
