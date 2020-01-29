from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    auther = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)


    def __str__(self):
        return '{}-{}'.format(self.name,self.id)


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)


    def __str__(self):
        return self.comment_text




