
  # Programmer:  Joseph Segich
  # Course:  CS201.01, Dr. Olsen
  # Date: 9/16/15
  # Assignment:  PA1
  # Problem Statement:  Solves the quadradic formula
  # Data In: values of the coefficents of a quadradic function
  # Data Out:  answers to the quadradic formula

#statement that explains what the program does
print('this program will solve the quadradic formula')

#inputing the values of the coefficents
a=int(input('A='))
b=int(input('B='))
c=int(input('C='))

#Preforming calculations
answer1=(((b)+((b**2)+(4*a*c))**(1/2))/(2*a))
answer2=(((-b)-((b**2)-(4*a*c))**(1/2))/(2*a))

#Outputting results to the reader
print('Answer1=',answer1)
print('Answer2=',answer2)
