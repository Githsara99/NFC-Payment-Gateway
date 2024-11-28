from django.shortcuts import render, redirect

from creator.models import Creator


def index(request):
    creators = Creator.objects.all()

    if request.user.is_authenticated:
        try:
            creator = request.user.creator
        except Exception:
            return redirect('create_app:admin_home')
        
    return render(request, 'core/index.html', {
        'creators': creators
    })
    
def admin_home(request):
    return render(request, 'creator_app/admin_home.html')    