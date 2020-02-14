# Generated by Django 3.0.3 on 2020-02-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damage', '0002_auto_20200208_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='ammo',
            field=models.CharField(choices=[('None', 'None'), ('Ammo5mm', '5mm'), ('Ammo556', '5.56mm'), ('Ammo308Caliber', '.308'), ('Ammo308Caliber_AntiScorchBeast', '.308 Ultracite'), ('Ammo38Caliber', '.38'), ('Ammo10mm', '10mm'), ('Ammo44', '.44'), ('Ammo45Caliber', '.45'), ('Ammo50Caliber', '.50'), ('Ammo50CaliberBall', '.50 ball'), ('AmmoShotgunShell', 'Shotgun Shell'), ('Ammo2mmEC', '2mm EC'), ('AmmoFusionCell', 'Fusion Cell'), ('AmmoFusionCore', 'Fusion Core'), ('AmmoGammaCell', 'Gamma Cell'), ('AmmoPlasmaCartridge', 'Plasma Cartridge'), ('AmmoPlasmaCore', 'Plasma Core'), ('AmmoCryoCell', 'Cryo Cell'), ('AmmoAlienBlaster', 'Alien Blaster'), ('AmmoCannonBall', 'Cannonball'), ('AmmoRRSpike', 'Railway Spike'), ('AmmoFlamerFuel', 'Flamer Fuel'), ('AmmoGrenadeLauncher', '40mm Grenade'), ('AmmoMissile', 'Missile'), ('AmmoFatManMiniNuke', 'Mini Nuke')], max_length=32),
        ),
    ]
