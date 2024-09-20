from django.db import models

# Create your models here.

class AutorizacionMedica(models.Model):

    TIPOS_AUTORIZACION = (
        ('examenes', 'Exámenes Diagnósticos'),
        ('procedimientos', 'Procedimientos Quirúrgicos'),
        ('maternidad', 'Servicios de Maternidad'),
        ('vacunacion', 'Servicios de Vacunación'),
        ('dermatologia', 'Servicios de Dermatología'),
        ('laboratorio', 'Servicio de Laboratorio'),
        ('otros', 'Otros Servicios'),
    )

    tipo_autorizacion = models.CharField(
        max_length=50, 
        choices=TIPOS_AUTORIZACION, 
        default='otros'
    )

    estado = models.CharField(
        max_length=10, 
        choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], 
        default='pendiente'
    )
    paciente = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.paciente} - {self.get_tipo_autorizacion_display()} - {self.estado}'

class Pacientes(models.Model):

    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre}'