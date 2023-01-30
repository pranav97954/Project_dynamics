from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dataapp(models.Model):
    t = models.IntegerField(blank=True)
    h = models.IntegerField(blank=True)
    r = models.DecimalField(max_digits=10, decimal_places=10, default="")
    d = models.DecimalField(max_digits=10, decimal_places=10, default="")
    l = models.DecimalField(max_digits=10, decimal_places=10, default="")
    segment_i_node = models.IntegerField(blank=True)
    index = models.IntegerField(blank=True)
    nodes = models.IntegerField(blank=True)
    xpos = models.DecimalField(max_digits=10, decimal_places=10, default="")
    ypos = models.DecimalField(max_digits=10, decimal_places=10, default="")
    zpos = models.DecimalField(max_digits=10, decimal_places=10, default="")
    volume_ratio = models.IntegerField(blank=True)
    hNode = models.IntegerField(blank=True)
    tNode = models.IntegerField(blank=True)
    nodes_mesh = models.IntegerField(blank=True)
    xpos_mesh = models.DecimalField(max_digits=10, decimal_places=10, default="")
    xpos_mesh = models.DecimalField(max_digits=10, decimal_places=10, default="")
    xpos_mesh = models.DecimalField(max_digits=10, decimal_places=10, default="")

class upload_file(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
    added_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.file_name