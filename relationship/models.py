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


class Follow(models.Model):
    """ フォロー・フォロワーの管理 """
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'FROM：{str(self.user.account_name)}――＞TO：{str(self.follow_user.account_name)}'


class Comment(models.Model):
    """ コメントの管理 """
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.author.account_name)}：{str(self.date_posted)}'


class Intimate(models.Model):
    """ 親密な関係 """
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    request = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name='登録日', auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return f'{str(self.sender.account_name)}――{str(self.receiver.account_name)}' \
               f'｜request―{self.request}｜approval―{self.approval}'