# Python code to print the string with minimum number of unique characters
list = ['abc', 'qr', 'with', 'boywp', 'cabled']
print("Original List is:" + str(list))
dict = {i: len(set(i)) for i in list}
pranjal = min(dict, key=dict.get)
print("The string with minimum unique characters is:" + str(pranjal))
