linguagens = ['python', 'js', 'c', 'java', 'C#']

print(sorted(linguagens, key=lambda x: len(x)))  # ['c', 'js', 'C#', 'java', 'python']
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ['python', 'java', 'js', 'C#', 'c']

print(sorted(linguagens))
