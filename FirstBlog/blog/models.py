from django.db import models

class Post(models.Model):
    '''Данные о посте'''
    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField("Имя Автора", max_length=100)
    date = models.DateField("Дата публикации")
    images = models.ImageField("Изображение", upload_to='image/%Y')

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comments(models.Model):
    '''Комментарии'''
    email = models.EmailField()
    user_name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name="Публикации", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name}, {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP адресс', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)


