import math

a = str(input())
a = '(' + a + ')'
s = ''
b = ''
for i in a:
    if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
        b = b + i
        if len(s) != 0:
            if s[-1] == '*' or s[-1] == '/':
                b = b + s[-1]
                s = s[:-1]
    elif i == ')':
        while s[-1] != '(':
            b = b + s[-1]
            s = s[:-1]
        s = s[:-1]
    else:
        while (i == '+' or i == '-') and len(s) != 0:
            if s[-1] != '(':
                b = b + s[-1]
                s = s[:-1]
            else: break
        s = s + i
print(b) 

# a+b*c-(a+b-c)/k
# (a-b+c)/(d*e-f)+r
# a+b*(c-d*e*(f-c-l))-3
# a+b*(c+d*(e-k*r))



    
    
