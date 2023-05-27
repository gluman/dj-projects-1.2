from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}




def index(request):
    return HttpResponse('Hello')


def calc(bludo, count):
    recipe = DATA[bludo]
    result = {}
    for ing, val in recipe.items():
        result[ing] = val * count
    return result


def recipe_(request, bludo):
    count = int(request.GET.get('servings', 1))
    recipe = calc(bludo, count)
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)