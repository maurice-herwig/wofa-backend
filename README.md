# WoFaBackend

TODO Beschreiben

# Getting started

You can start the WoFaBackend as a dockerfile container or as python application. In both cases you need at first 
an RSA key for the encryption.

## RSA
You can generate an RSA key on this website:

https://travistidwell.com/jsencrypt/demo/

- Create the files rsa_pri.key and rsa_pub.key at the same path as manage.py and put the key content in the files. 
- Create .env file and locate it on same path as manage.py. Add the key “OIDC_RSA_PRIVATE_KEY” and put the content of the private key in there.
    ````
    OIDC_RSA_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    -----END RSA PRIVATE KEY-----"
    ````
  
## DOCKER 

The easy way is to start this application with [Docker](https://www.docker.com/). 
Add on the .env file the username and password of the superuser and additionally his email. For this you can use this template:
    ````
    SU_USERNAME=" "
    SU_PASSWORD=" "
    SU_EMAIL = " "
    ````

Then you can with docker compose build and start the WoFaBackend with the following command.

```bash
Docker compose up -d
```

The server runs now on the local machine on port 8000. 


## Python

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements for this package.

```bash
pip install -r requirements.txt 
```
  
#### DB
As next, we need a database, for this we run the next two commands. The first is for setup and the second for create.

```bash
python manage.py makemigrations
python manage.py migrate
```

Now we need a superuser/admin, to do this run the following command and fill in the dialog. 

```bash
python manage.py createsuperuser
```

#### Start 

Now we can start the server, typically on port 8000. 

```bash
python manage.py runserver 8000 
```

The server runs in development mode at http://127.0.0.1:8000/ by the way, it is normal that you get an 404 error on this URL.  


# Register an Application
Now we can register an application. Now we show the registration process for the test client application, for other applications the process is the same. 

- Visit the site http://127.0.0.1:8000/admin/
- add a new application and fill in the dialog as follows
![](./assets/register_application.jpg)
- Store the values for client_id and client_secret local. 

# Usage
#### Authorization
The first thing that you need to get access to this backend is to authorities. For this send a POST request
to the endpoint ```<base_url>:<port>/o/token ``` with the body values ```{"grant_type": ""client_credentials",
"client_id": <client_id>, "client_secret": <client_secret>}.``` 
Here is an example for this request:

```
curl -L -X POST 'http://127.0.0.1:8080/o/token/' \
-F 'client_id="rXdjzo2VUOUMUgjz1csBoxvhVXpgqMVg1rphQryl"' \
-F 'client_secret="CnVcZ4qgIgXD73l9wMpxt3lqVGBcvE1qaKqi52weJHOxoCupxD7f8SLkc6ehgWADanAp0wmIm323vX3nvUfErZgrRDS0GsQ8eS2UIQZeJoHhYtTNrmKUlnR1BWyh2hHp"' \
-F 'grant_type="client_credentials"'
```

After that you receive an access token as response with this you have access to all endpoints of this backend.



- TODO: beispiel für einen Endpunkt zeigen.

# TODOs
- Auch die Eingabe von regulären Ausdrücken ermöglichen
