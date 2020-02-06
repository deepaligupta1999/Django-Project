from django.db import models

class TaskModel(models.Model):
    task=models.TextField()
    date=models.DateTimeField(auto_now=True)
    complete=models.BooleanField(default=False)

    class Meta:
        ordering=['date']
        #verbose_name='deepali'
        verbose_name_plural='TaskModel'

    def __str__(self):
        return self.task
