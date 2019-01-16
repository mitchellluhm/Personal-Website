from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    text = models.TextField()
    start_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    '''
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    '''

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
