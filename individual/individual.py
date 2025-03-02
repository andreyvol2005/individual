import random

def generate_random_list(num_elements):
    random_list = [random.randint(5, 6 * 100) for i in range(num_elements)]
    return random_list
 
random_list = generate_random_list(16)
print(random_list)
