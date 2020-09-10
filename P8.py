temp_list = []
for i in range(1,21):
    temp_list.append(i)

my_list = list(map(lambda num:num**2,temp_list))
print(my_list)