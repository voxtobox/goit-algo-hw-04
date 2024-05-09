from random import randint
from timeit import timeit
from sort_it import sort_insertion, sort_merge

def generate_array(elements_number):
    arr = []
    
    for i in range(elements_number):
        arr.append(randint(0, 1000))
        
    return arr

def test_arr(size_number, size_name):
    arr = generate_array(size_number)
    
    print(f"{size_name} масив {size_number} елементів\n")
    
    t = timeit(lambda: sorted(arr), number=1)
    print(f"Сортування Timsort: {t}ms")
    
    t = timeit(lambda: sort_merge(arr), number=1)
    print(f"Сортування злиттям: {t}ms")
    
    t = timeit(lambda: sort_insertion(arr), number=1)
    print(f"Сортування вставкою: {t}ms")
    print('\n')
        
def main():
    test_arr(100, 'Малий')
    test_arr(1000, 'Середній')
    test_arr(10000, 'Великий')
    
main()