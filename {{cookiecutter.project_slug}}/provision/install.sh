#!/bin/bash

# Update OS packages
apt-get update -y
apt-get upgrade -y

# Install Ansible
apt-get install -y software-properties-common
apt-add-repository -y ppa:ansible/ansible
apt-get -y update
apt-get install -y ansible

# Install Python3
apt-get install python3 -y
