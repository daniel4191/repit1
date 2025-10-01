from django.db import models

class Post(models.Model):
    title = models.CharField("글 제목", max_length=40)
    content = models.TextField("글 내용")
    thumbnail = models.ImageField("썸네일")
    
    def __str__(self):
        return f"{self.title}: {self.content}"
    
class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField("댓글 내용")
    
    def __str__(self):
        return self.comment