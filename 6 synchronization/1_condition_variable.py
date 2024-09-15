#!/usr/bin/env python3
""" Two hungry people, anxiously waiting for their turn to take soup """

import threading

N_THREADS = 5
slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)

def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid:
            # compares id number with the amount of soups_servings remaining
            while (person_id != (soup_servings % N_THREADS)) and (soup_servings > 0): # check if it's your turn
                print(f'Person {person_id} checked... then put the lid back.')
                soup_taken.wait()
            if soup_servings > 0:
                soup_servings -= 1 # it's your turn; take some soup!
                print(f'Person {person_id} took soup! Servings left: {soup_servings}')
                soup_taken.notify_all()

if __name__ == '__main__':
    for person in range(N_THREADS):
        threading.Thread(target=hungry_person, args=(person,)).start()
