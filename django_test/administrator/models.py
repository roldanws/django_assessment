from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from authentication.models import CustomUser

# Create your models here.

class Administrator(models.Model):
    ROL = (
        (False, "administrator"),
        (True, "super_administrator"),
    )
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rol = models.BooleanField(choices=ROL, verbose_name = 'Rol', default=True)
    created = models.DateTimeField(verbose_name = 'fecha de creacion', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'ultima modificacion')
    def __str__(self): 
        return self.usuario.username
    
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return True



@receiver(post_save, sender=User)
def crear_usuario_administrator(sender, instance, created, **kwargs):
    if created:
        Administrator.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_administrator(sender, instance, **kwargs):
    instance.administrator.save()