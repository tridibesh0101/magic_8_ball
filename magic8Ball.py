import random 
def getAnswer(answerNumber):
	if answerNumber==1:
		return "It's certain"
	elif answerNumber==2:
		return "It is decidedly so"
	elif answerNumber==3:
		return "Yes"
	elif answerNumber==4:
		return "reply hazy turn again"
	elif answerNumber==5:
		return "ask again later"
	elif answerNumber==6:
		return "concentrate and ask again"
	elif answerNumber==7:
		return "my reply is no"
	elif answerNumber==8:
		return "outlook is not so good"
	elif answerNumber==9:
		return "Are you crazy?"
	
r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)
