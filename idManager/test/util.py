import random
from faker import Faker

fake = Faker()


def generate_random_email():
    domains = ["hotmail.com", "gmail.com", "icloud.com", "yahoo.com"]

    # pre_name removes 'dr. xyz wkz' problem
    pre_name = fake.name().lower().replace(".", "")
    name = pre_name.replace(" ", ".")
    domain = random.choice(domains)

    return name + '@' + domain
