# animal.py

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print(f"Hello, I am {self.__name} and I am {self.__age} years old.")

    def talk(self):
        print(f"{self.__name} says hi!")

    def eat(self, food):
        print(f"{self.__name} is eating {food}.")

    def sleep(self, hours):
        print(f"{self.__name} is sleeping for {hours} hours.")

    def move(self, distance):
        print(f"{self.__name} moved {distance} meters.")

    def celebrate_birthday(self):
        self.__age += 1
        print(f"Happy Birthday, {self.__name}! You are now {self.__age} years old.")

    def describe(self):
        print(f"{self.__name} is a {self.__age}-year-old animal.")


