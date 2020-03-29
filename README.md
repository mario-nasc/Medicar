# Medicar
Medicar is an appointment scheduling system, the system allows the user to:
- Create a user
- Log in to the system
- Make a new appointment with pre-defined filters.
- View scheduled appointments
- Deselect an appointment

In addition, there is a medicar administrator system where it is possible to create doctors, specialties and schedules to provide the data to be used in the previous functionalities.es e agendas para provêr os dados a serem utilizados nas funcionalidades anteriores.

## Requirements

```
Docker: https://docs.docker.com/install/
Docker compose: https://docs.docker.com/compose/install/ 
Node && npm: https://nodejs.org/en/
```

## Setup

### 1. Clone the repository
```$ git clone https://github.com/Mario0606/Medicar.git```

### 2. Project Setup
The backend is added to the docker structure, buter the addition of the frontend is Work in progress.

- Backend
Depending on the user, you may need to run dockers commands along with sudo.

```
$ cd <project_path>
$ docker-compose up --build
in some cases, the web container tries to connect to the db container prematurely and from exit 0, running the command above again, the problem is solved and migrates are performed
```

- Frontend
```
$ cd <project_path>/MedicarFrontend
$ npm install
$ npm start
```

### 3. Access Medicar Admin

Creating a superuser to access the administration system

```
$ docker-compose exec web python3 medicar_backend/manage.py createsuperuser
```

access localhost:8000

### 4. Access Frontend

access localhost:4200

### TO DO
- Add angular to docker
- Create some tests
- Create a new user type inheriting from the django auth user to provide new attributes such as Full Name.
- Improve the front.
