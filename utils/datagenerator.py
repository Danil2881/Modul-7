import string
import random
import time
import uuid
from datetime import datetime

from faker import Faker
faker = Faker()

class DataGenerator:
    _counter = 0

    @staticmethod
    def generate_email():
        DataGenerator._counter += 1
        timestamp = int(time.time() * 1000)  # миллисекунды
        random_suffix = random.randint(1000, 9999)
        unique_id = uuid.uuid4().hex[:1]  # 1 случайных hex символов

        return f"user.{unique_id}.{timestamp}{DataGenerator._counter}@test.com"

    @staticmethod
    def generate_name():
        return f"{faker.first_name()} {faker.last_name()}"

    @staticmethod
    def generate_random_password():
        letters = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)
        # Дополняем пароль случайными символами из допустимого набора
        special_chars = "?@#$%^&*|:"
        all_chars = string.ascii_letters + string.digits + special_chars
        remaining_length = random.randint(6,18)
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        #Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return ''.join(password)
