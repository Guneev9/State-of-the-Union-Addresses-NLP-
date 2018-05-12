#Importing Necessary Packages
import nltk as n
import re
from nltk.collocations import *

#i have executed the .py file in the directory where i have kept the source files.Please provide the complete dir path, if source file and the code is in the separate folder.
#function to get corpus/text file data 
def Get_Corpus(Text):
    #reading
    from nltk.corpus import PlaintextCorpusReader
    corpus_read= PlaintextCorpusReader('.','.*\.txt')
    Part= corpus_read.raw(Text)
    Part_file= corpus_read.fileids()[0]
    Part_string = corpus_read.raw(Part_file)
    return Part_string


#Tokenize
def Tokenize_Corpus(Words):
    Corpus_Tokens = n.word_tokenize(Words) 
    #strip() is used to remove extra whitespaces from the text
    Tokens = [Token.strip() for Token in Corpus_Tokens]
    return Tokens

#function to filter alphabetical words
def Get_aplha_words(words):
# pattern to match a word of non-alphabetical characters
    pattern = re.compile('^[^a-z]+$')
    if (pattern.match(words)):
        return True
    else:
        return False

#function to get pos of the word in order to get lemma's
def get_pos(word):
    #another corpus reader
    from nltk.corpus import wordnet 
    #synsets() is used to lookup a word
    #pos argument is used to constrain the part of speech of the word
    w_synsets = wordnet.synsets(word)
    #for counting the 
    from collections import Counter
    pos_counts = Counter()
    pos_counts["n"] = len([item for item in w_synsets if item.pos()=="n"])
    pos_counts["v"] = len([item for item in w_synsets if item.pos()=="v"])
    pos_counts["a"] = len([item for item in w_synsets if item.pos()=="a"])
    pos_counts["r"] = len([item for item in w_synsets if item.pos()=="r"])
    
    most_common_pos_list = pos_counts.most_common(3)
    # first index for getting the top POS from list, second index for getting POS from tuple
    return most_common_pos_list[0][0]

#function to lemmatize the tokens in order to get lemm'a(base form)
def lemmatize_text(word):
    # NLTK has a lemmatizer that uses WordNet as a dictionary
    from collections import Counter 
    # To get words in dictionary with their parts of speech
    from nltk.corpus import wordnet 
    # lemmatizes word based on it's parts of speech
    from nltk.stem import WordNetLemmatizer
    wnl = WordNetLemmatizer()
    lemma_words=[wnl.lemmatize(t, get_pos(t)) for t in word]  

    return lemma_words

#function for removal of stop words
def remove_stopwords(words):
    stopwords = n.corpus.stopwords.words('english')
    #custom stop words, not much meaningful for analysis point of view
    stopwords = stopwords + ['ebook', 'ebooks', 'january', 'february', 'march',
                            'april', 'may', 'june', 'july', 'august',
                            'september', 'october', 'november', 'december',
                             'state','address','copyright','union']

    filter2_words = [w for w in words if w not in stopwords]
    return filter2_words

#function to get top most frequency words, normalized by length of document
def Top50_freq(w):
    from nltk import FreqDist
    words={}
    Part1dist = FreqDist(w)
    d = dict(Part1dist.most_common(50))
    for token,f in d.items():
        #normalizing it by length of filtered document w
         words[token]=f/float(len(w))
    return words
        
# setup for bigrams and bigram measures
from nltk.corpus import stopwords

def bigram_with_filter(w):
    finder = BigramCollocationFinder.from_words(w)
    bigram_measures = n.collocations.BigramAssocMeasures()
    stopwords = n.corpus.stopwords.words('english')
    #custom stop word
    stopwords = stopwords + ['ebook', 'ebooks', 'january', 'february', 'march',
                            'april', 'may', 'june', 'july', 'august',
                            'september', 'october', 'november', 'december',
                             'state','address','copyright','union','addresses']
    # apply a filter to remove non-alphabetical tokens
    finder.apply_word_filter(Get_aplha_words)
    #removed low frequency words
    finder.apply_freq_filter(2)
    # apply a filter to remove stop words
    finder.apply_word_filter(lambda w: w in stopwords)
    scored = finder.score_ngrams(bigram_measures.raw_freq)   
    for bscore in scored[:50]:
        print (bscore)
        


def Top50bigrams_MutualInfoScore(w):  
    finder2 = BigramCollocationFinder.from_words(w)
    bigram_measures = n.collocations.BigramAssocMeasures()
    stopwords =  n.corpus.stopwords.words('english')
    stopwords = stopwords + ['ebook', 'ebooks', 'january', 'february', 'march',
                            'april', 'may', 'june', 'july', 'august',
                            'september', 'october', 'november', 'december',
                             'state','address','copyright','union','addresses']
    # apply a filter to remove non-alphabetical tokens
    finder2.apply_word_filter(Get_aplha_words)
    finder2.apply_word_filter(lambda w: w in stopwords)
    finder2.apply_freq_filter(5)
    scored = finder2.score_ngrams(bigram_measures.pmi)
    for bscore in scored[:50]:
        print (bscore)
        
def Part_1_execution():
    #fetching the corpus
    Part_string=Get_Corpus('state_union_part1.txt')
    #Tokenization
    Tokens=Tokenize_Corpus(Part_string)
    #lowercase conversion after fetching alphabetical words
    Part1_filter1_words= [w.lower() for w in Tokens if not Get_aplha_words(w)]
    #Lemmatization
    Part1_filter2_words=lemmatize_text(Part1_filter1_words)
    #Removal of Stop Words
    Part1_filter3_words=remove_stopwords(Part1_filter2_words)
    #Functions calling and Results
    Top50_freq_words=Top50_freq(Part1_filter3_words)
    print("####################### PROBLEM-2(STATE UNION PART-1 FILE) ##########################")
    print("#############################Top 50 words by frequency###########")
    print (Top50_freq_words)
    print("##################### Top 50 Bigrams by frequency ##################################")
    bigram_with_filter(Tokens)
    print("###################### Top 50 Bigrams by thier Mutual Information Scores ########################")
    Top50bigrams_MutualInfoScore(Tokens)

def Part_2_execution():
    #fetching the corpus
    Part_string=Get_Corpus('state_union_part2.txt')
    #Tokenization
    Tokens=Tokenize_Corpus(Part_string)
    #lowercase conversion after fetching alphabetical words
    Part2_filter1_words= [w.lower() for w in Tokens if not Get_aplha_words(w)]
    #lemmatization
    Part2_filter2_words=lemmatize_text(Part2_filter1_words)
    #Stop words Removal
    Part2_filter3_words=remove_stopwords(Part2_filter2_words)
    #Functions calling and results
    Top50_freq_words=Top50_freq(Part2_filter3_words)
    print("####################### PROBLEM-3 (STATE UNION PART-2 FILE) ##########################")
    print("##################### Top 50 words by frequency #############################")
    print (Top50_freq_words)
    print("######################## Top 50 Bigrams by frequency ###############################")
    bigram_with_filter(Tokens)
    print("######################### Top 50 Bigrams by thier Mutual Information Scores ###########################")
    Top50bigrams_MutualInfoScore(Tokens)
    
#Final Execution

if __name__ == '__main__':
    Part_1_execution()
    Part_2_execution()
