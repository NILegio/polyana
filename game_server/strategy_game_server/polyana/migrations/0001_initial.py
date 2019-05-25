# Generated by Django 2.2.1 on 2019-05-23 20:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('token', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
                ('played_battles', models.IntegerField(default=0)),
                ('battles_won', models.IntegerField(default=0)),
                ('winrate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('registration', 'registration'), ('battle_start', 'battle_start'), ('battle_end', 'battle_end'), ('money_buying', 'money_buying'), ('achievement', 'achievement'), ('login', 'login'), ('logout', 'logout')], db_column='type', max_length=200)),
                ('source', models.IntegerField(null=True)),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polyana.Player')),
            ],
        ),
    ]