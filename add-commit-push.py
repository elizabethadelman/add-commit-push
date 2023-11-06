from turtle import clear
from distutils.util import execute

m = input("Enter your commit message")
message = "-m " + m
print("git status: ")
def confirm_choice():
    while True:
        answer = input("Are you sure? (y/n)") != "y"
        answer = answer.lower()
        if answer == 'y':
            return execute
        if answer == 'n':
            return clear
        if answer == '-f' and accept_enter_key:
            return [force]
        print('Answer with "y" for yes or "n" for no.')
    return confirm

    exit()
  