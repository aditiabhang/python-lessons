# Hacker rank list problem 

'''
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''


# if __name__ == '__main__':
#     N = int(input())

# print(N)
# # L = []

# # # for i in range(0, N):
# tokens = input().split()

# print(tokens)   # ['insert', '0', '5'] 
# # print(L)     # [5]

arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print (arr.index(s[1]))
    elif s[0] == "count":
        print (arr.count(s[1]))
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)


# if __name__ == '__main__':
#     N = int(input())


L = []

S1 = 'insert 0 5 insert 1 10 insert 0 6 print remove 6 append 9 append 1 sort print pop reverse print'.split()
print(S1)

# for i, l_element in enumerate('insert 0 5 insert 1 10 insert 0 6 print remove 6 append 9 append 1 sort print pop reverse print'.split()):
#     print("print here: ", l_element)
#     if l_element[0][0] == 'insert':
#         L.insert(l_element[0][1], l_element[0][2])
#     elif l_element[1][0] == 'insert':
#         L.insert(l_element[1][1], l_element[1][2])  
#     elif l_element[2][0] == 'insert':
#         L.insert(l_element[2][1], l_element[2][2])
#     elif l_element[3] == 'print':
#         print(L)
#     elif l_element[4][0] == 'remove':
#         L.remove(l_element[4][1])
#     elif l_element[5][0] == 'append':
#         L.append(l_element[5][1])
#     elif l_element[6][0] == 'append':
#         L.append(l_element[6][1])
#     elif l_element[7] == 'sort':
#         L.sort()    
#     elif l_element[8] == 'print':
#         print(L)
#     elif l_element[9] == 'pop':
#         L.pop()
#     elif l_element[10] == 'sort':
#         L.sort(reverse=True) 
#     elif l_element[11] == 'print':
#         print(L)