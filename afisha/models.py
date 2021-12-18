import datetime

from django.db import models
from django.utils import timezone


class Film(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'

    film_title = models.CharField('Название', max_length=255)
    film_description = models.TextField('Описание')
    film_original_title = models.CharField('Оригинальное название', max_length=255)
    film_year = models.IntegerField('Год выпуска')
    film_producer = models.CharField('Режиссер', max_length=255)
    film_roles = models.ManyToManyField('Actor', verbose_name='В главных ролях')
    film_length = models.IntegerField('длительность фильма (мин)')
    film_premiere = models.DateField('Дата премьеры в мире')
    film_age_limit = models.IntegerField('Возрастное ограничение')
    film_genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    film_rent_start_date = models.DateField('Начало проката')
    film_rent_end_date = models.DateField('Конец проката')
    film_poster = models.ImageField('Постер', blank=True)
    is_film_in_rent = models.BooleanField('В прокате ли', default=1)

    def get_film_absolute_url(self):
        return f'film/{self.id}'

    def get_film_age_limit_str(self):
        return f'{self.film_age_limit}+'

    get_film_age_limit_str.short_description = 'Возрастное ограничение'

    def set_is_film_in_rent(self):
        try:
            if self.film_rent_start_date <= timezone.now().date() <= self.film_rent_end_date:
                self.is_film_in_rent = True
            else:
                self.is_film_in_rent = False
        except Exception as e:
            print(e)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_is_film_in_rent()

    def __str__(self):
        return f'{self.film_title}'


class Show(models.Model):
    class Meta:
        verbose_name = 'Дата показа'
        verbose_name_plural = 'Дата показа'

    show_date = models.DateTimeField('Дата показа', unique=True)
    show_film = models.ForeignKey('Film', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Фильм')

    def __str__(self):
        return f'{self.show_date}'


class Actor(models.Model):
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актер'

    actor_name = models.CharField('Актер', max_length=255)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанр'

    genre = models.CharField('Жанр', max_length=255)

    def __str__(self):
        return self.genre


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв'

    review_author = models.CharField('Автор отзыва', max_length=255)
    review_text = models.TextField('Отзыв')
    review_film = models.ForeignKey('Film', on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return f'{self.review_author} {self.review_film} {self.review_text}'
