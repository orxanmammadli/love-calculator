print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name3=(name1+name2).lower()
t=name3.count("t")
r=name3.count("r")
u=name3.count("u")
e=name3.count("e")
true=t+r+u+e
l=name3.count("l")
o=name3.count("o")
v=name3.count("v")
e=name3.count("e")
love = l+o+v+e
love_score=str(true)+str(love)
int_ls=int(love_score)
if int_ls<40 and int_ls>50:
  print(f"Your score is {int_ls}, you are alright together.")
elif int_ls>10 or int_ls>90:
  print(f"Your score is {int_ls}, you go together like coce and mentos.")
else:
  print(f"Your score is {int_ls}.")
love=name3.count("l")
print(str(true)+str(love))

