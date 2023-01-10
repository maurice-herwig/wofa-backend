from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
import constants


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Overwrite the handle method. This command parse the values from the .env file and create a new superuser.
        """

        try:
            # Parse the environment variables
            su_username = os.environ.get(constants.SU_USERNAME)
            su_email = os.environ.get(constants.SU_EMAIL, '')
            su_password = os.environ.get(constants.SU_PASSWORD)

            # Create a new superuser
            super_user = User.objects.create_superuser(
                username=su_username,
                email=su_email,
                password=su_password
            )

            # Save the new superuser in the database
            super_user.save()

            # Write a message to the console.
            self.stdout.write('The superuser is created successfully', ending='')

        except Exception as e:
            # Write an error message on the console
            self.stderr.write(str(e), ending='')

