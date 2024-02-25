# -----------------------
# Apps
# -----------------------
# Creating apps in a suborder called 'apps'
mkdir apps/<app_name>
python manage.py startapp <app_name> ./apps/<app_name>

# -----------------------
# Database
# -----------------------
python manage.py makemigrations
python manage.py migrate

# squash migration <-- to check , should put all migration into a file

# Manually delete migrations
delete from django_migrations where app = 'account';

python manage.py sqlmigrate   <app_name>
python manage.py makemigrations --empty <app_name>

python manage.py migrate  --fake address 0002_populate

# -----------------------
# Testings
# -----------------------
# Keep database after test
python manage.py test --keepdb
# Not ask to destroy/reuse database
python manage.py test --noinput


drop table address_address;
drop table address_city;
drop table address_country;
drop table address_subregion;
drop table address_continent;
delete from django_migrations where app = 'address';


python manage.py makemigrations address
python manage.py migrate   address 0001_initial

python manage.py sqlmigrate address 0002_populate
python manage.py migrate address 0002_populate

python manage.py migrate account 0002_populate

delete from django_migrations where app = 'account' ;
