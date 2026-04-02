"""String basic exercises."""

first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string[10::-1]

cake = "toppingfillingbase"
print(cake[0:7] + "\n" + cake[7:14] + "\n" + cake[14:18])
