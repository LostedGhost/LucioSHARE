from django.shortcuts import render, redirect
from app.models import *

# Create your views here.
def index(request):
    error = request.session.pop('error', None)
    success = request.session.pop('success', None)
    if request.POST:
        slug = request.POST.get('slug', None)
        try:
            media = Media.objects.get(slug=slug)
        except:
            request.session["error"] = "Le slug rentré est invalide !!!"
            return redirect("/")
        return redirect(f"/view/{slug}")
    return render(request, 'app/index.html',{
        'success': success,
        'error': error
    })

def upload(request):
    error = request.session.pop('error', None)
    success = request.session.pop('success', None)
    if request.POST:
        media = request.FILES.get('media',None)
        media = Media(document=media)
        media.save()
        return redirect(f"/view/{media.slug}")
    return render(request, 'app/upload.html',{
        'success': success,
        'error': error
    })

def view(request, slug):
    error = request.session.pop('error', None)
    success = request.session.pop('success', None)
    try:
        media = Media.objects.all().get(slug=slug)
    except:
        request.session["error"] = "Le slug rentré est invalide !!!"
        return redirect("/")
    return render(request, 'app/view.html',{
        "media": media,
        'success': success,
        'error': error
    })