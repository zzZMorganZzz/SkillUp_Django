from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Account(models.Model):
    """
    Модель профилей пользователей
    """
    Account_FirstName = models.CharField('FirstName', max_length=20, blank=True, null=True)
    Account_Name = models.CharField('Name', max_length=20, blank=True, null=True)
    Account_LastName = models.CharField('LastName', max_length=30, blank=True, null=True)
    Account_NickName = models.CharField('Nickname', max_length=20)
    Account_Birthday = models.DateField('Birthday', blank=True, null=True)
    Account_RegistretedAt = models.DateTimeField('RegistreteAt', auto_now_add=True)

    def __str__(self):
        return self.Account_NickName

class Tag(models.Model):
    """
    Модель тегов
    """
    Tag_Name = models.CharField('TagName', max_length=30, blank=True, null=True) 

    def __str__(self):
        return self.Tag_Name



class Post(models.Model):
    """
    Модель публикаций
    """
    Post_Title = models.CharField('Caption', max_length=50)
    Post_Context = models.TextField('Context')
    Post_CreatedAt = models.DateTimeField('DatePub',auto_now_add=True)

    Owner = models.ForeignKey('Account', verbose_name='Owner', 
                                related_name='r_PostAccount', on_delete=models.CASCADE)

    TagCollection = models.ManyToManyField('Tag', verbose_name='Tag', related_name='r_PostsTag')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.Post_Title


class Likes (models.Model):
    """
    Модель лайков
    """
    PostLink = models.ForeignKey('Post', verbose_name='Post', 
                                related_name='r_PostLikes', on_delete=models.CASCADE)
    Owner = models.ForeignKey('Account', verbose_name='Owner', 
                                related_name='r_LikesAccount', on_delete=models.CASCADE)

