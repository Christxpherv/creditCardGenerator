# creditCardGenerator

Generates MasterCard and Visa card numbers utalizing their respective requirements to create real numbers that also satisfy the Luhn formula until the user 
decides to exit the program. 

Luhn Formula:
- starting from the next-to-last digit, double every other digit going left.
- for each of the doubled values that exceed 9, subtract 9.
- add up all the doubled values, along with the digits that were not doubled.
- if the result is a multiple of 10, the number satisfies the Luhn formula. If the result is not a multiple of 10, the number does not satisfy
  the Luhn formula.


Requirements (MasterCard):
- must start with 51-55 (inclusive) or 222100-272099 (inclusive)
- must be 16 digits in length

Requirements (Visa): 
- must start with 4 
- must be 13, 16, or 19 digits in length
