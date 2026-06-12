from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from .models import Skill, Project, ContactMessage


class LexiAdminSite(AdminSite):
    site_header = "LEXI. Admin"
    site_title  = "Lexitechsolutions"
    index_title = "Dashboard"

    def _get_extra_context(self):
        return {
            "total_projects":    Project.objects.count(),
            "featured_projects": Project.objects.filter(featured=True).count(),
            "recent_projects":   Project.objects.order_by("-created_at")[:6],
            "total_messages":    ContactMessage.objects.count(),
            "unread_messages":   ContactMessage.objects.filter(is_read=False).count(),
            "recent_messages":   ContactMessage.objects.order_by("-created_at")[:5],
            "total_skills":      Skill.objects.count(),
            "top_skills":        Skill.objects.order_by("-proficiency")[:6],
        }

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._get_extra_context())
        return super().index(request, extra_context)

    def app_index(self, request, app_label, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._get_extra_context())
        return super().app_index(request, app_label, extra_context)


lexi_admin = LexiAdminSite(name="admin")


@admin.register(Skill, site=lexi_admin)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ("name", "category", "proficiency", "order")
    list_editable = ("proficiency", "order")
    list_filter   = ("category",)
    ordering      = ("category", "order")


@admin.register(Project, site=lexi_admin)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ("title", "category", "featured", "order", "created_at")
    list_editable = ("featured", "order")
    list_filter   = ("category", "featured")
    search_fields = ("title", "description", "tech_stack")
    ordering      = ("order",)


@admin.register(ContactMessage, site=lexi_admin)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ("name", "email", "subject", "is_read", "created_at")
    list_editable   = ("is_read",)
    list_filter     = ("is_read",)
    search_fields   = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    ordering        = ("-created_at",)