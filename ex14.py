from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}), I'm the {script} script")
print("I'd like to ask you a few quetions")
print(f'Do you like me {user_name}?')
likes = input(prompt)

print(f'Where do you live {user_name}?')
lives = input(prompt)

print(f'What kind of computer do you have')
computer = input(prompt)

print(f"""
18 Alright, so you said {likes} about liking me.
19 You live in {lives}.
20 And you have a {computer} computer.
21 """)
