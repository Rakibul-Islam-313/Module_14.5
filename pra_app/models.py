from django.db import models

# Create your models here.

class My_Models(models.Model):
   
    roll = models.IntegerField(primary_key=True)
    my_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(max_digits=20, decimal_places=4)
    durationfield = models.DurationField()
    file = models.FileField()
    ip_address = models.GenericIPAddressField()
    image = models.ImageField()
    json = models.JSONField()
    positive_integer_big = models.PositiveIntegerField()
    small_integer = models.PositiveSmallIntegerField()
    Slugfield = models.SlugField()
    uuid = models.UUIDField()
    agree = models.BooleanField(default=False)

    # many = models.ManyToManyField(OtherModel)
    # foreignKey = models.ForeignKey(on_delete=models.CASCADE)
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )

    # binaryfield = models.BinaryField()
    # big_integer_field = models.BigIntegerField()
    # binary_field = models.BinaryField()
    # big_auto_field = models.BigAutoField(primary_key=True)

