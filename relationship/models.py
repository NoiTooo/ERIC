from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """ ユーザー投稿 """
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:5]


class Profile(models.Model):
    """ ユーザーに写真を追加 """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')


class Follow(models.Model):
    """ フォロー・フォロワーの管理 """
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'FROM：{str(self.user)}――＞TO：{str(self.follow_user)}'


class Comment(models.Model):
    """ コメントの管理 """
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)