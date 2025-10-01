from django.db import models

class Post(models.Model):
    title = models.CharField("글 제목", max_length=40)
    content = models.TextField("글 내용")
    thumbnail = models.ImageField("썸네일", upload_to="post", blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField("댓글 내용")
    
    def __str__(self):
        return self.comment