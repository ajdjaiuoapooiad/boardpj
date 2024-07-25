from django.db import models

class Post(models.Model):
    title=models.CharField('タイトル',max_length=100)
    text=models.TextField('本文')
    author=models.CharField('投稿者',max_length=100)
    image=models.ImageField(upload_to='media/images')
    good=models.IntegerField('いいね')
    read=models.IntegerField('既読')
    read_text=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title