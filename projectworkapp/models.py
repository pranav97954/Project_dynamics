from django.db import models

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

class UploadFiles(models.Model):
    field_name = models.FileField(upload_to=None, max_length=254)
    


 
