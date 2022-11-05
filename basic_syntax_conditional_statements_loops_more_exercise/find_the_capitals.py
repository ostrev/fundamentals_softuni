string_single = list(input())
result_list = []
for index in range(len(string_single)):
    if string_single[index].isupper():
        result_list.append(index)
print(result_list)
