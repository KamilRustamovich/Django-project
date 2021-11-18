from django.db import models
from django.urls import reverse
from django.conf import settings



class Faculties(models.Model):
    title = models.CharField(max_length=100, verbose_name='Факультет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факультеты'
        verbose_name_plural = 'Факултеты'


class Departments(models.Model):
    title = models.CharField(max_length=100, verbose_name='Кафедра')
    faculty = models.ForeignKey(Faculties, on_delete=models.PROTECT, verbose_name='Факультет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Groups(models.Model):
    title = models.CharField(max_length=100, verbose_name='Группа')
    department = models.ForeignKey(Departments, on_delete=models.PROTECT, verbose_name='Кафедра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Students(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    faculty = models.ForeignKey('Faculties', on_delete=models.PROTECT, verbose_name="Факультет")
    department = models.ForeignKey('Departments', on_delete=models.PROTECT, verbose_name="Кафедра")
    group = models.ForeignKey('Groups', on_delete=models.PROTECT, verbose_name="Группа")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'

class Obhodnoi(models.Model):
    select_status = (
        ('В обработке', 'В обработке'),
        ('Завершен', 'Завершен'),
        ('Отклонён', 'Отклонён'),
    )
    student = models.OneToOneField(Students, on_delete=models.SET_NULL, null=True, verbose_name="Студент")
    dateOfBirth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    statusLibrary = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус библиотеки')
    statusInternationalDepartment = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус международного отдела')
    passportPhoto = models.FileField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография паспорта')
    statusPassporttiska = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус паспортистки')
    statusKafedra = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус кафедры')
    statusAccounting = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус бухгалтерии')
    statusDormitories = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус общежитии')
    statusStudentOK = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус студенческого отдела кадров')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    document = models.CharField(max_length=30, choices=select_status, default=select_status[0][0], verbose_name='Статус документа')

    def __str__(self):
        return '{}'.format(self.student)

    class Meta:
        verbose_name = 'Обходной лист'
        verbose_name_plural = 'Обходные листы'
        ordering = ['-time_create']