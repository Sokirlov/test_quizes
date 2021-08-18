from django.db import models

class QuizeName(models.Model):
    name = models.CharField('Название опроса', max_length=500)
    dataStart = models.DateField('Дата начала опроса', auto_now_add=True)
    dateFinish = models.DateField('Дата окончания опроса')
    description = models.TextField('Описание опроса', null=True, blank=True)
    status = models.BooleanField('Статус (акстив/деактив)')
    class Meta:
        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'
        ordering = ['-status', '-dataStart']
    def __str__(self):
        return self.name

class Questions(models.Model):
    CHOISE_TYPE = (
        ('text', 'Ответ текстом'),
        ('select', 'Ответ с выбором одного варианта'),
        ('multiselect', 'Ответ с выбором нескольких вариантов'),
    )
    quize = models.ForeignKey(QuizeName, related_name='questions', on_delete=models.DO_NOTHING)
    question = models.CharField('Техт вопоса', max_length=1000)
    questionType = models.CharField('Выберте тип ответа', choices=CHOISE_TYPE, max_length=15)

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопросы'
        ordering = ('quize',)

    def __str__(self):
        return self.question

class SingelAnswer(models.Model):
    answer = models.CharField(max_length=250, default='')
    question = models.ForeignKey(Questions, related_name='answerVariant', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.answer

def names():
    try:
        all = Client.objects.all().last()
        last = all.userName
        print('last', last)
    except:
        last ='0'

        print(last)
    newName = int(last) +1
    return newName


class Client(models.Model):
    userName = models.CharField('Имя', max_length=250, default=names)
    quize = models.ForeignKey(QuizeName, on_delete=models.DO_NOTHING, null=True, blank=True)
    questions = models.ForeignKey(Questions, on_delete=models.DO_NOTHING, null=True, blank=True)
    answer = models.ForeignKey(SingelAnswer, on_delete=models.DO_NOTHING, null=True, blank=True)
    writeAnswer = models.CharField('Ответ клиента', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиенты'
    def __str__(self):
        return self.userName
