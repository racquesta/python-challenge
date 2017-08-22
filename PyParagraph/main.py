import os
import string

#choose file_number (1 or 2)
file_num = 2

#sets file
file = os.path.join('raw_data', 'paragraph_' + str(file_num) + '.txt')

# open and reads file and saves text as paragraph string?
paragraph = ''
with open(file, 'r') as txtfile:
    paragraph = txtfile.read()


#sentence count by counting .
sen_count = paragraph.count('.')

#sentences = paragraph.split('.')

#creates a string of upper and lowercase letters
letters = string.ascii_letters + " " 

#loops through paragraph string and deletes all characters 
# that are not letters replacing with nothing
for c in paragraph:
    if c not in letters:
        paragraph = paragraph.replace(c,'')


#reassigns the paragraph string and makes a list of words by splitting at spaces
paragraph = paragraph.split(" ")

#counts all of the letters in list paragraph
letter_total = 0
for word in paragraph:
    letter_total += len(word)

#counts words by counting the length of paragraph list
word_count = len(paragraph)

#calculates average word length by dividing the total # of letters
#by the number of words
avg_word_length = letter_total/word_count

# calculates words per sentence by dividing the number of words by the number of sentences.
words_per_sentence = word_count/sen_count


output_file = os.path.join('Output', 'paragraph_analysis_' + str(file_num)+ '.txt')

with open(output_file, 'w') as txtfile:

    txtfile.writelines('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + 
                        '\nAverage Letter Count: ' + str(avg_word_length) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))

with open(output_file, 'r') as txtout:
    print(txtout.read())

