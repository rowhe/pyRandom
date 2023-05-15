from faker import Faker

fake = Faker('ru_RU')


for i in range(2000000000000):
    # print(fake.name())
    # print(fake.address())
    # print(fake.password(4))
    # print(fake.phone_number())
    # print(fake.job())
    # print(fake.isbn13())
    print(fake.company())