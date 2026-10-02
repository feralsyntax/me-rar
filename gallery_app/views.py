from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image
from gallery_app.forms import SignUpForm
from django.contrib.auth import login, authenticate


# Create your views here.
def galleries(request):
    galleries = Image.galleries()

    return render(request,'galleries/gallery-today.html',{"galleries":galleries})


def gallery_today(request):
    """
    gallery view function
    :param request: http request
    :return: images for a particular day
    """
    date = dt.date.today()
    gallery = Image.todays_gallery()

    return render(request,'galleries/gallery-today.html',{"date":date,"gallery":gallery})


def past_days_gallery(request,past_date):
    """
    :param request: http request
    :param past_date: date from the url
    :return: galleries from a past date
    """

    try:
        # convert data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # raise 404 when value error is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    gallery = Image.days_gallery(date)

    return render(request,'galleries/past-gallery.html',{"date":date,"gallery":gallery})

def tag_results(request):

    if 'image' in request.GET and request.GET["image"]:
        tag_term = request.GET.get("image")
        searched_images = Image.search_by_tag(tag_term)

        message = f"{tag_term}"

        return render(request,'galleries/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search.html',{"message":message})


def category_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category_term = request.GET.get("image")
        searched_images = Image.search_by_category(category_term)

        message = f"{category_term}"

        return render(request,'galleries/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search.html',{"message":message})


def location_results(request):

    if 'image' in request.GET and request.GET["image"]:
        location_term = request.GET.get("image")
        searched_images = Image.search_by_location(location_term)

        message = f"{location_term}"

        return render(request,'galleries/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for an image yet"

        return render(request,'galleries/search.html',{"message":message})

# def search_category(request):
#
#     if 'image' in request.GET and request.GET["image"]:
#         category_term = request.GET.get("image")
#         searched_images = Image.search_by_category(category_term)
#
#         message = f"{category_term}"
#
#         return render(request,'galleries/search.html',{"message":message,"images":searched_images})
#
#     else:
#         message = "You haven't searched for an image yet"
#
#         return render(request,'galleries/search.html',{"message":message})
#



def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)

    except DoesNotExist:
        raise Http404()

    return render(request,'galleries/image.html',{"image":image})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
