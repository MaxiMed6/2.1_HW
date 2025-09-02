import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

inner_randominfo_path = os.path.join(current_dir, 'randominfo', 'randominfo-master', 'randominfo')
parent_of_inner = os.path.dirname(inner_randominfo_path)
sys.path.insert(0, parent_of_inner)

import randominfo
person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)




