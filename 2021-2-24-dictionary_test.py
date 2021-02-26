from bert_serving.client import BertClient

bc = BertClient("wx.ringdata.net", port=15555, port_out=15556)
vectors = bc.encode(["1234"])
print(vectors)
