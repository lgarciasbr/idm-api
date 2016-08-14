import random
from faker import Faker

fake = Faker()


def generate_random_email():
    domains = ["hotmail.com", "gmail.com", "icloud.com", "yahoo.com"]

    name = fake.name().lower().replace(" ", ".")
    domain = random.choice(domains)

    return name + '@' + domain
