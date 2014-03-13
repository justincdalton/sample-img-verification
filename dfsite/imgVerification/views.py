
import hashlib
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.cache import never_cache
from imgVerification.models import ImgVerificationHelper

def index(request):
    template = loader.get_template('imgVerification/index.html')
    return HttpResponse(template.render(RequestContext(request)))

@never_cache
def send_img(request):
    helper = ImgVerificationHelper()

    request.session["imgVerHash"] = hashlib.md5(helper.numString).hexdigest()

    response = HttpResponse(mimetype="image/jpeg")
    response["Expires"] = "Mon, 26 Jul 1997 05:00:00 GMT"
    response["Last-Modified"] = datetime.now().strftime("%a, %d %b %Y %T %z")
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"

    helper.img.save(response, "JPEG")

    return response

def submit(request):
    imgver = request.POST.get("imgver", "").strip()

    formhash = hashlib.md5(imgver).hexdigest()

    if (formhash == request.session["imgVerHash"]):
        response = "It Matches!!"
    else:
        response = "It doesn't match..."

    return HttpResponse(response)
