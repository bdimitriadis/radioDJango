# radioDjango
The frontend of radioDjango web application (e-radio) project, implemented using Django framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install on your system

```
* Python 3.x.x
* The required packages found in requirements.txt file via pip installer. 
  The file requirements.txt, contains the minimum versions of the required packages 
  that have been tested and working. The packages' versions could probably be omitted
  so that the latest packages are installed.
```

## Deployment

Adjust settings in the settings.py file to your own database settings, or export the necessary variables ('SECRET_KEY', 'DEBUG', 'DATABASE_URL'), that settings.py file utilizes, to your local (virtual) environment.

* Just run the command python manage.py runserver in the local directory with python3 on your local machine **for development and testing purposes**.
* To deploy the project **on a live system**, follow the instruction given by the official documentation of Django: https://docs.djangoproject.com/en/4.0/howto/deployment/ 

## Built With

* [Python 3.5.2](https://www.python.org/) - Developing with the best programming language
* [Django 2.0.1](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.

## Authors

* **Blasis Dimitriadis** - *Initial work* - [radioDango](https://github.com/bdimitriadis/radioDjango)


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
