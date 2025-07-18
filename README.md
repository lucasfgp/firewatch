Steps to make the application run

cd /path_to_the_file

python3.9 -m venv firewatchenv

source firewatchenv/bin/activate

workon firewatchenv

cd firewatch

pip install -r requirements.txt

python scripts/populate_firewatch.py

python manage.py makemigrations

python manage.py migrate

python manage.py runserver