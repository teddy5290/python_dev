import jieba
from wordcloud import WordCloud,ImageColorGenerator
from collections import Counter
import matplotlib.pyplot as plt

# 讀取哈工大停用詞庫(已簡轉繁) 也塞了一下自定義過濾常用詞語
with open('cn_stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# 讀取文本文件
with open(r'test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用 jieba 進行中文分詞
wordlist = jieba.lcut(text)
word_freq = Counter(wordlist)
# 過濾掉單個字詞和常用詞語 長度>1 , 出現次數>5
filtered_words = [word for word in wordlist if len(word) > 1 and word not in stopwords and word_freq[word] > 5]

# 將過濾後的詞彙組合成一個字符串
text_after_jieba = ' '.join(filtered_words)

# 生成文字雲
wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\msjh.ttc',  # 設定字體路徑，適用於顯示中文
                      width=1600,
                      height=800,
                      background_color='white',
                      colormap="Set3").generate(text_after_jieba)

# 顯示文字雲
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
