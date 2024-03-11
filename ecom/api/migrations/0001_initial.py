from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="ecom",
                          email="madhumk0709m@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="7483417996",
                          gender="Male"
                          )
        user.set_password("ecom")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
