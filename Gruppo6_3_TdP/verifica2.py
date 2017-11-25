from Gruppo6_3_TdP.count_kmp import count_kmp

print("Primo test:count_kmp(\"ababa\",\"aba\")=")
count = count_kmp("ababa", "aba")
print(count)

print("Secondo test:count_kmp(\"abababa\",\"aba\")=")
count = count_kmp("abababa", "aba")
print(count)

# print("Terzo test:count_kmp(22, 33)=")
# count = count_kmp(22, 33)
# print(count)

# print("Quarto test:count_kmp(\"test\", 33)=")
# count = count_kmp("test", 33)
# print(count)

print("Quinto test:count_kmp(\"aba\",\"abababa\")=")
count = count_kmp("aba", "abababa")
print(count)

print("Sesto test:count_kmp(\"aba\",\"aba\")=")
count = count_kmp("aba", "aba")
print(count)

print("Settimo test:count_kmp(\"\",\"aba\")=")
count = count_kmp("", "aba")
print(count)

print("Ottavo test:count_kmp(\"\",\"\")=")
count = count_kmp("", "")
print(count)

print("Nono test:count_kmp(\"aba\",\"\")=")
count = count_kmp("aba", "")
print(count)