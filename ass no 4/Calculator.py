{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6568abd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select operationns.\n",
      "1.Add\n",
      "2.Substract\n",
      "3.Multiply\n",
      "4.Divide\n",
      "5.Power\n",
      "Enter choice 1/2/3/4/5: 3\n",
      "Enter the first number: 2\n",
      "Enter the second number: 2\n",
      "2 * 2 = 4\n"
     ]
    }
   ],
   "source": [
    "#program to make calculator using python\n",
    "\n",
    "def add(x,y):\n",
    "    \"\"\"This function adds 2 numbers\"\"\"\n",
    "    return x + y\n",
    "def substract(x,y):\n",
    "    \"\"\"This fumction substract 2 numbers\"\"\"\n",
    "    return x - y\n",
    "def multiply (x,y):\n",
    "    \"\"\"This function multiplies 2 numbers\"\"\"\n",
    "    return x * y\n",
    "def divide (x,y):\n",
    "    \"\"\"This function divides 2 numbers\"\"\"\n",
    "    return x / y\n",
    "def power (x,y):\n",
    "    \"\"\"This gives power\"\"\"\n",
    "    return pow(x,y)\n",
    "    \n",
    "#take input frm user\n",
    "print(\"Select operationns.\")\n",
    "print(\"1.Add\")\n",
    "print(\"2.Substract\")\n",
    "print(\"3.Multiply\")\n",
    "print(\"4.Divide\")\n",
    "print(\"5.Power\")\n",
    "choice=input(\"Enter choice 1/2/3/4/5: \")\n",
    "num1=int(input(\"Enter the first number: \"))\n",
    "num2=int(input(\"Enter the second number: \"))\n",
    "\n",
    "if choice == '1':\n",
    "    print(num1, \"+\", num2, \"=\", add(num1,num2))\n",
    "\n",
    "elif choice == '2':\n",
    "    print(num1, \"-\", num2, \"=\", substract(num1,num2))\n",
    " \n",
    "elif choice == '3':\n",
    "    print(num1, \"*\", num2, \"=\", multiply(num1,num2))\n",
    "\n",
    "elif choice == '4':\n",
    "    print(num1, \"/\", num2, \"=\", divide(num1,num2))\n",
    "elif choice == '5':\n",
    "    print(num1, \"^\", num2, \"=\", power(num1,num2))\n",
    "\n",
    "else:\n",
    "    print('invalid input')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c81eca4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
