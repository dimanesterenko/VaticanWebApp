from django.db import models

# Create your models here.
class Visitor(models.Model):
    Visitor_ID = models.AutoField(primary_key=True)
    Visitor_Name = models.CharField(max_length=50)
    Visitor_Mail = models.CharField(max_length=50)
    Visitor_Tel = models.CharField(max_length=10)
    Visitor_Card = models.CharField(max_length=16)

    def __str__(self):
        return self.Visitor_Name

class Responsible(models.Model):
    Responsible_ID = models.AutoField(primary_key=True)
    Responsible_Name = models.CharField(max_length=25)
    Responsible_Pos = models.CharField(max_length=50)
    Responsible_Tel = models.CharField(max_length=10)
    Responsible_Mail = models.CharField(max_length=50)

    def __str__(self):
        return self.Responsible_Name

class Guide(models.Model):
    Guide_ID = models.AutoField(primary_key=True)
    Guide_Name = models.CharField(max_length=50)
    Guide_Lang = models.CharField(max_length=50)
    Guide_Tel = models.CharField(max_length=10)
    Guide_Mail = models.CharField(max_length=50)

    def __str__(self):
        return self.Guide_Name

class Ticket(models.Model):
    Ticket_ID = models.AutoField(primary_key=True)
    Visitor_ID = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    Ticket_Guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    Ticket_Type = models.CharField(max_length=20)
    Ticket_Date = models.DateField()
    Ticket_Time = models.TimeField()
    Ticket_Count = models.IntegerField()
    Ticket_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Ticket_Status = models.CharField(max_length=15, default='booked')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.Ticket_Status = 'booked'
        super().save(*args, **kwargs)

    def calculate_price(self):
        if self.Ticket_Type == 'adult':
            self.Ticket_Price = 62 * self.Ticket_Count
        elif self.Ticket_Type == 'child':
            self.Ticket_Price = 52 * self.Ticket_Count
        elif self.Ticket_Type == 'baby':
            self.Ticket_Price = 5 * self.Ticket_Count
        super().save()
    def __str__(self):
        return f'Ticket-{self.Ticket_ID} for {self.Visitor_ID.Visitor_Name}'

class Booking(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    Visitor_ID = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    Responsible_ID = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    Guide_ID = models.ForeignKey(Guide, on_delete=models.CASCADE)
    Booking_Count = models.IntegerField()
    Booking_Date = models.DateField()
    Booking_Time = models.TimeField()

    def __str__(self):
        return f'Booking-{self.Booking_ID} for {self.Visitor_ID.Visitor_Name}'
