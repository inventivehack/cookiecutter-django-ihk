# -*- coding: utf-8 -*-

"""Removed unused files."""


import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_name):
    """Remove file."""
    if os.path.exists(file_name):
        os.remove(file_name)


if '{{ cookiecutter.use_travis }}'.lower() != 'y':
    remove_file(os.path.join(PROJECT_DIRECTORY, '.travis.yml'))
