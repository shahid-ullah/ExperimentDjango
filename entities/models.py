from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Origin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entity(models.Model):
    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHERS = "Others/Unknown"

    name = models.CharField(max_length=100)
    alternative_name = models.CharField(
            max_length=100,
            null = True,
            blank = True,
        )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=100,
        choices=(
            (GENDER_MALE, GENDER_MALE),
            (GENDER_FEMALE, GENDER_FEMALE),
            (GENDER_OTHERS, GENDER_OTHERS),
        )
    )

    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Hero(Entity):

    class Meta:
        verbose_name_plural = "Heroes"

    headshot = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")
    not_editable_field = models.CharField(editable=False, max_length=200)
    is_immortal = models.BooleanField(default=True)
    benevolence_factor = models.PositiveIntegerField(
        help_text="How benevolent this hero is?"
    )
    arbitrariness_factor = models.PositiveIntegerField(
        help_text="How arbitrary this hero is?"
    )

    # relationships
    father = models.ForeignKey(
        "self", related_name="children", null=True, blank=True, on_delete=models.SET_NULL
    )
    mother = models.ForeignKey(
        "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )
    spouse = models.ForeignKey(
        "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )


class Villian(Entity):
    is_immortal = models.BooleanField(default=False)
    malevolence_factor = models.PositiveSmallIntegerField(
        help_text="How malevolent this villian is?"
        )
    power_factor = models.PositiveSmallIntegerField(
        help_text="How powerfull this villian is?"
        )
    is_unique = models.BooleanField(default=True)
    count = models.PositiveSmallIntegerField(default=1)
