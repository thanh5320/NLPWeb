from pyvi import ViTokenizer,ViPosTagger
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def posstaggingVi(text):
    rs = ViPosTagger.postagging(ViTokenizer.tokenize(text))
    a = rs[0]
    b = rs[1]
    w = str(' ')
    for i in range(0, len(a)):
        w = w + a[i] + '-' + b[i] + ' '
    return w
def posstaggingEn(text):
    rs =pos_tag(word_tokenize(text))
    w = str('')
    for i in rs:
        if (i[1] != '.'):
            w = w + i[0]+'-'+i[1]+' '
        else: w = w + i[0]+' '
    return w
