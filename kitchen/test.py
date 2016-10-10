from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from stop_words import get_stop_words
import re

text_neg_path = 'E:\\dataset\\domain_sentiment_data_rating\\sorted_data_acl\\kitchen\\review_text_neg'
text_pos_path = 'E:\\dataset\\domain_sentiment_data_rating\\sorted_data_acl\\kitchen\\review_text_pos'
stop_words_path = 'E:\\dataset\\en_stop_word'


en_stop = get_stop_words('english')
with open(stop_words_path, 'r') as stop_words_file:
    for line in stop_words_file:
        line = line.strip()
        en_stop.append(line)
en_stop.append('_the')
# print(en_stop)


def remv_stop_words(line):
    line = re.sub(r'([\d])', '', line)
    line_low = line.lower()
    tokens = word_tokenize(line_low)
    # print(tokens[:10])
    remv_stop_tokens = [i for i in tokens if not i in en_stop]
    remv_stop_tokens = [i for i in remv_stop_tokens if not len(i) < 3]
    # print(remv_stop_tokens[:20])
    return remv_stop_tokens


def remvLowFreWords(corpora):
    wordNum = dict()
    for word in corpora:
        wordNum[word] = wordNum.get(word, 0) + 1
    low_wordNumList = []
    for word in wordNum.keys():
        if wordNum[word] < 11:
            low_wordNumList.append(word)
    print('总词数', len(wordNum))
    print('低频词数', len(low_wordNumList))
    return low_wordNumList


def get_corpus(path):
    corpus_all_x = []
    with open(path, 'r') as cor_file:
        for line in cor_file:
            # 对每一条评论进行预处理,得到的是列表
            lineTokens = remv_stop_words(line)
            # 预处理后的每一条评论添加到语料库列表中
            corpus_all_x = corpus_all_x + lineTokens
            # 预处理后的每一条评论添加到语料库列表中（列表的列表）
            corpus.append(lineTokens)

    return corpus, corpus_all_x


def get_corpus_after_process():
    # corpus 负向语料列表(1000个列表)，corpus_all_neg 负向语料列表（1000个元素）
    corpus, corpus_all_neg = get_corpus(text_neg_path)
    # corpus 所有语料列表(2000个列表)，corpus_all_pos 正向语料列表（1000个元素）
    corpus, corpus_all_pos = get_corpus(text_pos_path)
    # 所有语料（1个元素）
    corpus_all = corpus_all_neg + corpus_all_pos
    print(len(corpus))
    print(len(corpus_all))
    # 低频词列表
    low_wordNumList = remvLowFreWords(corpus_all)
    # 第一个for遍历语料列表中的所有评论（列表），第二个for遍历每条评论中的每个词
    for item in corpus:
        item_remv_low = []
        for word in item:
            # 不在低频词列表中的词
            if not word in low_wordNumList:
                item_remv_low.append(word)

        # 每一条评论的列表转换成字符串
        review = ','.join(item_remv_low).replace(',', ' ')
        # 每一条评论构成列表的一个元素
        corpus_after_process.append(review)
    print(pos_tag(item_remv_low))
    print(corpus_after_process[1001])
    # print(pos_tag(corpus_after_process[1001]))


corpus = []
corpus_after_process = []
get_corpus_after_process()
