import splitPara as sp
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='a79238a0-5e8d-4b5b-8101-825adeff273e',
  password='UmI06x7q7AYk',
  version='2017-02-27')


res = sp.getPlacesDict()
#print(res.keys())
#print(res.values())


pos = []
neg = []
neu = []

user = {}
user_f = {}
place_final={}
for k,v in res.items():
	place_final[k] = []
	eff_per_rev = 0
	user_f[k]=[]
	for split in v:       #split is per user review(list of sentences)
		print(split)
		pos = []
		neg = []
		neu = []
		pos_scr = []
		neg_scr = []
		
		neu_scr = []
		user[k] = []
		
		for line in split:
			try:
				if line!=" " and line !="." and line != "!" and line != "":
					print(line)
					response = natural_language_understanding.analyze(
					  text=line,
					  features=Features(
					    keywords=KeywordsOptions(
					      sentiment=True,
					      emotion=True,
					      limit=2)))

			

					#resp=json.dumps(response, indent=2)
					#print(resp)


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
				if len(pos_scr)==0 :
					poav = 0
				else :
					poav = sum(pos_scr)/len(pos_scr)
				if len(neg_scr)==0 :
					negav = 0
				#pos = [int(i) for i in pos]
				#neg = [int(j) for j in neg]
				#print(sum(neg))
				else:
					negav = sum(neg_scr)/len(neg_scr)
				eff_per_rev = poav + negav
			except:
				pass
			user[k].append([pos,neg,neu,pos_scr,neg_scr,neu_scr])
			user_f[k].append(eff_per_rev)
					

		#print(user_f)
	if len(user_f[k]) == 0 :
		place_final[k] = 0
	else:
		place_final[k] = sum(user_f[k])/len(user_f[k])			
print("*****************************************************************************************")			
print(place_final)
print("*****************************************************************************************")			
print(user_f)
print("*****************************************************************************************")			
print(user)
print("*****************************************************************************************")			




				







				#print(json.dumps(response, indent=2))
