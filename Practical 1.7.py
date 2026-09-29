def remove_dollar_sign(s):
    s = s.replace("$", "")
    return s
s = str(input("Type your string: "))
new_s = remove_dollar_sign(s)
print(new_s)