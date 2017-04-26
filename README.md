# Inventive's Django Cookiecutter

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter) and inspired by
[Pydanny's cookiecutter](https://github.com/pydanny/cookiecutter-django) and with the
goal of optimize our development processes, we are happy to introduce our Django projects boilerplate packed and ready to use with the following features:

* **Django** 1.11 LTS
* **Ansible** provisioning for production, testing and development environments
* **Travis CI** for continuous integration
* **AWS CodeDeploy** for continuous delivery
* [**12 Factor**](https://12factor.net/) based settings
* **SSL** automatic certificate installation
* **Whitenoise** for static files optimization and distribution.
* **Systemd** daemon for production environment
* **NGINX** setup for production environment
* **PostgreSQL** as database engine
* Preloaded with **ZSH profile** and **development scripts**.

## Installation

1. Install [cookiecutter](https://github.com/audreyr/cookiecutter) by running this
command (*NIX systems only*):

```
$ pip install cookiecutter
```

2. Run against this repo

```
$ cookiecutter https://github.com/inventivehack/cookiecutter-django-ihk
```

## Getting Started

### Prerequisites

In order to run the project you need to first install:

* [Vagrant](https://vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

### Running the project

1. Create a copy of `.env.sample` and change its content.
2. Run `$ vagrant up --provision` to start the virtual machine.
3. Run `$ vagrant ssh` to connect to the machine via SSH.
4. Run `$ run` to start the development server
5. Go to the application port (8888 by default) [http://localhost:8888/](http://localhost:8888/).

### Deployment

If you selected **use_aws_codedeploy** during setup, all you need to do is create an
application, create a deployment group, and release a new revision.

All deployments require a `.env` file as well as the `.key` and `.crt` files from the
SSL certificate inside `/app/ansible/nginx/files/ssl` in order to succeed.

## Not Exactly What You Want

This is what we use to optimize projects setup, it might not be what you want but don't worry, you have [options](http://cookiecutter.readthedocs.io/en/latest/readme.html#python-django)

## Contributing

Please fill free to submit pull requests as well as open issues.

### Contributors

* [Oscar Roa](https://github.com/OscaRoa)
* [Pablo Trinidad](https://github.com/pablotrinidad)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
