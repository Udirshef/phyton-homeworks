txt = "abcabcdabcdeabcdefabcdefg"  
vowels = "aeiouAEIOU"  
result = ""

for i in range(len(txt)):
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        if txt[i] in vowels or (i > 0 and txt[i-1] == '_'):
             result += txt[i]
        else:
            result += txt[i] + "_"
    else:
        result += txt[i]

print(result)
