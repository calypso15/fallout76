from django.db import models

class Weapon(models.Model):
	AUTOMATIC_PISTOL = 'automatic pistol'
	NON_AUTOMATIC_PISTOL = 'non-automatic pistol'
	SHOTGUN = 'shotgun'
	AUTOMATIC_RIFLE = 'automatic rifle'
	NON_AUTOMATIC_RIFLE = 'non-automatic rifle'
	NON_EXPLOSIVE_HEAVY_GUN = 'non-explosive heavy gun'
	EXPLOSIVE_HEAVY_GUN = 'explosive heavy gun'
	ONE_HANDED_MELEE = 'one-handed melee'
	TWO_HANDED_MELEE = 'two-handed melee'
	
	WEAPON_TYPES = (
		(AUTOMATIC_PISTOL, 'Automatic Pistol'),
		(NON_AUTOMATIC_PISTOL, 'Non-Automatic Pistol'),
		(SHOTGUN, 'Shotgun'),
		(AUTOMATIC_RIFLE, 'Automatic Rifle'),
		(NON_AUTOMATIC_RIFLE, 'Non-Automatic Rifle'),
		(NON_EXPLOSIVE_HEAVY_GUN, 'Non-Explosive Heavy Gun'),
		(EXPLOSIVE_HEAVY_GUN, 'Explosive Heavy Gun'),
		(ONE_HANDED_MELEE, 'One-Handed Melee'),
		(TWO_HANDED_MELEE, 'Two-Handed Melee'),
	)

	name = models.CharField(max_length=64)
	type = models.CharField(max_length=32, choices=WEAPON_TYPES)
	energy = models.BooleanField(default=False)
	strength_factor = models.DecimalField(max_digits=3, decimal_places=2)
	speed = models.DecimalField(max_digits=4, decimal_places=2)
	level = models.PositiveSmallIntegerField()
	damage = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return f"{self.name} (level {self.level})"