from django.db import models


class Tutor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя преподавателя')
    position = models.CharField(max_length=256, verbose_name='Должность')
    load = models.FloatField(default=1, verbose_name='Ставка')
    additional_work = models.TextField(blank=True, null=True, verbose_name='Дополнительная работа')
    workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.CASCADE,
        verbose_name='Аудитория'
    )
    disciplines = models.ManyToManyField(
        'Discipline',
        related_name='tutors',
        verbose_name='Дисциплины'
    )

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
        ordering = ['name']

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название дисциплины')
    description = models.TextField(blank=True, verbose_name='Описание дисциплины')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор',
                            help_text="Идентификатор страницы для URL; "
                                      "разрешены символы латиницы, цифры, дефис и подчёркивание.",
                            )

    class Meta:
        verbose_name = 'дисциплина'
        verbose_name_plural = 'дисциплины'
        ordering = ['name']

    def __str__(self):
        return self.name


class Workplace(models.Model):
    number = models.CharField(max_length=5, verbose_name='Номер кабинета')

    class Meta:
        verbose_name = 'преподавательская'
        verbose_name_plural = 'преподавательские'
        ordering = ['number']

    def __str__(self):
        return self.number
