import random
print("---------------------------------------------------HANGMAN---------------------------------------------------")
print("*************************************************************************************************************")
print("----------------------------------------------------Rules----------------------------------------------------")
print("You have to choose any content from the given list and a related word will be randomly asked.")
print("You have to guess the word correctly in given number of chances.")
print("*************************************************************************************************************")
print("Let's start playing!")
contents={1:['cat','frog','sheep','snake','turtle','rabbit','crocodile','giraffe','cow','horse','pig','penguin','tiger','duck','bat','fox','elephant','monkey','dog','donkey','zebra','deer','kangaroo'],
2:['cricket','basketball','baseball','badminton','soccer','cycling','weightlifting','football','hockey','archery','volleyball','golf','javelin','tennis','running','surfing','darts','longjump','skiing'],
3:['bike','car','scooter','boat','van','rocket','bus','truck','ambulance','plane','train','helicopter','tractor','motorbike','auto'],
4:['policeman','nurse','mechanic','doctor','artist','pilot','driver','carpenter','scientist','reporter','teacher','farmer','electrician','builder','engineer','chef','pharmacist','soldier','plumber'],
5:['sun','rainbow','river','volcano','moon','flower','snow','bush','planet','rain','clouds','mountain','forest','cliffs','tree','leaf','desert','lake','wind','stars','island','tornado','earth'],
6:['violin','keyboard','saxophone','trumpet','clarinet','piano','drums','guitar','accordion','tambourine','harp','harmonica','banjo'],
7:['apartment','bridge','theatre','garage','petstore','hospital','skyscrapers','church','castle','airport','tunnel','stadium','factory','zoo','house','lighthouse'],
8:['red','yellow','black','orange','purple','blue','green','white','grey','brown'],
9:['india','america','australia','canada','ireland','southafrica','france','england','spain','thailand','egypt','china','italy','turkey','argentina','russia','germany','japan','brazil','mexico'],
10:['candle','magnet','satchel','dice','padlock','letter','microscope','balloon','briefcase','globe','can','sword','coins','box','luggage','axe','bolt','ball','drone','medal','shield']}
while(True):
	print("Choose any topic from the given list:")
	print("1.Animals\t2.Sports\t3.Transport\t4.Jobs\t\t5.Nature\n6.Music\t\t7.Buildings\t8.Colors\t9.Countries\t10.Things")
	ch=int(input("Enter a number of your choice: "))
	try:
		l=contents[ch]
	except:
		print("Please enter valid choice:")
		continue
	word=random.choice(l)
	lw=len(word)
	lives=lw-1
	print("You have",lives,"lives to guess the correct word. Each incorrect guess will decrease one life.")
	sec='_'*lw
	g=[]       #to store the list of already guessed characters
	while(lives!=0):
		for s in sec:
			print(s, end=" ")
		w=list(word)
		guess=(input("\nGuess a letter: ")).lower()
		if guess in g:
			print("You have already guessed the letter. Try something else!")
			continue
		g.append(guess)
		if guess in word:
			for i in range(len(w)):
				if(w[i]==guess):
					pos=i
					s1=list(sec)
					s1[pos]=guess
					sec="".join(s1)
			if(sec.find('_')==-1):
				print("\nYou guessed the correct word!")
				break
		else:
			lives-=1
			if(lives!=0):
				print("You have {0} lives left, try again!".format(lives))
			else:
				print("You lost!")
				print("The correct word is: ",word)
	print("\n1.Play again\t\t2.Quit")
	pa=int(input("-->"))
	if pa!=1:
		break