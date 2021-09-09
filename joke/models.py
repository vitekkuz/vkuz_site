from django.db import models


class Joke(models.Model):
    ''' Модель Анекдот '''
    title = models.CharField('Заголовок', max_length=100)
    # slug = models.SlugField('URL', max_length=120)
    content = models.TextField('Текст')
    banner = models.ImageField('Баннер', upload_to='images/', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'Анекдот: {self.title}'

    # def get_absolute_url(self):
    #     return reverse('service_category', kwargs={'slug': self.slug})

    # прописываем, как будет отоборажаться название модели в админке
    class Meta:
        verbose_name = 'Анекдот'
        verbose_name_plural = 'Анекдоты'
