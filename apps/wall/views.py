from django.shortcuts import render, redirect
# from .models import Job
from ..login_regs.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    me = User.objects.get(id = request.session['user_id'])
    context = {
        'user': me,
    }
    return render(request, "wall/index.html", context)
