from django.http import JsonResponse
def home(request):
    return JsonResponse({'i hello':'hoo'})
