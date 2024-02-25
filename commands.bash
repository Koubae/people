# -----------------------
# Database
# -----------------------
python manage.py makemigrations
python manage.py migrate

# squash migration <-- to check , should put all migration into a file

# Manually delete migrations
delete from django_migrations where app = 'account';

# -----------------------
# Testings
# -----------------------
# Keep database after test
python manage.py test --keepdb
# Not ask to destroy/reuse database
python manage.py test --noinput