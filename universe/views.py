from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ObjectCategory, AstronomicalObject

def index(request):
    categories = ObjectCategory.objects.all()
    
    # Base queryset
    queryset = AstronomicalObject.objects.all()

    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        queryset = queryset.filter(
            Q(name__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(full_description__icontains=search_query)
        )

    # Category filtering
    category_slug = request.GET.get('category', '')
    if category_slug:
        queryset = queryset.filter(object_type__slug=category_slug)

    # Pagination
    paginator = Paginator(queryset, 9) # Show 9 objects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'search_query': search_query,
        'current_category': category_slug,
    }
    return render(request, 'universe/index.html', context)

def detail(request, slug):
    obj = get_object_or_404(AstronomicalObject, slug=slug)
    related_objects = AstronomicalObject.objects.filter(object_type=obj.object_type).exclude(id=obj.id)[:3]
    
    context = {
        'obj': obj,
        'related_objects': related_objects,
    }
    return render(request, 'universe/detail.html', context)
