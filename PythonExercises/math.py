import math
#Exercise 2 for python

#int
oddnum = 5
evennum = 6
#float
floatnum = 3572.5571
#complex
compnum = 15+3j
#hex
hexnum = 0x13
print(type(oddnum),type(floatnum),type(compnum),type(hexnum))


#1.)
#operations
op1 = oddnum/2
print(op1,type(op1))

op2 = evennum/2
print(op2,type(op2))

op3 = int(floatnum/5)
print(op3,type(op3))


#2.)
#division
negoddnum = -5
div1 = oddnum/2
div2 = oddnum//2
div3 = oddnum%2
print((div1,type(div1)),(div2,type(div2)),(div3,type(div3)))

negdiv1 = oddnum/-2
negdiv2 = oddnum//-2
negdiv3 = oddnum%-2
print((negdiv1,type(negdiv1)),(negdiv2,type(negdiv2)),(negdiv3,type(negdiv3)))

#3.)
#Rounding!
notround = 15.19573
biground = round(notround,4)
mediumround = round(notround,3)
smallround = round(notround,1)
print(biground,mediumround,smallround)
#abs
val = -1500
val2 = 1500
compare = val == val2
compare2 = abs(val) == val2
print(compare,compare2)
#pow
explosion = pow(5,2)
print(explosion)



#4.)
#triangle
a = 15.5
b = 13.7
c = math.sqrt(a**2 + b**2)
print(c)
c = math.sqrt(pow(a,2) + pow(b,2))
print(c)



#5.)
#hex
op1 = hexnum + 5
op2 = hexnum - 15
op3 = hexnum/3
op4 = hexnum**2
print(hexnum,type(hexnum))
print((op1,type(op1)),(op2,type(op2)),(op3,type(op3)),(op4,type(op4)))
print(hex(hexnum))


#6.)
#hexnum = hex('0x13')
print(int(hexnum))
