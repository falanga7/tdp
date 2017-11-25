from Gruppo6_3_TdP.count_kmp import count_kmp

print("Primo test:count_kmp(\"ababa\",\"aba\")=")
count = count_kmp("ababa", "aba")
print(count)

print("Secondo test:count_kmp(\"abababa\",\"aba\")=")
count = count_kmp("abababa", "aba")
print(count)
