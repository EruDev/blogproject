from django.db import models
from django.contrib.auth.admin import User
from django.shortcuts import reverse
from django.utils.six import python_2_unicode_compatible



@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100) # 分类名

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100) # 标签名

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100) # 文章标题
    body = models.TextField() # 文章内容
    created_time = models.DateTimeField() # 创建时间
    modified_time = models.DateTimeField() # 修改时间
    excerpt = models.CharField(max_length=200, blank=True) # 摘要, blank=True 允许为空
    tags = models.ManyToManyField(Tag, blank=True)  # 因为一篇文章下可能会有多个标签, 所以这里定义的是多对多关系
    category = models.ForeignKey(Category) # 一个分类下面会有多篇文章, 所以定义为一对多, 也就是外键关系
    author = models.ForeignKey(User) # User模型是 django 自带的

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

