import sys
sys.path.append(r"C:\Users\shire\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages")

from faker import Faker

fake = Faker()
print(fake.name())
print(fake.address()) 
print(fake.email())


def add(nb):
    users = []
    for i in range(nb):
        user = {"name" : fake.name(),
                "address" : fake.address(), 
                "language_code" : fake.language_code()}   
        users.append(user)
    for u in users:
        print(f"{u} \n")

nb = int(input("How many users do you want to generate ? :"))
add(nb)