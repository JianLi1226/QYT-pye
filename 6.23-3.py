import PyInstaller

print("Pls input any word:")
word = str(input())

# new_list_word = list(word)

# first_cha = new_list_word.pop(0) # pop the first character
#
# # Note list.append() does not return a new list
# new_list_word.append('-')  # add a dash at the end of the word
# new_list_word.append(first_cha)
# new_list_word.append('y')
#
# print('Translated: ' + ''.join(new_list_word))

# much better method
new_word = word[1:] + word[0] + '-' + 'y'
print(new_word)