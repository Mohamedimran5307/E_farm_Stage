import string
import random


class Testdata:
    username = "aiyappa@gmail.com"
    password = "56001955"

    package_name = "com.digitalgreen.org.d2fo"
    database_name = "d2fo_loop_digital_green_db"

    Dev_group_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Farmer_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Father_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Grandfather_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Age = ''.join(random.choice(string.digits) for i in range(2))

    FIRST_FOUR = ''.join(random.choice(string.digits) for i in range(4))

    SECOND_FOUR = ''.join(random.choice(string.digits) for i in range(4))

    THIRD_FOUR =  ''.join(random.choice(string.digits) for i in range(4))