import string
import random


class Testdata:
    usernumber = "6666777711"
    OTP_1 = "1"
    OTP_2 = "1"
    OTP_3 = "1"
    OTP_4 = "1"
    OTP_5 = "1"
    OTP_6 = "1"

    package_name = "com.digitalgreen.org.d2fo"
    database_name = "d2fo_loop_digital_green_db"

    Major_crop_1 = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

    Major_crop_2 = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    First_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Second_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

    Product_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    Product_variety = ''.join(random.choice(string.ascii_lowercase) for i in range(4))

    # Generate a number between 16 and 99 (inclusive)
    number = random.randint(16, 99)

    # Convert the number to a string
    Age = str(number)
    print("Number", Age)

    # Age = ''.join(random.choice(string.digits) for i in range(2))
    No_OF_SHARES = ''.join(random.choice(string.digits) for i in range(6))

    Aadhar_number = ''.join(random.choice(string.digits) for i in range(12))

    Mobile_number = ''.join(random.choice(string.digits) for i in range(10))

    LANDHOLDING = ''.join(random.choice(string.digits) for i in range(3))

    IRRIGATED_LAND = ''.join(random.choice(string.digits) for i in range(3))

    RAINFED_LAND = ''.join(random.choice(string.digits) for i in range(3))

    NO_OF_COWS = ''.join(random.choice(string.digits) for i in range(4))

    NO_OF_GOATS = ''.join(random.choice(string.digits) for i in range(5))

    NO_OF_CHICKS = ''.join(random.choice(string.digits) for i in range(6))

    Procurement_Qunatity = ''.join(random.choice(string.digits) for i in range(3))

    Stock = ''.join(random.choice(string.digits) for i in range(2))

    MRP = "1000"

    Shareholder_Price = "800"

    Non_Shareholder_Price = "900"


    # Generate a random number that starts with 03, 07, or 09
    prefix = random.choice(['03', '07', '09'])
    # Append 8 more random digits to make a total length of 10 digits
    random_number_with_prefix = prefix + ''.join(random.choice(string.digits) for i in range(8))

    FIELD_SIZE_LAND = ''.join(random.choice(string.digits) for i in range(2))

    FIELD_SIZE_LIVESTOCK = ''.join(random.choice(string.digits) for i in range(2))

    LIVESTOCK_NUMBER = ''.join(random.choice(string.digits) for i in range(2))