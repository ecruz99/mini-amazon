from werkzeug.security import generate_password_hash
import csv
from faker import Faker

num_users = 1000
num_products = 2000
num_purchases = 2500
num_inventory = 2000

Faker.seed(0)
fake = Faker()


def get_csv_writer(f):
    return csv.writer(f, dialect='unix')


def gen_users(num_users):
    with open('Users.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Users...', end=' ', flush=True)
        for uid in range(num_users):
            if uid % 10 == 0:
                print(f'{uid}', end=' ', flush=True)
            profile = fake.profile()
            email = fake.unique.email()
            plain_password = f'pass{uid}'
            password = generate_password_hash(plain_password)
            name_components = profile['name'].split(' ')
            firstname = name_components[0]
            lastname = name_components[-1]
            address = profile['address']
            balance = 0
            writer.writerow([uid, email, password, firstname, lastname, address, balance])
        print(f'{num_users} generated')
    return


def gen_products(num_products):
    available_pids = []
    with open('Products.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Products...', end=' ', flush=True)
        for pid in range(num_products):
            if pid % 100 == 0:
                print(f'{pid}', end=' ', flush=True)
            name = fake.sentence(nb_words=4)[:-1]
            price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            available = fake.random_element(elements=('true', 'false'))
            if available == 'true':
                available_pids.append(pid)
            writer.writerow([pid, name, price, available])
        print(f'{num_products} generated; {len(available_pids)} available')
    return available_pids


def gen_purchases(num_purchases, available_pids):
    with open('Purchases.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Purchases...', end=' ', flush=True)
        for id in range(num_purchases):
            if id % 100 == 0:
                print(f'{id}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_element(elements=available_pids)
            time_purchased = fake.date_time()
            writer.writerow([id, uid, pid, time_purchased])
        print(f'{num_purchases} generated')
    return

def gen_inventory(num_inventory):
    tuples = []
    with open('Inventory.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Inventory...', end = ' ', flush=True)
        for sellerID in range(num_inventory):
            if sellerID % 100 == 0:
                print(f'{sellerID}', end = ' ', flush=True)
            while True:
                a = fake.pyint(min_value = 0, max_value = 500)
                b = fake.pyint(min_value = 0, max_value = 2000)
                if (a,b) not in tuples:
                    tuples.append((a,b))
                    break
                else:
                    continue
            sellerID = a
            productID = b
            productname = fake.sentence(nb_words=4)[:-1]
            quantity = fake.pyint(min_value = 0, max_value = 200)
            writer.writerow([sellerID, productID, productname, quantity])
        print(f'{num_inventory} generated')
    return

def gen_carts(num_carts):
    with open('Carts.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Carts...', end=' ', flush = True)
        for cart in range(num_carts):
            if cart % 100 == 0:
                print(f'{cart}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_int(min=0, max=num_products-1)
            sid = fake.random_int(min=0, max=1999)
            productname = fake.sentence(nb_words=4)[:-1]
            quantity = fake.random_int(min=1, max=10)
            unit_price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            writer.writerow([uid, pid, sid, productname, quantity, unit_price])
        print(f'{num_carts} generated')
    return

def gen_review(num_review):
    with open('P_Reviews.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Review...', end=' ', flush = True)
        for review in range(num_review):
            if review % 100 == 0:
                print(f'{review}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            sid = fake.random_int(min=0, max=num_products-1)
            rating = fake.random_int(min=1, max=5)
            time_purchased = fake.date_time()
            writer.writerow([uid, sid, rating, time_purchased])
        print(f'{num_review} generated')
    return

#gen_carts(num_carts)            
#gen_inventory(num_inventory)
#gen_users(num_users)
# available_pids = gen_products(num_products)
# gen_purchases(num_purchases, available_pids)


