from django.db import models

SUCCESSION_CHOICES = (
	('N/A', 'not applicable'),
	('7', 're-seed every 7 days'),
	('14', 're-seed every 14 days'),
	('21', 're-seed every 21 days'),
	('30', 're-seed every 30 days')
)

class Plant(models.Model):

	kind = models.CharField(max_length=30)
	variety = models.CharField(max_length=50)
	seed_depth = models.IntegerField()
	seed_spacing = models.IntegerField()
	germination = models.IntegerField()
	plant_spacing = models.IntegerField()
	row_spacing = models.IntegerField()
	days_to_harvest = models.IntegerField()
	sunlight = models.IntegerField()
	indoor_start = models.DateField()
	indoor_stop = models.DateField()
	transplant_start = models.DateField()
	transplant_stop = models.DateField()
	outdoor_start = models.DateField()
	outdoor_stop = models.DateField()
	succession = models.CharField(max_length=50, choices = SUCCESSION_CHOICES)
	notes = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.kind

	class Meta:
		ordering = ['kind']

	# user = models.ForeignKey(User, on_delete=models.CASCADE)
		
