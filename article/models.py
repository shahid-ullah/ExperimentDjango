from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Designation(models.Model):
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.persons


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person, through='Membership', related_name='member_set')

    # def __str__(self):
    #     return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Community(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return self.name


class M2M(models.Model):
    name = models.CharField(max_length=100)
    relation = models.ManyToManyField(
        'self', through='M2Mthrough', symmetrical=False, related_name='double')

    def __str__(self):
        return self.name


class M2Mthrough(models.Model):
    age = models.PositiveIntegerField()
    frm = models.ForeignKey('M2M', on_delete=models.CASCADE,
                            related_name="from_set")
    to = models.ForeignKey('M2M', on_delete=models.CASCADE,
                           related_name="to_set")
