print('=== Stack dengan List ===')
stack = []

stack.append('www.google.com')
stack.append('www.facebook.com')
stack.append('www.youtube.com')
stack.append('www.instagram.com')

topElement = stack[-1]
print("Top element:", topElement)

popp = stack.pop()
print('Pop:', popp)

print('Stack After Pop:', stack)

isempty = not bool(stack)
print('Apakah stack kosong?', isempty)

print('SIze:', len(stack))
