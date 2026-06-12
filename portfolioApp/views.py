from django.shortcuts import render, redirect
from .models import Skill, Project
from django.core.cache import cache
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home(request):
    skills = Skill.objects.all().order_by('category', 'order')
    projects = Project.objects.all().order_by('order', '-created_at')
    context = {
        'skills_data': skills,
        'projects': projects,
        'also_know': ['OpenCV', 'Matplotlib', 'TensorFlow', 'Celery', 'Redis', 'Netlify', 'Render', 'REST APIs'],
        'form': ContactForm(),
    }
    return render(request, 'home.html', context)


RATE_LIMIT  = 3
RATE_WINDOW = 60 * 60   # 1 hour


def _get_client_ip(request):
    """Returns the real client IP, respecting proxy headers."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "unknown")


def _is_rate_limited(ip):
    """
    Returns True if the IP has exceeded RATE_LIMIT submissions
    within RATE_WINDOW seconds. Uses Django cache as counter store.
    """
    cache_key = f"contact_rate_{ip}"
    count = cache.get(cache_key, 0)

    if count >= RATE_LIMIT:
        return True

    if count == 0:
        cache.set(cache_key, 1, timeout=RATE_WINDOW)
    else:
        cache.incr(cache_key)

    return False


def contact(request):
    if request.method == "POST":
        ip   = _get_client_ip(request)
        form = ContactForm(request.POST)

        if _is_rate_limited(ip):
            messages.warning(request, "You've sent too many messages. Please wait an hour before trying again.",)
            return render(request, "home.html", { "form": form, })

        if form.is_valid():
            form.save()
            messages.success(request,"Message received! We'll be in touch within 1–2 business days.",)
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "home.html", {"form": form, })