import os
import random

verbs = []

with os.scandir("./data/") as entries:
    for entry in entries:
        if (entry.name.endswith('txt')):
            verbs.append(entry.name)

with open('./data/' + random.choice(verbs)) as f:
    message = "mystery verb\n\n".upper()
    message += f.read()
    p = os.popen('msmtp -t', 'w')
    dest_mail = "name@example.com"
    p.write(f"To:{dest_mail}\nSubject: {message}")
    p.close()
