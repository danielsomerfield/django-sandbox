from django.http import JsonResponse
import json

from django.shortcuts import render

from catservice.domain.cat import Cat


def health(request):
    return JsonResponse({'status': 'ok'})


def pet(request, cat_name):
    cat = Cat.from_name(cat_name)
    return JsonResponse({'cat': cat_name, 'action': cat.pet()})


def brush(request, cat_name):
    brush_type = json.loads(request.body)['brush_type']
    if brush_type == 'comfy':
        return JsonResponse({'cat': cat_name, 'action': 'purr'})
    else:
        return JsonResponse({'cat': cat_name, 'action': 'scratch'})


def foo(request):
    return render(request, "foo.html", {"bar": request.GET['baz']})
