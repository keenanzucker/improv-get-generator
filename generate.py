import markovify

# Commands to use:

# 1. make_sentence()
# 2. make_short_sentence()
# 3. make_sentence_with_start(string)


# # Build the model.
# clean_text = clean_book('texts/shakespeare.txt')
# text_model = markovify.Text(clean_text)

# model_a = markovify.Text(clean_book('texts/shakespeare.txt'))
# model_b = markovify.Text(clean_book('texts/sherlockHolmes.txt'))
# model_c = markovify.Text(clean_book('texts/robertBurns.txt'))

# model_combo = markovify.combine([ model_a, model_b, model_c ])

# # Print five randomly-generated sentences
# # print(model_combo.make_sentence_with_start('The', tries=1000))
# # for i in range(3):
# #   print(model_combo.make_sentence())

# Let's declare a function to get word index
def get_index(in_list,in_string):
  for num,row in enumerate(in_list):
    if in_string in row:
        return num
# We convert the script from the NLTK Stopwords tutorial into a def
def clean_book(path):
  # Let's open the book we downloaded
  book = open(path,'r').read()
  # Divide text by rows
  rows = book.split('\n')
  # Search for START and END tags to remove useless parts
  start_idx = get_index(rows,'*** START')
  end_idx = get_index(rows,'*** END')
  rows = rows[start_idx+1:end_idx]
  # We need to create a string for markovify
  text = '\n'.join([r for r in rows if r!=''])
  return text

def printParagraph(model, wordInput):
  print(model.make_sentence_with_start(wordInput, False, tries=1000))
  for i in range(3):
    print(model.make_sentence())


def getModel(filePath): 
  clean_text = clean_book(filePath)
  text_model = markovify.Text(clean_text)
  return text_model
  
if __name__ == '__main__':
  startWord = 'speech'
  file = 'texts/longfellow.txt'
  model = getModel(file)
  printParagraph(model, startWord)