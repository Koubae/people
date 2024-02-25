"""
Use this script to create demo data for the database
"""
import json
from datetime import datetime

from faker import Faker
from faker.providers import date_time, address, job, phone_number


DEFAULT_PASSWORD = "xPwVOJ-L0vVY3ERaLKgWOg"  # use same for all demo, so to don't go crazy if we want to test with a user the pass is always the same
LOCALES_MUTLI = ["en_GB", "fr_FR", "it_IT", "de_DE", "es_ES", "ru_RU", "ja_JP", "zh_CN"]  # check how make Django work with multiple languages
LOCALES = ["en_GB", "fr_FR", "it_IT", "de_DE", "es_ES"]
PRETTY_PRINT = True

fake = Faker(LOCALES)

fake_with_providers = Faker()
fake_with_providers.add_provider(date_time)
fake_with_providers.add_provider(address)
fake_with_providers.add_provider(job)
fake_with_providers.add_provider(phone_number)

def format_datetime(date_time: datetime) -> str:
	return date_time.strftime("%Y-%m-%d %H:%M:%S")

def create_accounts(total_users):
	print(f"Total users: {total_users}")
	print("Creating demo data...")
	users_data = {}
	for count in range(total_users):
		username = fake.user_name()

		account = {
			"birthday": format_datetime(fake_with_providers.date_of_birth()),
			"country": fake_with_providers.country(),
			"city": fake_with_providers.city(),
			"address": fake_with_providers.address(),
			"job": fake_with_providers.job(),
			"phone": fake_with_providers.phone_number(),
		}

		users_data[username] = {
			"username": username,
			"first_name": fake.first_name(),
			"last_name": fake.last_name(),
			"email": fake.email(),
			"password": DEFAULT_PASSWORD,
			"is_superuser": 0,
			"is_staff": 0,
			"is_active": 1,
			"date_joined": format_datetime(fake_with_providers.date_time_this_decade()),
			"account": account
		}
	if PRETTY_PRINT:
		print(json.dumps(users_data, indent=4))
	else:
		print(users_data)
	print("-"*200)

create_accounts(10)
