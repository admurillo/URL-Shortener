import random
import string
from django.shortcuts import render
from .models import URLs
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import URLForm


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        form = URLForm(request.POST)

        if form.is_valid():
            try:
                u = URLs.objects.get(URL=request.POST['url'])

            except URLs.DoesNotExist:
                shortened = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
                u = URLs(URL=request.POST['url'], shortened=shortened)

            u.save()

    urls_list = URLs.objects.all()
    form = URLForm()
    context = {
        'urls_list': urls_list,
        'form': form
    }

    return render(request, 'acorta/index.html', context)


@csrf_exempt
def get_content(request, shortened):
    try:
        u = URLs.objects.get(shortened=shortened)
        url = u.URL
        return HttpResponseRedirect(url)
    except URLs.DoesNotExist:
        context = {
            'shortened': shortened
        }
        return render(request, 'acorta/error.html', context)
