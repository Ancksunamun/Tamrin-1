
import math
Op = input(
    "Plz enter the operation you want: + or - or * or / or sin or cos or tan or cot or factorial or radical")


if Op=="sin" or Op=="cos" or Op=="cot" or Op=="tan" or Op=="factorial" or Op=="radical":
    A = float(input("plz enter your number"))
    if Op=="sin":
        result= math.sin(math.radians(A))
    if Op=="cos":
        result= math.cos(math.radians(A))
    if Op=="tan":
        result= math.tan(math.radians(A))
    if Op=="cot":
        result= math.cot(math.radians(A))
    if Op=="factorial":
        result=math.factorial(int(A))
    if Op=="radical":
        result=math.sqrt(A)

elif Op=="+" or Op== "-" or  Op=="*" or Op=="/":
    A = float(input("plz enter your first number:"))
    B = float(input ("plz enter your second number:"))
    if Op=="+":
        result= A + B
    if Op == "-":
        result= A - B
    if Op == "*":
        result= A * B
    if Op == "/":
        if B!=0:
            result= A/ B
        else:
            result="Division to zero eror"

print(result)
