count = 0
text = input()
vowels = "aeiouAEIOUyY"
for i in text:
    if i in vowels:
        count += 1
print(count)
