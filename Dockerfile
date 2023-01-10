# Use the pyhton 3.10 images as basic image
FROM python:3.10

# Create app directory
WORKDIR /usr/src/app

# Copy the requirements file.
COPY requirements.txt ./

# Updatate pip
RUN pip install --upgrade pip

# Install the requiremnts
RUN pip install -r requirements.txt

# Copy all files of the application
COPY . .

# Init the database and create a superuser by the values from the .env file
RUN python manage.py makemigrations  \
    && python manage.py migrate \
    && python manage.py createsuperuser_by_env

# Set the port on that this app starts
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
