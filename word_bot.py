import telebot
import random,string
import itertools


bot=telebot.TeleBot("API key here")
global di,score,eng_word
eng_word = []
score=0
@bot.message_handler(commands=['start'])
def yoyo(message):
    reply="Hi,this bot is made mzm .Jmzm -- This  bot will play a game with u.\n\nIt will give u a word enter a word made from its characters your score is incremented,if you enter a wrong word GAME OVER\n\n For another word press /start\n\n if no words possible or no more words possiblle enter DONE"
    
    #this generates a random no -->length and 3<=length<5
    length=random.randint(3,5)
    # x is the generated string
    x=''.join(random.choice(string.ascii_lowercase) for i in range(length))
    reply+="\n\n So, ur word is "+x
    
    #This uses a file words.txt which has one word in one line  
    with open("\words.txt") as f:
        di = f.read().split('\n')   # '\n'--> one word in one line
    bot.reply_to(message,reply) 
    word = x
    words = itertools.permutations(word)
    words = set([''.join(i) for i in words])  #Generated all possible words

    for i in words:
        if i.lower() in di:
            print(i)       #will give u all possible words {Prints in console}
            eng_word.append(i)
    print(len(eng_word))





@bot.message_handler(func=lambda message:True)
def blab(message):
    global score
    ans=message.text
    if ans.upper()=="DONE":
        if len(eng_word)==score:
            bot.reply_to(message,"Great job     :)\nyour score is equal to the highest score possible\n\nwanna play  again press /start")
            score=0
        else:
            bot.reply_to(message, "Good try\n there are more words possible")
            score=0

    elif ans.lower() in eng_word:
        score+=1
        bot.reply_to(message,"Great,Go on...")
    else:
        msg="The entered word is not correct.\n Good try\n\n Your score  :"+str(score)+"\nTo play again press /start"
        score=0


        bot.reply_to(message,msg)


# This stops the program to end
bot.polling()









