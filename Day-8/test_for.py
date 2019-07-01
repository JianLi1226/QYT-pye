List1 = ["aaa", 111, (4,5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4,5)]
# for x in List1:
#     for y in List2:
#         if x == y:
#             print(str(x),'in List1 and List2')
#             break
#     else:
#         print(str(x), 'only in List1')


# Method 2
print(f'Elements in both lists:\n{set(List1) - (set(List1) - set(List2))}')
print(f'Elements only in List1:\n{set(List1) - set(List2)}')

print('*'* 80)
# Function comparing two lists
def compare_lists(list1, list2):
    for x in list1:
        for y in list2:
            if x == y :
                print(str(x), 'in both lists')
                break
        else:
            print(str(x), f'only in first list')

compare_lists(List1, List2)