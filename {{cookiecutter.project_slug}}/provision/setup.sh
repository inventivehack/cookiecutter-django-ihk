#!/bin/bash

echo "Setting up users and groups"
getent group {{ cookiecutter.vagrant_group }} || groupadd {{ cookiecutter.vagrant_group }}
id -u {{ cookiecutter.vagrant_user }} || useradd -r -g {{ cookiecutter.vagrant_group }} {{ cookiecutter.vagrant_user }}

chown -R {{ cookiecutter.vagrant_user }} /app

cd /app/ansible

echo "Running ansible playbook"
ansible-playbook app.yml --extra-vars "$(cat ../.env)"

echo "Handling services"
test "$(hostname)" != '{{ cookiecutter.project_slug }}-dev' && (service {{ cookiecutter.project_slug }} restart)
test "$(hostname)" != '{{ cookiecutter.project_slug }}-dev' && (service nginx restart)
