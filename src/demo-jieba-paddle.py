# encoding=utf-8
import jieba

# 啟動 paddle 模式，0.40 版本之後開始支持，早期版本不支持
# 需注意 paddlepaddle-tiny 1.6.1 版本僅支援到 python 3.6 版本，若用更高的 python 環境安裝將會失敗
jieba.enable_paddle()
strs=["我來到新竹清華大學","乒乓球拍賣完了","我考進台灣科技大學資工所"]
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True)
    print("Paddle Mode: " + '/'.join(list(seg_list)))
