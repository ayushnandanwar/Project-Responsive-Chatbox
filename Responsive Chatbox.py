#!/usr/bin/env python
# coding: utf-8

# In[1]:



# Responsive Chat box
# Game: guess number and stone paper scissor and magic, dream 11
# joke, story, calculator, question 
# commands: slap, whatsapp number msg,  
# open- whatsapp, insta, facebook, linkedin, github, twitter, google, etc. 
# conversation commands: Hi or hello 
# more commands: question me
# jokes, story, question ,player
# chatbox


'''
Problem Statement: Make a responsive chatbox in which user will give some command to bot and bot will respond.

Project Members:-

        Ayush Nandanwar(860)
        Prathamesh Pawar(866)


'''

  
import random
import time
import webbrowser

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def guess_number():     # guess the number game definition  # command: pls guess
    N=random.randint(1,20)    # getting random number 
    print("bot: Welcome to the guessing number Game")
    print("     You have 5 chances to guess the correct number")
    print("     Guess the number between 1 to 20")
    print("     or you can enter end to exit from the game\n")
    chance=5    
    time_you_guess=0    
    while 1:         # game loop begins
        print("       Chance left:",chance)
        N1=input("You: ")     # getting user input
        try:
            N1=int(N1)    # Error handling   if user type any strig value
        except:
            
            if N1=='end':     
              print("bot: You ended the game")    # game will stop here if user type end
              break                               
            else:
              print("bot: Please enter valid number🙂\n")  
              continue
        if N1==N:
            time_you_guess+=1   # incrementing user attempts
            print("\nbot: Congratulations🎉🎉🎊🎊, you guess correct number",N,"in",time_you_guess,"guesses")
            
            break    # user win and game end here
        elif N1<N:
            print("bot: Haha, wrong guess")
            print("     Too low\n")
            chance-=1
            time_you_guess+=1     # incrementing user attempts
        elif N1>N:
            print("bot: Haha, wrong guess")
            print("     Too High\n")
            chance-=1
            time_you_guess+=1     # incrementing user attempts
        if chance==0:
            print("bot: Unlucky, Game over🤣😂")
            print("     Better luck next time")
            print("     the correct number was",N)
            break    # user lose and game end here

def magic_game():   # magic game definition # command: magic
    print("bot: so now we are going to play an interesting game so just follow the instruction")
    time.sleep(5)
    print("bot: now guess any number bet 0 to 30")
    time.sleep(5)
    print("bot: now multiply that number with 2")
    time.sleep(5)
    x=random.randint(0,20)
    print("bot: now add",x)
    time.sleep(5)
    print("bot: Now divide the number by 2")
    time.sleep(3)
    print("bot: Subtract the number that you guessed at start")
    time.sleep(3)
    y=x/2
    print("bot: The number you have now is",y)  

def sps_game():   # stone, paper, scissor game  # command: pls sps
  possibility=['stone','paper','scissor']   # list of possibility
  bot_choice=random.choice(possibility)     # getting random choice for bot
  print("bot: Welcome to stone, paper and scissor game")
  print("     You have three choice: stone, paper and scissor")
  while 1:
    print("\n     Enter your choice")
    user_choice=input("You: ")    # taking user choice as input
    if user_choice=='stone' or user_choice=='paper' or user_choice=='scissor':   # checking user input is valid or not
      if user_choice==bot_choice:   # for draw
        print("bot:",bot_choice)
        print("       Draw😕")
        print("       see you next time")
        break
      elif user_choice=='stone' and bot_choice=='paper' or user_choice=='paper' and bot_choice=='scissor' or user_choice=='scissor' and bot_choice=='stone':
        print("bot:",bot_choice)     # all possiblility for user lose
        print("bot: LOL, You lose the game😂")
        break
      else:   # if above fails, ofcourse user win
        print("bot:",bot_choice)
        print("bot: Congrats, You won the game🙂")
        break
    else:
      print("bot: Please enter valid choice carefully!")   # if user enter invalid choice
      continue    # continue from while loop

def whatsapp(cmd):   # Whatsapp message sender # command: whatsapp (number) (message)
    number=cmd.split(' ')[1]    # extracting number                          # [optional]
    try:
        number=int(number)    # checking number is valid or not
        if len(str(number))==10:  # checking digits of number
               if len(cmd.split(' '))>2:  # checking whether user given any message to send
               
                    msg=cmd[19:]   # Extracting message
                    url="https://wa.me/91"+str(number)+'?text='+msg  # creating link url 
                    print("bot: Opening whatsapp....")
                    time.sleep(2)
                    webbrowser.open(url,new=1)  # opeining whatsapp
               else:
                    url="https://wa.me/91"+str(number)  # creatin link url
                    print("bot: Opening whatsapp....")
                    time.sleep(2)
                    webbrowser.open(url,new=1)  # opeining whatapp 
        else:
               print("bot: Invalid number")   # if number is invalid
               print("     Please Enter valid number")
    except:
        print("bot: invalid number")
        print("     Please Enter valid number")

def open_links(cmd):  # open links/social # command: open (social app name)
  what=cmd.split(' ')[1]  # getting what to open
  if what == 'whatsapp':   # whatsapp
    print("bot: Opening whatsapp...")
    time.sleep(2)
    webbrowser.open('https://wa.me/',new=1)
  elif what == 'instagram':  # instagram
    print("bot: Opening instagram...")
    time.sleep(1)
    webbrowser.open('https://www.instagram.com/',new=1)
  elif what == 'facebook':   # facebook
    print("bot: Opening facebook...")
    time.sleep(1)
    webbrowser.open('https://www.facebook.com/',new=1)
  elif what=='linkedin':    # linkedin
    print("bot: Openign linkedin...")
    time.sleep(1)
    webbrowser.open('https://www.linkedin.com/',new=1)
  elif what=='twitter':    # twitter
    print("bot: Opening twitter...")
    time.sleep(1)
    webbrowser.open('https://www.twitter.com/',new=1)
  elif what=='google':    # google
    print("bot: Opening google...")
    time.sleep(1)
    webbrowser.open('https://www.google.com/',new=1)
  elif what=='github':    # github
    print("bot: Opening github...")
    time.sleep(1)
    webbrowser.open('https://www.github.com/',new=1)
  else:
    print("bot: invalid !!!")
    print("     please enter valid link")

def jokes():  # jokes # command: pls joke
  joke_number=random.randint(1,7)   # random joke selecting
  if joke_number==1:
    print("bot: What is the best thing for switzerland?")
    time.sleep(1)
    print("      I don't know, but the flag is a big plus")
  elif joke_number==2:
    print("bot: Why do we tell actors to “break a leg?")
    print("       Why do we tell actors to “break a leg?")
  elif joke_number==3:
    print("bot:  Hear about the new restaurant called Karma?")
    print("         There’s no menu: You get what you deserve.")
  elif joke_number==4:
    print("bot : Why don’t scientists trust atoms?")
    print("        Because they make up everything.")
  elif joke_number==5:
    print("bot : Where are average things manufactured?")
    print("        The satisfactory.")
  elif joke_number==6:
    print("bot : What kind of exercise do lazy people do?")
    print("        Diddly-squats.")
  elif joke_number==7:
    print("bot : Why should the number 288 never be mentioned?")
    print("        It’s two gross.")
  
 # https://shortstorylines.com/very-short-stories-with-morals/

def story():      # story  # command: tell story                           
  story_number=random.randint(1,4)  # random story selecting
  if story_number==1:
    print("bot: 1. The Lion and the Rabbit\n")
    print("       Once there was a Lion in the jungle who used to kill 2-3 animals daily for his meal. All animals went to him to tell,") 
    print("       that daily one of them will come to him for his meal.")
    print("       So, the Lion agreed and this started going for many days. One day, it was Rabbit’s turn. When he was on his way he saw a well.")
    print("       Now he plans to kill the lion and save himself. He went to the lion and told him that, there is another lion who claims to be more powerful than him.")
    print("       Then the lion asks the rabbit to take him to that lion. The rabbit takes him to the well and said he lives here.") 
    print("       When the lion looked in the well he saw his own reflection and jumped in the well and dies.")
    print("\n       Moral: Wisdom wins might.")
   

  elif story_number==2:
    print("bot : 2. The Hunter and the Pigeo2.")
    print("        One day a hunter sets a net to catch birds and placed grains and rice over the net.")
    print("        After some time a flock of pigeons comes by and start eating grains and get caught in the net.")      
    print("        After some time they started losing hope, then their leader asks them to fly together up in the sky. ")
    print("        They did as they were told and carried the net away.")
    print("        The hunter runs after them but they flew away to their friend’s mouse hole. Then the mouse cuts the net and freed the pigeons")
  elif story_number==3:
    print("bot : 3. Two friends and the Bear")
    print("         Once there were two friends who were crossing the jungle. After some time they saw a bear coming towards them.")
    print("         Then, one of the friends quickly climbed the nearby tree and the other one did not know how to climb the tree.  ")
    print("         So he lays down on the ground holding his breath.")
    print("         The bear reaches near him and sniffs him in the ear. After some time bear left the place, thinking the man is dead.")
    print("         Now the other friend climbs down and asked his friend, what did bear said to him in his ear? He replied,” to be safe from the fake friends.”")
  elif story_number==4:
    print("bot: 4. The Crow and the Peacock – Who is Happy?")
    print("       Once there was a crow who wishes to be colorful and beautiful like other birds. He then went to the parrot and shared his thoughts. ")
    print("       But parrot said peacock is most beautiful bird so talk to him. Then the crow went to the peacock and told him about his looks. ")
    print("       Then the peacock replied,” You are the luckiest bird that has been never caged in life and we because of our beauty stay caged, and you are always free.")
    print("       After listening to this, crow realized his mistake and thanked God for making him like this and he flew away happily. ")
    
def question():  # Question # command: question me
  question_number=random.randint(1,4)  # random question selecting
  correct=False    # correct defining as false
  corrct_choice='NULL'
  ans='NULL'
  if question_number==1:
    print("bot: Question: Who is the PM of India?")
    print("     a) Narendra Modi")
    print("     b) Kejriwal")
    print("     c) Uddavh Thakrey")
    print("     d) Rahul gandhi")
    corrct_choice='a'   # allocating correct choice and ans
    ans='a) Narendra Modi'
   
  elif question_number==2:
    print("bot: The country that has the highest in Barley Production?")
    print("      a) China ")
    print("      b) India")
    print("      c) Russia")
    print("      d) France")
    corrct_choice='c'
    ans='c) Russia'

  elif question_number==3:
    print("bot: The hottest planet in the solar system?")
    print("      a) Mercury ")
    print("      b) Venus")
    print("      c) Mars")
    print("      d) Jupiter")
    corrct_choice='b'
    ans='b) Venus'
  elif question_number==4:
    print("bot : Which of the following is not a nuclear power center?")
    print("      a) Narora")
    print("      b) Kota")
    print("      c) Chamera")
    print("      d) Kakrapara")
    corrct_choice='c'
    ans='c) Chamera'
  
  # above are the questions with answer

  while 1:    # while loop is for getting inputs/choice
    print("\n     Enter your choice:")
    choice=input("you: ")   # taking user input
    if choice=='a' or choice=='b' or choice=='c' or choice=='d':  # checking input is valid or not
      if choice==corrct_choice:  # checking corrct option entered or not
        correct=True  # if corrct correct variable will be true
        break 
      else:
        break   # if not then correct will be ramain false
    else:
      print("bot: Enter valid choice")
      continue
  # while loop ends here

  if correct:    # if correct true
    print("bot: 🎉Well done! your answer is correct")
  else:
    print("bot: LOL, your answer is incorrect")
    print("     correct answer was",ans)

def search(cmd):  # search links in browser # command: search (url/any)
  print("bot: Searching",cmd[7:]+"...")  
  time.sleep(1)
  webbrowser.open(cmd[7:],new=1)  # searching and opening browser

def help():  # help definition # command: help
  print("bot: Game Commands:")
  print("          pls guess   -   guess the number game")
  print("          magic pls   -   magic game")
  print("          play dream11-   dream 11 game")
  print("          pls sps     -   stone, paper and scissor game")
  print("\n     More commands:")
  print("          pls joke    -   randomly jokes will show")
  print("          tell story  -   randomly story will show")
  print("          question me -   randomly bot will ask question")
  print("\n     Smart commands:   ")
  print("          whatsapp <number> <message>   - whatsapp will open with number (message is optional)")
  print("          open <social links/app>       - given link will open in app or browser")
  print("          search <url>                  - url will open in browser ( url may be any thing you want to search)")
  

def fact(num):
  if num == 0 or num==1:
    return 1
  else:
    return num * fact(num - 1) 

def calculator(cmd):  # calculator # commands: +, -, *, /  
    try:
        if '+' in cmd:
            num1 = cmd.split('+')[0]
            num2 = cmd.split('+')[1]
            print("bot:",int(num1)+int(num2))
        elif '-' in cmd:
            num1 = cmd.split('-')[0]
            num2 = cmd.split('-')[1]
            print("bot:",int(num1)-int(num2))
        elif '*' in cmd:
            num1 = cmd.split('*')[0]
            num2 = cmd.split('*')[1]
            print("bot:",int(num1)*int(num2))
        elif '/' in cmd:
            num1 = cmd.split('/')[0]
            num2 = cmd.split('/')[1]
            print("bot:",int(num1)/int(num2))
        elif '!' in cmd:
            num=cmd.split('!')[0]
            print("bot:",fact(int(num)))
        else:
            print("bot: sorry, I cannot do multiple operation at a time")
    except:
        print("bot: sorry, I cannot do multiple operation at a time")

def dream11(): # dream 11 game # command: play dream11
  players=['Virat Kohli','MS dhoni','Rohit Sharma', 'Mayank Agarwal',' Cheteshwar Pujara', 'Ajinkya Rahane' , 
           'Hanuma Vihari', 'Rishabh Pant', 'R. Ashwin', 'Ravindra Jadeja', 'Axar Patel', 'Jasprit Bumrah', 'Ishant Sharma', 
           'Mohammed Shami', 'Mohammad Siraj', 'Shardul Thakur', 'Umesh Yadav', 'KL Rahul', 'Wriddhiman Saha' , 'Abhimanyu Easwaran',
           'Prithvi Shaw', 'Suryakumar Yadav']  # player list defined
  strength=[]
  user_player_list=[]  # user player list user will add then
  print("bot: Welcome to dream 11 game")
  print("     make your 11 player cricket team")
  print("     Instruction: Enter np to see player")
  print("                  then nadd to add that player")
  print("                  or no to leave that player then np to see next player")
  print("                  enter show list see your current player list")
  print("                  Enter end to exit")
  team_=11  # 11 player cricket team
  while 1:
    
  
    if team_!=0:  # checking team is done or not
      random_player=random.choice(players)  # getting random player from list
      user_input=input("you: ")  # taking user input
      if user_input=='np': 
        print("bot: ",random_player)  # showing player
        add=input("you: ")   # taking input whether user want add player or not
        if add=='nadd':
          team_-=1
          user_player_list+=[random_player]  # adding player to user list
          players.remove(random_player)    # removing that player so, that player never select by bot randomly
          print("bot: player added in your list")
          print("      ",team_,"players is remaining to add")  # printing how many player remaining to add
        elif add=='no':
          print("bot: player not added")
          print("      ",team_,"players is remaining to add")
        else:
          print("bot: invalid input")
          print("      ",team_,"players is remaining to add")
      elif user_input=='end':       # if user type end 
        print("bot: You ended the dream11")
        break                       # game will end
      elif user_input=='show list':  # if show list type
        print("bot: your cricket player list:")
        print("      ",user_player_list)   # current added player will shown to user
        print("      ",team_,"players is remaining to add")
      else:
        print("bot: Please Enter np to proceed")
    else:  # if user completly selct all 11 player
      print("bot: Well done you have succesfully created 11 player cricket team")
      print("       your team members are")
      print("      ",user_player_list)
      break   # then game will end 
  
# chatbox starts
print("******** Welcome to Responsive Chatbox********\n")
print("bot: I'm your chatbot ")
print("     I can play games with you")
print("     If you want more help just type help!, ")
print("     If you want to exit, type Bye!")
invalid=0
flag=True

while flag:
  chat=input("you: ")
  if chat.lower()=='pls guess':
    guess_number()
  elif chat.lower()=='magic pls':
    magic_game()
  elif chat.lower()=='pls sps':
    sps_game()
  elif chat.lower()=='play dream11':
    dream11()
  elif chat.lower()=='pls joke':
    jokes()
  elif chat.lower()=='tell story':
    story()
  elif chat.lower()=='question me':
    question()
  elif chat.lower()=='help':
    help()
  elif chat[0:8].lower()=='whatsapp':
    whatsapp(chat)
  elif chat[0:4].lower()=='open':
    open_links(chat)
  elif chat[0:6].lower()=='search':
    search(chat)
  elif '/' in chat or '+' in chat or '-' in chat or '*' in chat or '!' in chat:
    calculator(chat)
  elif chat.lower()=='help':
    help()
  else:
    chat=chat.lower()
    if(chat!='bye'):
        if(chat=='thanks' or chat=='thank you' ):
            print("bot: You are welcome..")
            time.sleep(1)
        else:
            if(greeting(chat)!=None):
                print("bot: "+greeting(chat))
            else:
                print("bot: sorry, I didn't understand you!")
                print("      you can enter help")
    else:
        flag=False
        print("bot: Bye! take care..")
        time.sleep(2)

    

