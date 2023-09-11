from ckiptagger import WS, POS, NER
ws = WS("./data")
pos = POS("./data")
ner = NER("./data")
def get_ckiptagger_tokenization(text):
    ckip_tokenized = ws([text])
    return ' '.join(ckip_tokenized[0])
text1 = '''2003年沙士一役，港大新發病毒性疾病學講座教授管軼在廣州野味市場的果子狸身上，找到感染人類的沙士冠狀病毒，找到元兇遏止疫情擴散，成為沙士抗疫英雄。事隔17年，他本周二三（21、22日），與團隊到武漢考察，但找不到源頭，「源頭被銷毀得乾乾淨淨，這裏似乎不歡迎專家」，他對內地傳媒說，估計武漢感染規模大沙士十倍起跳，又說政府不作為，無奈做「逃兵」訂機票返港，感到極其無力。'''
text2 = '''農曆新年將至，又是逗利是的時候，打工仔也可望收到開工利是。滙豐連續第二年向本港員工派發電子利是，每位500元，將在員工下一個出糧日透過出糧戶口發放。滙豐香港區行政總裁施穎茵向香港員工發出電郵，宣布派發電子利是的消息。她於電郵內表示，十分感謝同事對公司及客戶無限的貢獻及投入，即使前景仍有不確定性，她有信心克服挑戰，今年再創繁榮。滙豐發言人回覆傳媒查詢時稱，滙豐希望藉著農曆新年，感謝各同事過去一年的努力。跟去年一樣，該行將會向每位香港員工派發500元的電子利是，在各同事下一個出糧日透過出糧戶口發放。'''
text3 = '''大阪、京都、奈良、神戶是親子遊的熱門路線，其實除了京阪神，從大阪玩到鳥取也是不錯選擇！官方早前推出鳥取1000円巴士優惠，由大阪難波往鳥取只需1000円，大阪Open Jaw玩鳥取一流，加上適逢鳥取紅楚蟹季開鑼，平食海產、鳥取和牛、21世紀梨……還有必去鳥取砂丘、鬼太郎商店街及小朋友最愛的柯南博物館等，大人小朋友都玩得滿足！'''
print (f'ckiptagger result: \n{get_ckiptagger_tokenization(text1)}')
print ('\n')
print (f'ckiptagger result: \n{get_ckiptagger_tokenization(text2)}')
print ('\n')
print (f'ckiptagger result: \n{get_ckiptagger_tokenization(text3)}')
print ('\n')
tokenized_result = ws([text3])
pos_result = pos(tokenized_result)
entity_result = ner(tokenized_result, pos_result)
print (entity_result)
