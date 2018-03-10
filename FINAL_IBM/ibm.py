import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='a79238a0-5e8d-4b5b-8101-825adeff273e',
  password='UmI06x7q7AYk',
  version='2017-02-27')

response = natural_language_understanding.analyze(
  text="Must visit atleast once as it is the best place ever.There are lots of monkeys here which is dissapointing",
  features=Features(
    keywords=KeywordsOptions(
      sentiment=True,
      emotion=True,
      limit=2)))


pos = []
neg = []
neu = []
pos_scr = []
neg_scr = []
neu_scr = []

user = {}


resp=json.dumps(response, indent=2)
print(resp)


for i in response['keywords']:
	if i['sentiment']['label'] == "positive":
		pos.append(i['text'])
		pos_scr.append(i['sentiment']['score'])

	if i['sentiment']['label'] == "negative":
		neg.append(i['text'])
		neg_scr.append(i['sentiment']['score'])

	if i['sentiment']['label'] == "neutral":
		neu.append(i['text'])
		neu_scr.append(i['sentiment']['score'])


print(pos)
print(pos_scr)

print(neg)
print(neg_scr)

print(neu)
print(neu_scr)


