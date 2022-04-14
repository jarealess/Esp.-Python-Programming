####### SENTIMENT ANALYSIS #########################
### LA IDEA ES TOMAR UNOS DATOS DE TWEETS, RETWEETS, REPLIES, APLICAR LAS SIGUIENTES FUNCIONES A LA COLUMNA DE TWEETS Y 
## PONER LUEGO TODO JUNTO EN OTRO CSV

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

### Remove punctiation from a word
def strip_punctuation(x):
    for chart in punctuation_chars:
        x = x.replace(chart, '')
    return x

## count number of positive words in a sentence
def get_pos(string_char):
    words = string_char.split()
    ct = 0
    for word in words:
        if strip_punctuation(word).lower() in positive_words:
            ct += 1
    return ct

## count number os negative words in a sentence
def get_neg(string_char):
    words = string_char.split()
    ct = 0
    for word in words:
        if strip_punctuation(word).lower() in negative_words:
            ct += 1
    return ct

### LECTURA DATOS
twitter_data = []
with open('project_twitter_data.csv', 'r') as f2:
    for lin in f2:
        if lin[0] != ';' and lin[0] != '\n':
            twitter_data.append(lin.strip())


### ESCRITURA RESULTADOS
OutputFile = open('resulting_data.csv', 'w')
OutputFile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
OutputFile.write('\n')
for line in twitter_data[1:]:
    tweet = line.split(',')[0]
    retweets = line.split(',')[1]
    replies = line.split(',')[2]
    pos_val = get_pos(tweet)
    neg_val = get_neg(tweet)
    net_score = pos_val-neg_val
    row_file = f'{int(retweets)},{int(replies)},{pos_val},{neg_val},{net_score}'
    OutputFile.write(row_file+'\n')

