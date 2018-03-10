import ast
import re
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


def getPlacesDict():

	#print("**********************FILE**********************:",file)
	fp = open("placesToSee.txt","r")
	data = fp.readlines()[0]
	dataDict = ast.literal_eval(data)
	dataValues = [vals for vals in dataDict.values()]

	for key,value in dataDict.items():
		#print("**********************KEY**********************:",key)
		temp = []
		for review in value:
			res = split_into_sentences(review)
			temp.append(res)
		dataDict[key]=temp
	
	return(dataDict) #key is place ID, value will be a list of lists, where each inner list will be a set of strings seperated from the para.

def getRestDict():
	files = ['rajajiRest.txt','royalRest.txt','forumRest.txt']
	d1={}
	d2={}
	d3={}
	#print("**********************FILE**********************:",file)

	fp = open("rajajiRest.txt","r")
	data = fp.readlines()[0]
	dataDict = ast.literal_eval(data)
	dataValues = [vals for vals in dataDict.values()]

	for key,value in dataDict.items():
		#print("**********************KEY**********************:",key)
		temp = []
		for review in value:
			res = split_into_sentences(review)
			temp.append(res)
		dataDict[key]=temp
	d1=dataDict
	
	fp = open("royalRest.txt","r")
	data = fp.readlines()[0]
	dataDict = ast.literal_eval(data)
	dataValues = [vals for vals in dataDict.values()]

	for key,value in dataDict.items():
		#print("**********************KEY**********************:",key)
		temp = []
		for review in value:
			res = split_into_sentences(review)
			temp.append(res)
		dataDict[key]=temp
	d2=dataDict

	fp = open("forumRest.txt","r")
	data = fp.readlines()[0]
	dataDict = ast.literal_eval(data)
	dataValues = [vals for vals in dataDict.values()]
	
	for key,value in dataDict.items():
		#print("**********************KEY**********************:",key)
		temp = []
		for review in value:
			res = split_into_sentences(review)
			temp.append(res)
		dataDict[key]=temp
	d3=dataDict
	res={**d1,**d2,**d3}
	return(res) #key is place ID, value will be a list of lists, where each inner list will be a set of strings seperated from the para.
	
