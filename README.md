# State of Union Data set
The State of the Union Addresses dataset is a collection of annual speeches delivered by the presidents of the United States, 
from George Washington to Barack Obama, to a joint session of the United States Congress for the span of 1790-2016. 
This dataset contains the two texts combined, which are small subsets of the Project Gutenberg Ebook corpus. 
Here is the Project Gutenberg Ebook web page: http:// http://www.gutenberg.org/

#Analysis
Files are taken from Gutenberg EBook "Complete State of Union Addresses" written by James Linden. State of Union addresses 
is the message given by the President of US to joint session of Congress after first year of a new president's term. 
George Washington delivered the first annual on January 8, 1790, in New York City. In 1801, Thomas Jefferson discontinued 
the practice of delivering the address in person and thus, the address was written and then sent to Congress for reading. 
Presidents during the latter half of the 20th century have sent written State of the Union addresses. For many years, 
the speech was referred to as "the President's Annual Message to Congress". They contain details about budget and an economic 
report of nation and allows the President to outline their legislative agenda and national priorities.
Each Addresses in the book are separated by “***”. Both the files are written by the same author “James Linden”. 
Every message has sections indicating to whom it is being cited. Naming Convention:
Content of files have index convention: President Name followed by Title "State of Union Address" followed by the Date, 
when message has been delivered. The messages have been sorted on basis of year, it is being delivered. 
Part1 contains messages from year 1790 to 1860 and Part2 contains messages from 1946 to 2016. First file contains 
71 messages whereas File2 contains 970 messages.

#Document Policy:
Every book has copyright policy before downloading it in any country or redistributing it. Both the files have header saying 
that, written permission is needed to remove the header or before making any changes to it. It contains the
"legal small print," and other information about the eBook and Project Gutenberg. It states important information about
the specific rights and restrictions in how the file may be used. You can also find out about how to make donation to project
, and how to get involved. The policy starts with "*** END OF THIS PROJECT GUTENBERG EBOOK STATE UNION ADDRESSES ***".
Initially, it has mentioned that, anyone can copy and distribute it in the United States without permission and without 
paying copyright royalties. It’s "General Terms of Use part" section has rules of this license, apply to copying and 
distributing the project. It further states that book can used for any purpose and can be modified. 
There is a License note (Points A to F) after that, which is giving instructions before modifying or redistributing the book. 
Then Section-2 talks about mission of Gutenberg project. Section-3 gives information about its Literary Archive Foundation. 
Section 4 tells about Donations to the its Foundation and Section-5 tells General Information about its electronic works.

##Analysis of State of the Union Addresses dataset: Part1
#Top 50 words by frequency (normalized by the length of the document):
As per my understanding of “normalization by the length of document”, I have filtered the frequency by normalizing it against 
length of filtered Tokens. This means that distribution
 
will give scores on behalf of filtered tokens not the whole document. It is slightly different from the term frequency 
concept where frequency of every token is retrieved against multiple documents.
a) Get_Corpus() function is created to get corpus using PlaintextCorpusReader.
b) Tokenize_Corpus() function is used to get tokens from the corpus.
c) Get_aplha_words(w) function is then used to remove punctuations and non-
Alphabetical words ([,],*,41).
d) Then, I have Lemmatize the words to get their base form with use of Vocabulary.
Also, I have done this before removing the stop words because there are words like address/addresses which can be removed 
in stop-words after getting their basic form easily.
e) remove_stopwords() function is then used to remove English stop words. I have appended the list with some other 
stop words (months and ebook, ebooks) since it is not used for analysis.
f) I have used the function Top50_freq(w) to get frequency distribution of above filtered top50 words.
I have normalized this frequency by the length of the document.
g) I have used the filtered words list for the length of document since, taking the raw corpus length will not give any 
good results because it contains text which is not useful at all and hence removed from token list.

##Top 50 bigrams by frequencies:
a) Ihaveusedbigram_with_filter()functiontoapplyvariousfilterfunctionstofinder.I have first applied Get_aplha_words() 
function to get only alphabetical words. Then further I have applied filter to remove stop words. Now, here I am not 
lemmatizing the words, so I have included ‘addresses’ also in stop words list. At last I have applied filter to get 
words having minimum frequency 0f 2 since otherwise result will not be much helpful.
b) The scores are sorted in order of decreasing frequency.
c) The Result has given the top 50 bigrams by frequencies of meaningful important
bigrams.

##Top 50 bigrams by their Mutual Information scores (using min frequency 5)
a) I have used the Top50bigrams_MutualInfoScore() function for this.
b) I have first removed the stop words and fetched only alphabetical words before
using the PMI measure.
c) Then,IhaverunPMIscorerwithaminimumfrequencybecauseitwillnotbeuseful
to apply the Mutual Information score to all the bigrams as results don’t really make sense and expressions are also 
very infrequent, because uniquely occurring pairs of words get high scores. Thus, it will be good to filter it, to make 
sense for very heavy documents.
d)PMI gives strange results when frequencies are very low e.g. 1-3 tokens, thus set a minimum frequency for the collocates, 
which takes care of most of the problem.
e) The result has given me the bigram pairs which are frequent by their associativity.

#Analysis of State of the Union Addresses dataset: Part2
I have used the same functions for Part-2 as well because it has the similar text containing state of union addresses for 
ifferent year written by the same author.

##Top 50 words by frequency (normalized by the length of the document):
a) Get_Corpus() function is created to get corpus using PlaintextCorpusReader.
b) Tokenize_Corpus() function is used to get tokens from the corpus.
c) Get_aplha_words(w) function is then used to remove punctuations and non-
Alphabetical words like numbers, asterisk etc. Also, I have converted all the tokens
to lowercase.
d) remove_stopwords() function is then used to remove English stop words. I have
appended the list with some other stop words (months and ebook, ebooks) since I
am only looking for words which are gist of the document.
e) Here,alsoIhavelemmatizethewordtogetthedictionaryform.
f) I have used the function Top50_freq(w) to get frequency distribution of above
filtered top50 words. I have normalized this frequency by the length of the
document.
g) I have used the filtered words list for the length of document since, taking the raw
corpus length will not give any good results because it contains text which is not useful at all and hence removed 
from token list.

##Top 50 bigrams by frequencies:
a) Ihaveusedbigram_with_filter()functiontoapplyvariousfilterfunctionstofinder.I have first applied Get_aplha_words() function 
to get only alphabetical words. Then further I have applied filter to remove stop words. At last I have applied filter to get words having minimum frequency 0f 2 since otherwise result will not be much helpful.
b) The scores are sorted in order of decreasing frequency.
c) The Result has given the top 50 bigrams by frequencies of meaningful important bigrams.

##Top 50 bigrams by their Mutual Information scores (using min frequency 5)
a) I have used the Top50bigrams_MutualInfoScore() function for this as well.
b) I have first removed the stop words and fetched only alphabetical words before
using the PMI measure.
c) Then,IhaverunPMIscorerwithaminimumfrequencybecauseitwillnotbeuseful
to apply the Mutual Information score to all the bigrams as results don’t really make sense and expressions are also very 
infrequent, because uniquely occurring pairs of words get high scores. Thus, it will be good to filter it, to make sense 
for very heavy documents.
d)PMI gives strange results when frequencies are very low e.g. 1-3 tokens, thus set
a minimum frequency for the collocates, which takes care of most of the problem.
e) The result has given me the bigram pairs which are frequent by their associativity.

##Comparison of results
#How are state_union_part1 and state_union_part2 similar or different in the use of the language, based on your results? Why?
Both the Text Files, state_union_part1 and state_union_part2 are similar in terms of the language. The reason behind this is, 
that they are written by the same author and thus have the similar writing style and kinds of words used are also similar. 
Also, the author has used same words in both files in writing the speeches. The Top-50 frequency words are also giving 
quite similar results for both the documents.
This is the reason, I have filtered the tokens of both the files in same manner because, both the files are written by 
James Linden. The only difference is the speeches and their delivered time.

#Are there any problems with the word or bigram lists that you found? Could you get a better list of bigrams?
I found some words which have multiple ‘*’ as a prefix or suffix in tokens of both the documents. Such words don’t appear 
in the Top-50 bigram, as they are few. As per my analysis, Bigram’s list currently contains important pair of words but however they can be improved on further filtering like we can change minimum frequency and then check the results and decide accordingly.

#How are the top 50 bigrams by frequency different from the top 50 bigrams scored by Mutual Information?
For both the documents, Part1 and Part2, Top-50 bigrams and Top-50 bigrams scored by Mutual Information are different due 
to following reasons:
i) The bigrams which I got from bigram_with_filter() function, has words which are important and meaningful for analysis. 
I have applied minimum frequency of 2 as a filter to remove low frequency words whereas minimum frequency is 5 in case of 
bigrams by mutual information scores.The above tokens are used together in speeches many a times which means and thus, 
they are high in frequency.
ii) The bigrams which I got from Top50bigrams_MutualInfoScore() function are different and not that useful because 
they are not common words and are of low frequency. Also, they give poor result when frequency is low (0-2) and that’s 
because I have applied frequency filter 5.
The results given by the top 50 bigrams scored by Mutual Information, are highly associative but not useful in terms of 
analysis.
iii) Mutual Information score cannot be applied to all the bigrams(unfiltered), because the results don’t really make 
sense, since uniquely occurring pairs of words get high scores. Whereas, Bigrams can be applied to filtered or unfiltered 
words.
