#
# Sam Ghalayini
# CE 232 Stacks HW20
#
#%% Regular Stack
class Stack:
    def __init__(self):
        self.data = []
    def push(self,item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def is_empty(self):
        return self.data == []
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
    def get_stack(self):
        return self.data
s = Stack()
s.push(3)
s.push(5)
print(s.get_stack())
s.pop()
print(s.get_stack())
#%% Convert to Binary
def toBinary(decimal):
    s = Stack()
    bNum = ''
    while decimal > 0:
        remainder = decimal%2
        decimal = decimal//2
        s.push(remainder)
    while not s.is_empty():
        bNum += str(s.pop())
    return bNum
print(toBinary(1234))
#%% Reverse String
def reverseStr(inputStr):
    s = Stack()
    index = 0
    rev = ''
    while index in range(len(inputStr)):
        s.push(inputStr[index])
        index +=1
    while not s.is_empty():
        rev += s.pop()
    return rev
print(reverseStr("HELLO"))

#%% Balanced parenthesis check
def match(first,last):
    if first =='(' and last == ')':
        return True
    elif first =='{' and last == '}':
        return True
    elif first =='[' and last == ']':
        return True
    else:
        return False
def parenBal(string):
    index = 0
    bal = True
    s = Stack()
    if string == '':
        bal = False
        return False
    elif string[-1] in '([{':
        bal = False
        return False
    else:
        while index < len(string) and bal == True:
            if string[index] in '([{':
                s.push(string[index])
            else:
                if s.is_empty():
                    bal = False
                    return False
                elif match(s.pop(),string[index]):
                    bal = True
                else:
                    bal = False
                    return False
            index += 1
    if s.is_empty() and bal == True:
        return True

print(parenBal('[]'))
print(parenBal('()'))
print(parenBal('{}'))
print(parenBal('({[]})'))
print(parenBal(''))
print(parenBal('{(({')) # Dont know why this returns "None"
print(parenBal('{(({))))))))'))
print(parenBal('())'))


#%% Class Notes
# : ! python % "enter" to run python file in vim
# set guifont = 12
# set number
# :vert new test_subfunc.py
# "control WW" to wtich windows























