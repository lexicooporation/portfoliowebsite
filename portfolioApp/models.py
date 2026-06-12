from django.db import models
from cloudinary.models import CloudinaryField 

# Create your models here.
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework'),
        ('ml', 'ML / Data Science'),
        ('tool', 'Tool / DevOps'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome or Devicons class", blank=True)
    proficiency = models.PositiveIntegerField(default=80,help_text="Proficiency percentage (0–100)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name




class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
        ('data', 'Data Analysis'),
        ('cv', 'Computer Vision'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='web')
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated tech tags")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.subject}"
