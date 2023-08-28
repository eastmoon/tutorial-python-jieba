# encoding=utf-8
import jieba

# 全模式
seg_list = jieba.cut("我來到新竹清華大學", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))

# 精確模式
seg_list = jieba.cut("我來到新竹清華大學", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# 若不設定默認精確模式
seg_list = jieba.cut("他來到台北松山文創園區")  # 默认是精确模式
print(", ".join(seg_list))

# 搜尋引擎模式
seg_list = jieba.cut_for_search("小明碩士畢業於中央科學研究院資工所，後在日本京都大學深造")
print(", ".join(seg_list))
