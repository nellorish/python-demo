import random
number = input()

print("Your Enter the number :"+number)

minNumber = 1
maxNumber = 100

magicNumber = random.randint(minNumber, maxNumber)
print(magicNumber)

message= "This is a magic number {0} and {1}"
print(message.format(minNumber,maxNumber))

found=False

while not found:
    print("Guess what it is ?")
    guess = int(input())
    print(guess)

    if guess==magicNumber:
        found = True
        print("*******")

    if guess < magicNumber:
         print("Too Low")

    if guess > magicNumber:
         print("Too High")



print("Got it")


