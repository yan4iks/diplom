from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from .models import PlanetarySystem, Star, Planet

def index(request):
    stars = Star.objects.filter(is_published=True).order_by('name')
    planets = Planet.objects.filter(is_published=True).order_by('name')

    # Пагинация звёзд
    paginator_stars = Paginator(stars, 3)
    page_number_star = request.GET.get('page-star', 1)
    try:
        page_obj_stars = paginator_stars.get_page(page_number_star)
    except PageNotAnInteger:
        page_obj_stars = paginator_stars.page(1)
    except EmptyPage:
        page_obj_stars = paginator_stars.page(paginator_stars.num_pages)

    # Пагинация планет
    paginator_planets = Paginator(planets, 3)
    page_number_planet = request.GET.get('page-planet', 1)
    try:
        page_obj_planets = paginator_planets.get_page(page_number_planet)
    except PageNotAnInteger:
        page_obj_planets = paginator_planets.page(1)
    except EmptyPage:
        page_obj_planets = paginator_planets.page(paginator_planets.num_pages)

    context = {
        'page_obj_stars': page_obj_stars,
        'page_obj_planets': page_obj_planets,
        'title': "Astro - Главная"
    }

    return render(request, 'astro_objects/index.html', context=context)

def star_detail(request, slug):
    star = get_object_or_404(Star, slug=slug)
    
    systems = star.planetary_system.all()
    planets_in_system = Planet.objects.filter(planetary_system__in=systems)
    stars_in_system = Star.objects.filter(planetary_system__in=systems)

    context = {
        'star': star,
        'planets': planets_in_system,
        'stars': stars_in_system,
        'title': f'Звезда {star.name}'
    }
    return render(request, 'astro_objects/star_detail.html', context=context)

def planet_detail(request, slug):
    planet = get_object_or_404(Planet, slug=slug)
    
    system = planet.planetary_system
    

    planets_in_system = Planet.objects.filter(planetary_system=system)
    stars_in_system = Star.objects.filter(planetary_system=system)
    
    context = {
        'planet': planet,
        'planets': planets_in_system,
        'stars': stars_in_system,
        'title': f'Планета {planet.name}'
    }
    return render(request, 'astro_objects/planet_detail.html', context=context)

def planets_by_planetary_system(request, pk):
    planetary_system = get_object_or_404(PlanetarySystem, pk=pk)
    planets = planetary_system.planets.filter(is_published=True)

    paginator = Paginator(planets, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': f"Планеты в системе: {planetary_system.name}"
    }
    return render(request, 'astro_objects/planet_list.html', context=context)

def stars_by_planetary_system(request, pk):
    planetary_system = get_object_or_404(PlanetarySystem, pk=pk)
    stars = planetary_system.stars.filter(is_published=True)

    paginator = Paginator(stars, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': f"Планеты в системе: {planetary_system.name}"
    }
    return render(request, 'astro_objects/planet_list.html', context=context)