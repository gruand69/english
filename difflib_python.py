import difflib

# text1 = "Python - лучший язык программирования!"
# text2 = "Python - самый лучший язык для программирования!"

# d = difflib.Differ()
# diff = d.compare(text1.splitlines(), text2.splitlines())
# print('\n'.join(diff))


s = difflib.SequenceMatcher(None,
                            "Hi - you must be John's cousin Matt, right? From San Diego?",
                            "Hi - you must be John's cousin Matt, right? From San Diego")
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print(f"{tag} a[{i1}:{i2}] b[{j1}:{j2}]")
print(s.get_opcodes()[1][1])
