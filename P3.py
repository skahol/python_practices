#reserve order of list and print only unique elements
def unique(my_list):
    seen = set()
    # list comprehension
    return [x for x in my_list if not (x in seen or seen.add(x))]

my_list = [12,24,35,24,88,120,155,88,120,155]
print(unique(my_list))