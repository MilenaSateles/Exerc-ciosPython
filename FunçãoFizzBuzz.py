# função fizzbuzz devolve "fizz" se o número for divisível por 3 e não por 5;
# "buzz" se o número for divisível por 5 e não por 3; e "fizzbuzz" se for
# divisível por ambos.



def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 != 0):
        return "Fizz"
    if  (x % 5 == 0) and (x % 3 != 0):
        return "Buzz"
    if  (x % 3 == 0) and (x % 5 == 0):
        return "FizzBuzz"
    else:
        return x

    
