from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


def post_student_save(sender , instance , **kwargs):
    print("post has been saved")

def post_student_delete(sender , instance , **kwargs):
    print("post has been deleted")


post_delete.connect(post_student_delete,Student)

pre_save.connect(post_student_save, Student)
post_save.connect(post_student_save,Student)