import os
from anonymate.anonymizer import Anonymizer
from cryptography.fernet import Fernet

# Profiles listed in the assignment
profiles = [
# Profile 1
    {
    'name': 'Oscar Newman',
    'DoB': '1927,1,19',
    'sex': 'M',
    'blood_group': 'B+'
    },
# Profile 2
    {
        'name': 'Jeremy Wilson',
        'DoB': '1996,10,12',
        'sex': 'M',
        'blood_group': 'A-'
    },
# Profile 3
    {
        'name': 'Kenneth Rhodes',
        'DoB': '2003,6,15',
        'sex': 'M',
        'blood_group': 'A-',
    },
# Profile 4

    {
        'name': 'Nicole Richardson',
        'DoB': '2003,9,7',
        'sex': 'F',
        'blood_group': 'AB+'
    },
# Profile 5
    {
        'name': 'Gary Gamble',
        'DoB': '1968,8,19',
        'sex': 'M',
        'blood_group': 'A+'
    }
]

# encryption key
key_file = 'secret.key'
if os.path.exists(key_file):
    with open(key_file, "rb") as f:
        encryption_key = f.read()
else:
    encryption_key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(encryption_key)

anonymizer = Anonymizer(encryption_key=encryption_key)


# Create a loop
i=1
for profile in profiles:
    print(f"{i}: {profile['name']}")
    i += 1

# Choose profile out of the 5
choice = int(input("Enter your choice: "))

selection = profiles[choice - 1]

category = input("Enter your category (name, DoB, sex, blood_group): ")


print("Result: ", selection[category])

encrypt_choice = input('Do you want to encrypt your choice (y/n): ').strip().lower()
if encrypt_choice == 'y':
    data_str = str(selection[category])
    encrypted_data = anonymizer.encrypt(data_str)
    print('Encrypted Data: ', encrypted_data)

save_choice = input(
    'Do you want to save your encrypted data (y/n): '
    ).strip().lower()
if save_choice == 'y':
    filename = input("Enter your filename: ")
    with open(filename, "w") as f:
        f.write(str(encrypted_data))
    print(f'saved to {filename}')






