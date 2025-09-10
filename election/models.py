from django.db import models

# Create your models here.

class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField(null=True, blank=True)
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    polling_unit_number = models.CharField(max_length=50, null=True, blank=True)
    polling_unit_name = models.CharField(max_length=200, null=True, blank=True)
    entered_by_user = models.CharField(max_length=50, null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "polling_unit"
        managed = False

    def __str__(self):
        return f"{self.polling_unit_name or 'PU'} (ID {self.uniqueid})"
      
class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.ForeignKey(
        PollingUnit,
        to_field="uniqueid",
        db_column="polling_unit_uniqueid",
        on_delete=models.CASCADE
    )
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "announced_pu_results"
        managed = False

    def __str__(self):
        return f"{self.party_abbreviation} - {self.party_score}"
      
class LGA(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=200)
    state_id = models.IntegerField()

    class Meta:
        db_table = "lga"
        managed = False

    def __str__(self):
        return self.lga_name
      
class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=200)
    lga_id = models.IntegerField()

    class Meta:
        db_table = "ward"
        managed = False

    def __str__(self):
        return self.ward_name
      
class Party(models.Model):
    id = models.AutoField(primary_key=True)
    partyid = models.CharField(max_length=50)
    partyname = models.CharField(max_length=200)

    class Meta:
        db_table = "party"
        managed = False

    def __str__(self):
        return self.partyid