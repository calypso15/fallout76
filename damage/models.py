from django.db import models

class Weapon(models.Model):
	TYPE_PISTOL = 'pistol'
	TYPE_SHOTGUN = 'shotgun'
	TYPE_RIFLE = 'rifle'
	TYPE_HEAVY = 'heavy gun'
	TYPE_MELEE = 'melee'
	TYPE_THROWN = 'thrown'
	
	WEAPON_TYPES = (
		(TYPE_PISTOL, 'Pistol'),
		(TYPE_SHOTGUN, 'Shotgun'),
		(TYPE_RIFLE, 'Rifle'),
		(TYPE_HEAVY, 'Heavy Gun'),
		(TYPE_MELEE, 'Melee'),
		(TYPE_THROWN, 'Thrown'),
	)
	
	AMMO_NONE = 'none'
	AMMO_308 = '.308'
	AMMO_38 = '.38'
	AMMO_44 = '.44'
	AMMO_45 = '.45'
	AMMO_50BALL = '.50 ball'
	AMMO_50 = '.50'
	AMMO_10MM = '10mm'
	AMMO_556 = '5.56mm'
	AMMO_5MM = '5mm'
	AMMO_CANNONBALL = 'cannonball'
	AMMO_SPIKE = 'railway spike'
	AMMO_SHELL = 'shotgun shell'
	AMMO_2MMEC = '2mm ec'
	AMMO_ALIEN = 'alien blaster'
	AMMO_CRYO = 'cryo cell'
	AMMO_FUEL = 'fuel'
	AMMO_FUSIONCELL = 'fusion cell'
	AMMO_FUSIONCORE = 'fusion core'
	AMMO_GAMMA = 'gamma'
	AMMO_PLASMA = 'plasma cartridge'
	AMMO_PLASMACORE = 'plasma core'
	AMMO_40MMGRENADE = '40mm grenade'
	AMMO_MININUKE = 'mini nuke'
	AMMO_MISSILE = 'missile'
	
	AMMO_TYPES = (
		(AMMO_NONE, 'None'),
		(AMMO_308, '.308'),
		(AMMO_38, '.38'),
		(AMMO_44, '.44'),
		(AMMO_45, '.45'),
		(AMMO_50BALL, '.50 ball'),
		(AMMO_50, '.50'),
		(AMMO_10MM, '10mm'),
		(AMMO_556, '5.56mm'),
		(AMMO_5MM, '5mm'),
		(AMMO_CANNONBALL, 'Cannonball'),
		(AMMO_SPIKE, 'Railway Spike'),
		(AMMO_SHELL, 'Shotgun Shell'),
		(AMMO_2MMEC, '2mm EC'),
		(AMMO_ALIEN, 'Alien Blaster'),
		(AMMO_CRYO, 'Cryo Cell'),
		(AMMO_FUEL, 'Fuel'),
		(AMMO_FUSIONCELL, 'Fusion Cell'),
		(AMMO_FUSIONCORE, 'Fusion Core'),
		(AMMO_GAMMA, 'Gamma'),
		(AMMO_PLASMA, 'Plasma Cartridge'),
		(AMMO_PLASMACORE, 'Plasma Core'),
		(AMMO_40MMGRENADE, '40mm Grenade'),
		(AMMO_MININUKE, 'Mini Nuke'),
		(AMMO_MISSILE, 'Missile'),
	)

	name = models.CharField(max_length=64)
	type = models.CharField(max_length=32, choices=WEAPON_TYPES)
	level = models.PositiveSmallIntegerField()
	damage = models.PositiveSmallIntegerField()
	ammo = models.CharField(max_length=32, choices=AMMO_TYPES)
	automatic = models.BooleanField(default=False)
	explosive = models.BooleanField(default=False)
	speed = models.DecimalField(max_digits=4, decimal_places=2)
	strength_factor = models.DecimalField(max_digits=3, decimal_places=2)

	def __str__(self):
		return f"{self.name} (level {self.level})"