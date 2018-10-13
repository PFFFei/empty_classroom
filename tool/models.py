from django.db import models

# Create your models here.

class Monday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Tuesday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Wednesday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Thursday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Friday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Saturday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom

class Sunday(models.Model):
    
    classroom = models.CharField('教室',max_length=32)
    lesson_0102 = models.CharField('0102',max_length=64)
    lesson_0304 = models.CharField('0304',max_length=64)
    lesson_05 = models.CharField('05',max_length=64)
    lesson_0607 = models.CharField('0607',max_length=64)
    lesson_0809 = models.CharField('0809',max_length=64)
    lesson_10 = models.CharField('10',max_length=64)
    lesson_1112 = models.CharField('1112',max_length=64)
    lesson_13 = models.CharField('13',max_length=64)

    def __str__(self):
        return self.classroom
