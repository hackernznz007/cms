# Generated by Django 3.2.5 on 2021-07-11 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_comment_action_ip'),
        ('core', '0017_auto_20210711_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footermenu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='footermenu',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.page', verbose_name='Page'),
        ),
        migrations.AlterField(
            model_name='footermenu',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.page', verbose_name='Page'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.page', verbose_name='Page'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.tag', verbose_name='Tag'),
        ),
    ]