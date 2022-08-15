from django.http import HttpRequest, HttpResponse


# Create your views here.
def sample_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Request object below:\n{request!s}", content_type="text/plain")
