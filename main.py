
class Stack:
         def __init__(self):
            self.items = []

         def isEmpty(self):
             return self.items == []

         def push(self, item):
             self.items.insert(0,item)

         def pop(self):
             return self.items.pop(0)

         def peek(self):
             return self.items[0]

         def size(self):
             return len(self.items)

def check(myStr):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = Stack()
    for i in myStr:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((stack.size() > 0) and
                (open_list[pos] == stack.peek() )):
                stack.pop()
            else:
                return "Unbalanced"
    if stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"


balanced= ["(((([{}]))))",
"[([])((([[[]]])))]{()}",
"{{[()]}}"]

unbalanced= ["}{}",
"{{[(])]}}",
"[[{())}]"]

for k in unbalanced:
    print(check(k))

for i in balanced:
    print(check(i))
