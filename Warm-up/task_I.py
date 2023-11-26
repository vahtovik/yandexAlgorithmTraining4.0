s = input()
brackets = {'[]', '{}', '()'}
stack = ['x']
for char in s:
    if char in '[({':
        stack.append(char)
    elif (stack.pop() + char) not in brackets:
        print('no')
        break
else:
    print(('no', 'yes')[stack[-1] == 'x'])
