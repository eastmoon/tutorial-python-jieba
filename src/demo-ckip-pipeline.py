from ckipnlp.pipeline import CkipPipeline, CkipDocument

pipeline = CkipPipeline()
doc = CkipDocument(raw='中文字耶，啊哈哈哈')

# Word Segmentation
print("----- Word Segmentation -----")
pipeline.get_ws(doc)
print(doc.ws)
for line in doc.ws:
    print(line.to_text())

# Part-of-Speech Tagging
print("----- Part-of-Speech Tagging -----")
pipeline.get_pos(doc)
print(doc.pos)
for line in doc.pos:
    print(line.to_text())

# Named-Entity Recognition
print("----- Named-Entity Recognition -----")
pipeline.get_ner(doc)
print(doc.ner)

################################################################

from ckipnlp.container.util.wspos import WsPosParagraph

# Word Segmentation & Part-of-Speech Tagging
print("----- Word Segmentation & Part-of-Speech -----")
for line in WsPosParagraph.to_text(doc.ws, doc.pos):
    print(line)
