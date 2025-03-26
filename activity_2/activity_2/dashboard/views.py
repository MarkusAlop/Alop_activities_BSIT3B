from django.shortcuts import render
from django import template

register = template.Library()

@register.filter
def currency_format(value):
    """Format numbers as currency."""
    return f"${int(value):,}"

def dashboard_view(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'dashboard.html', {'data': data})
