from django.db import models


class Advert(models.Model):
    author = models.CharField("Автор", max_length=12)
    advert = models.TextField("Объявление")
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.author, self.created)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    author = models.CharField("Автор", max_length=12)
    comment = models.TextField("Коментарий")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name="Объявление", related_name="comments")

    def __str__(self):
        return "{} {}".format(self.author, self.comment)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"


class Tag(models.Model):
    title = models.CharField("Категория", max_length=10)
    advert = models.ManyToManyField(Advert, verbose_name="Объявления", blank=True, related_name="tags")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"