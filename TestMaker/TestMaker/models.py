from django.db import models

class TestProblem():
    def __init__(self):
        problem = models.TextField()
        answer = models.TextField()

# Create your models here.
class Test(models.Model):
    testTitle = models.CharField(max_length=60)
    problemsList = {TestProblem()}

    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.testTitle