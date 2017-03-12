export ZSH=~/.oh-my-zsh
ZSH_THEME="bira"
plugins=(git, python, django)
source $ZSH/oh-my-zsh.sh

PROJECT_PATH=/app

ENV_FILE=$PROJECT_PATH/.env
source $ENV_FILE

export DJANGO_SETTINGS_MODULE="config.settings.dev"

# Run Django project
run() {
    cd $PROJECT_PATH
    python3 manage.py runserver 0.0.0.0:8000
}

# Reset Database
reset_db() {
    sudo -u postgres psql -c "DROP DATABASE $DATABASE_NAME;"
    sudo -u postgres psql -c "CREATE DATABASE $DATABASE_NAME;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DATABASE_NAME TO $DATABASE_USER;"

    cd $PROJECT_PATH
    python3 manage.py migrate

}

save_to_fixture() {
    echo "Dump name (slug): "
    read fixture_name

    extension=".json"
    file_name=$fixture_name$extension

    cd $PROJECT_PATH
    python3 manage.py dumpdata | python3 -m json.tool > {{ cookiecutter.project_slug }}/fixtures/$file_name

}

update_db() {
    cd $PROJECT_PATH
    python3 manage.py migrate
}

rewrite_migrations() {
    echo "This command will delete all current migration files and rewrite them into a new ones based on your models.py"
    read -r -p "Are you sure? [Y/n]: " REPLY
    echo

    if [[ ! $REPLY =~ ^[Yy]$ ]]
        cd $PROJECT_PATH
        rm {{ cookiecutter.project_slug }}/*/migrations/0*
        python3 manage.py makemigrations

        echo
        echo "Run update_db to apply migrations"
    then
        exit 1
    fi
}

test_app() {
    cd $PROJECT_PATH

    flake8
    pep257
    python3 manage.py test

}
