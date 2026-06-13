#!/usr/bin/env bash
# build.sh — runs once during Render's build phase

set -o errexit   # exit on any error

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser (safe to re-run — skips if already exists)
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='lexi').exists():
    User.objects.create_superuser('lexi', 'lexicorporation22@gmail.com', 'lexiworld1959')
    print('Superuser created.')
else:
    print('Superuser already exists — skipped.')
"
