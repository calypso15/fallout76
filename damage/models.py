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
	
	AMMO_NONE = 'None'
	AMMO_5MM = 'Ammo5mm'
	AMMO_556 = 'Ammo556'
	AMMO_308 = 'Ammo308Caliber'
	AMMO_308ULTRACITE = 'Ammo308Caliber_AntiScorchBeast'
	AMMO_38 = 'Ammo38Caliber'
	AMMO_10MM = 'Ammo10mm'
	AMMO_44 = 'Ammo44'
	AMMO_45 = 'Ammo45Caliber'
	AMMO_50 = 'Ammo50Caliber'
	AMMO_50BALL = 'Ammo50CaliberBall'
	AMMO_SHOTGUNSHELL = 'AmmoShotgunShell'
	AMMO_2MMEC = 'Ammo2mmEC'
	AMMO_FUSIONCELL = 'AmmoFusionCell'
	AMMO_FUSIONCORE = 'AmmoFusionCore'
	AMMO_GAMMACELL = 'AmmoGammaCell'
	AMMO_PLASMACARTRIDGE = 'AmmoPlasmaCartridge'
	AMMO_PLASMACORE = 'AmmoPlasmaCore'
	AMMO_CRYOCELL = 'AmmoCryoCell'
	AMMO_ALIENBLASTER = 'AmmoAlienBlaster'
	AMMO_CANNONBALL = 'AmmoCannonBall'
	AMMO_RRSPIKE = 'AmmoRRSpike'
	AMMO_FLAMERFUEL = 'AmmoFlamerFuel'
	AMMO_40MMGRENADE = 'AmmoGrenadeLauncher'
	AMMO_MISSILE = 'AmmoMissile'
	AMMO_MININUKE = 'AmmoFatManMiniNuke'
	
	AMMO_TYPES = (
		(AMMO_NONE, 'None'),
		(AMMO_5MM, '5mm'),
		(AMMO_556, '5.56mm'),
		(AMMO_308, '.308'),
		(AMMO_308ULTRACITE, '.308 Ultracite'),
		(AMMO_38, '.38'),
		(AMMO_10MM, '10mm'),
		(AMMO_44, '.44'),
		(AMMO_45, '.45'),
		(AMMO_50, '.50'),
		(AMMO_50BALL, '.50 ball'),
		(AMMO_SHOTGUNSHELL, 'Shotgun Shell'),
		(AMMO_2MMEC, '2mm EC'),
		(AMMO_FUSIONCELL, 'Fusion Cell'),
		(AMMO_FUSIONCORE, 'Fusion Core'),
		(AMMO_GAMMACELL, 'Gamma Cell'),
		(AMMO_PLASMACARTRIDGE, 'Plasma Cartridge'),
		(AMMO_PLASMACORE, 'Plasma Core'),
		(AMMO_CRYOCELL, 'Cryo Cell'),
		(AMMO_ALIENBLASTER, 'Alien Blaster'),
		(AMMO_CANNONBALL, 'Cannonball'),
		(AMMO_RRSPIKE, 'Railway Spike'),
		(AMMO_FLAMERFUEL, 'Flamer Fuel'),
		(AMMO_40MMGRENADE, '40mm Grenade'),
		(AMMO_MISSILE, 'Missile'),
		(AMMO_MININUKE, 'Mini Nuke'),
	)

	name = models.CharField(max_length=64)
	type = models.CharField(max_length=32, choices=WEAPON_TYPES)
	level = models.PositiveSmallIntegerField()
	damage = models.PositiveSmallIntegerField()
	ammo = models.CharField(max_length=32, choices=AMMO_TYPES)
	automatic = models.BooleanField(default=False)
	explosive = models.BooleanField(default=False)
	speed = models.DecimalField(max_digits=4, decimal_places=2)
	range = models.DecimalField(max_digits=5, decimal_places=2)
	strength_factor = models.DecimalField(max_digits=3, decimal_places=2)
	accuracy = models.DecimalField(max_digits=4, decimal_places=2)
	weight = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} (level {self.level})"