#Word Counter

input_string =   input("Enter the text for word count:\n") + '/'

word_count = 0
special_character_count = 0


for i in range(len(input_string)) :
   a = input_string[i].lower()
   b = input_string[i - 1].lower()
   if (a > 'z' or a < 'a') :
        special_character_count  += 1
        if (b <= 'z' and b >= 'a') :
            word_count += 1
        else :
            continue

print(f"Word count :\t{word_count}")

