from django.db import models
from django.urls import reverse
from django.utils.text import slugify  # добавлен импорт

class PlanetarySystem(models.Model):
    # Общая информация
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Star(models.Model):
    # Общая информация
    name = models.CharField(max_length=100, verbose_name="Название звезды")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="star_photo/", verbose_name="Фото")

    # Детали
    planetary_system = models.ManyToManyField(
        PlanetarySystem,
        related_name='stars',
        verbose_name="Планетарные системы",
    )

    status = models.TextField(verbose_name="Статус")
    aged = models.FloatField(verbose_name="Возраст в миллиардах лет")

    # Служебная информация
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("star-detail", kwargs={"slug": self.slug})
    
    def get_planetary_system(self):
        """Метод для получения перечня планетарных систем"""
        return ', '.join(system.name for system in self.planetary_system.all())

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"

class Planet(models.Model):
    # Общая информация
    name = models.CharField(max_length=100, verbose_name="Название планеты")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="planet_photo/", verbose_name="Фото")

    # Детали
    planetary_system = models.ForeignKey(
        PlanetarySystem,
        on_delete=models.CASCADE,
        related_name="planets",
        verbose_name="Планетарная система",
    )

    aged = models.FloatField(verbose_name="Возраст в миллиардах лет")

    # Служебная информация
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("planet-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"
