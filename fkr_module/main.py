from faker import Faker

fake = Faker('ru_RU')


for i in range(2):
    print(fake.first_name(), fake.name())
    # print(fake.address())
    # print(fake.password(4))
    # print(fake.phone_number())
    # print(fake.job())
    # print(fake.isbn13())
    print(fake.company())
