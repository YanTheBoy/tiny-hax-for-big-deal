from datacenter.models import Mark, Chastisement, Lesson, Commendation, Schoolkid
from random import choice
import sys
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid_name_surname):
    schoolkid = find_schoolkid(schoolkid_name_surname)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for mark in marks:
        mark.points = choice([4, 5])
        mark.save()


def delete_chastisement(schoolkid_name_surname):
    schoolkid = find_schoolkid(schoolkid_name_surname)
    chantisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chantisement in chantisements:
        chantisement.delete()


def create_commendation(schoolkid_name_surname, subject_title):
    schoolkid = find_schoolkid(schoolkid_name_surname)
    last_lesson = Lesson.objects.filter(
        group_letter=schoolkid.group_letter,
        year_of_study=schoolkid.year_of_study,
        subject__title=subject_title).order_by('-date')[0]
    praises = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
               'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
               'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!',
               'Ты сегодня прыгнул выше головы!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
               'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!',
               'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!',
               'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Я поражен!'
               ]
    Commendation.objects.create(
        text=choice(praises),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )

def find_schoolkid(schoolchild):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolchild)
    except ObjectDoesNotExist:
        sys.exit('Указаный человек не найден.')
    except MultipleObjectsReturned:
        sys.exit('Найдено несколько человек. Уточните поисковый запрос.')
    return schoolkid
