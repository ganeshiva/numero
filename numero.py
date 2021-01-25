#!/usr/bin/python

codeHeader='''
title="Find the Numberology of the name word (English)"
summary="Calculate the Numberology of the given name word"
author=Ganeshiva
created=20200125
updated=20200125
cmdLine="python3 <filename>"
dependancy="python3"
license="(c)ganeshiva - freeToUse@yourOwnRisk - noGuaranty"
reference: https://astrologyfutureeye.com/fortune-tellers/name-numerology-calculator
'''
def sumOfDigits(numberInput):
    singleNumberValue=0
    for digit in str(numberInput):
        singleNumberValue += int(digit)
    if singleNumberValue == 0:
        singleNumberValue = numberInput
    return singleNumberValue

print("Welcome to Numberology Calculator! :~")
name=str(input("Enter the name: "))
numeroDict ={
'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':8,
'g':3,
'h':5,
'i':1,
'j':1,
'k':2,
'l':3,
'm':4,
'n':5,
'o':7,
'p':8,
'q':1,
'r':2,
's':3,
't':4,
'u':6,
'v':6,
'w':6,
'x':5,
'y':1,
'z':7,
}
vowels = ['a','e','i','o','u']
destinyBriefing='''Destiny Number:
The main name numeral is known as destiny or expression number. 
This is the digit which describes who you are and what you are or what you become.
This is referred as destiny and your life's purpose.
This is the sum of all name numbers of alphabets.
'''
numeroDestinyTotalValue=0
desireBriefing='''Soul Urge Number / Desire Number:
The heart desire number is known also as the soul urge.
The numeral is calculated from vowels in a name.
This is the number which describes your inner potentials, inner likes and dislikes, inner resources.
In simple words, what you are actually, by your inner core, what your inner desire which you kept private from others.
'''
numeroDesireTotalValue=0

dreamBriefing='''Dream Number / Personality Number:
Personality number is known also as dream or inner-dream.
The numeral is calculated from consonants in a name.
This is the number which describes your personality, indeed your first impression on others.
In simple words, this describes how and what you present yourself to the world.
This is your outer personality which may be different from your inner soul.
'''
numeroDreamTotalValue=0

for letter in name.lower():
    numeroDestinyTotalValue+=numeroDict.get(letter,0)
    if letter in vowels:
        numeroDesireTotalValue += numeroDict.get(letter,0)
    else:
        numeroDreamTotalValue += numeroDict.get(letter,0)

numeroDestiny = sumOfDigits(numeroDestinyTotalValue)
numeroDesire = sumOfDigits(numeroDesireTotalValue)
numeroDream = sumOfDigits(numeroDreamTotalValue)

print("~~~~~~~~~~~~~~~~~~~ " + name + " ~~~~~~~~~~~~~~~~~~")
print(" Destiny Value: " + str(numeroDestinyTotalValue) + "/" + str(numeroDestiny))
print(" Desire Value: " + str(numeroDesireTotalValue) + "/" + str(numeroDesire))
print(" Dream Value: " + str(numeroDreamTotalValue) + "/" + str(numeroDream))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n\nBriefing")
print(destinyBriefing)
print(desireBriefing)
print(dreamBriefing)