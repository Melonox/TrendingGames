 #-*- coding: utf-8 -*-
from random import *
import tkinter
import tkinter.font as font
from tkinter import Canvas 
import tkinter.messagebox


def decks():
  Deck = []
  i = 0
  while i < 4:
    if i == 0:
      z = "Hearts"
    elif i == 1:
      z = "Spades"
    elif i == 2:
      z = "Clubs"
    else:
      z = "Diamonds"
    for num in range(1, 14):
      if num == 11:
        Deck.append(["Jack", z])
      elif num == 12:
        Deck.append(["Queen", z])
      elif num == 13:
        Deck.append(["King", z])
      elif num == 1:
        Deck.append(["Ace", z])
      else:
        Deck.append([num, z])
    i += 1
  return Deck

def shuffle():
  new_deck = []
  DECK = decks()
  for i in range(1, 53):
    sh = randint(0, 52-i)
    new_deck.append(DECK[sh])
    DECK.remove(DECK[sh])
  return(new_deck)

def blackjack(hand_pl):
  if hand_pl[1][0] == "King" and hand_pl[0][0] == "Ace":
    return True
  if hand_pl[1][0] == "Queen" and hand_pl[0][0] == "Ace":
    return True
  if hand_pl[1][0] == "Jack" and hand_pl[0][0] == "Ace":
    return True
  if hand_pl[1][0] == 10 and hand_pl[0][0] == "Ace":
    return True
  if hand_pl[0][0] == "King" and hand_pl[1][0] == "Ace":
    return True
  if hand_pl[0][0] == "Queen" and hand_pl[1][0] == "Ace":
    return True
  if hand_pl[0][0] == "Jack" and hand_pl[1][0] == "Ace":
    return True
  if hand_pl[0][0] == 10 and hand_pl[1][0] == "Ace":
    return True
  return False

def convert(strng):
  if strng == "King":
    return 10
  elif strng == "Queen":
    return 10
  elif strng == "Jack":
    return 10
  else:
    return strng

def dealer(hand, d):  
  if hand[0][0] == hand[1][0]:
    hand.append(d[0])
    hand.append(d[1])
    d.remove(d[0])
    d.remove(d[1])
    for k in range(4): ## if the bot has split and all are aces, the dealer deserves to lose.
      if hand[k][0] == "Ace":
        hand[k][0] = 11
    hand_1 = convert(hand[0][0]) + convert(hand[2][0]) ##TypeError: 'int' object is not subscriptable
    hand_1_card = [hand[0], hand[2]]
    hand_2 = convert(hand[1][0]) + convert(hand[3][0])
    hand_2_card = [hand[1], hand[3]]
    X = 400
    Y = 200
    if hand_1 > hand_2 and hand_1 <= 21:
      cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
      cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
      return hand_1_card, d
    elif hand_2 > hand_1 and hand_2 <=21: 
      cards(hand_1_card[1][1], hand_1_card[1][0], X, Y)
      cards(hand_2_card[1][1], hand_2_card[1][0], X+200, Y)
      return hand_2_card, d
    elif hand_1 == hand_2:
      cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
      cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
      return hand_1_card, d
    elif hand_1 > 21:
      cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
      cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
      return hand_1_card, d
    else:
      cards(hand_1_card[1][1], hand_1_card[1][0], X, Y)
      cards(hand_2_card[1][1], hand_2_card[1][0], X+200, Y)
      return hand_2_card, d
  while True: 
    begin_hand = 0
    by_chance = randint(1,140)
    for i in range(len(hand)):
      if hand[i][0] == "Ace":
        if begin_hand < 11:
          hand[i][0] = 11
        else:
          hand[i][0] = 1
      begin_hand += convert(hand[i][0]) 
    if begin_hand >= 17:
      x = 0
      for every_card in range(len(hand)):
        if every_card % 3 == 0:
          cards(hand[every_card][1], hand[every_card][0], 400, 300+(100 * x * -1))
        elif every_card % 3 == 1:
          cards(hand[every_card][1], hand[every_card][0], 600, 300+(100 * x * -1))
        elif every_card % 3 == 2:
          cards(hand[every_card][1], hand[every_card][0], 800, 300+(100 * x * -1))
          x += 1
      return hand, d
    elif begin_hand == 16 and 0 < by_chance < 11: ### redo standard deviation?
      hand.append(d[0])
      d.remove(d[0])
    elif begin_hand == 15 and 0 < by_chance < 35:
      hand.append(d[0])
      d.remove(d[0])
    elif begin_hand == 14 and 0 < by_chance < 60:
      hand.append(d[0])
      d.remove(d[0])
    elif begin_hand == 13 and 0 < by_chance < 85:
      hand.append(d[0])
      d.remove(d[0])
    elif begin_hand == 12 and 0 < by_chance < 100:
      hand.append(d[0])
      d.remove(d[0])
    elif begin_hand <= 11:
      hand.append(d[0])
      d.remove(d[0])
    else:
      x = 0
      for every_card in range(len(hand)):
        if every_card % 3 == 0:
          cards(hand[every_card][1], hand[every_card][0], 400, 300+(100 * x * -1))
        elif every_card % 3 == 1:
          cards(hand[every_card][1], hand[every_card][0], 600, 300+(100 * x * -1))
        elif every_card % 3 == 2:
          cards(hand[every_card][1], hand[every_card][0], 800, 300+(100 * x * -1))
          x += 1
      return hand, d

def split(hand, decK, X, Y):
  hand.append(decK[0])
  hand.append(decK[1])
  decK.remove(decK[0])
  decK.remove(decK[1])
  hand_1 = convertion(hand[0][0]) + convertion(hand[2][0]) ##TypeError: 'int' object is not subscriptable
  hand_1_card = [hand[0], hand[2]]
  hand_2 = convertion(hand[1][0]) + convertion(hand[3][0])
  hand_2_card = [hand[1], hand[3]]
  if hand_1 > hand_2 and hand_1 <= 21:
    cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
    cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
    return hand_1_card, decK
  elif hand_2 > hand_1 and hand_2 <=21: 
    cards(hand_1_card[1][1], hand_1_card[1][0], X, Y)
    cards(hand_2_card[1][1], hand_2_card[1][0], X+200, Y)
    return hand_2_card, decK
  elif hand_1 == hand_2:
      cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
      cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
      return hand_1_card, decK
  elif hand_1 > 21:
      cards(hand_2_card[1][1], hand_2_card[1][0], X, Y)
      cards(hand_1_card[1][1], hand_1_card[1][0], X+200, Y)
      return hand_1_card, decK
  else:
      cards(hand_1_card[1][1], hand_1_card[1][0], X, Y)
      cards(hand_2_card[1][1], hand_2_card[1][0], X+200, Y)
      return hand_2_card, decK

def convertion(strng):
  if strng == "King":
    return 10
  elif strng == "Queen":
    return 10
  elif strng == "Jack":
    return 10
  else:
    if strng == "Ace":
      return ace_convertion()
    else:
      return strng


def ace_convertion(): ############
    while True: 
      valueACE = tkinter.messagebox.askyesno('prompt', "Do you want your ace to have a value of 1?")
      if valueACE == True:
        return 1
      if valueACE == False:
        return 11

window = tkinter.Tk()   
HEIGHT = 860
WIDTH = 1024
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()
c.configure(bg='forest green')

# code for button
buttonFont = font.Font(family='Helvetica', size=20, weight='bold')
button = tkinter.Button(c, text="QUIT", fg="red", command=quit, height = HEIGHT//125, width = WIDTH//100, font=buttonFont)
button.place(x = 890, y = 680)

def cov(face_card):
    if face_card == "King":
        return "K"
    if face_card == "Queen":
        return "Q"
    if face_card == "Jack":
        return "J"
    if face_card == "Ace":
        return "A"

def cards(suit, nums, X, Y):
    c.create_rectangle(X+75,Y+75, X-75,Y-75, fill="floral white")
    if type(nums) == str:
        letter = cov(nums)
    else:
        letter = str(nums)
    if suit == "Diamonds":
        c.create_text(X, Y, text=letter+"♦", fill="red")
    if suit == "Spades":
        c.create_text(X, Y, text=letter+"♠", fill="gray40")
    if suit == "Hearts":
        c.create_text(X, Y, text=letter+"♥", fill="red")
    if suit == "Clubs":
        c.create_text(X, Y, text=letter+"♣", fill="gray40")
    return [nums, suit]

def simulation():
    c.delete("all")
    kced = shuffle()
    centerx = 400
    centery = 400
    c.create_text(250, 250, text="Dealer's hand")
    c.create_text(250, 450, text="Your's hand")
    notbot = cards(kced[0][1], kced[0][0], centerx, centery+100), cards(kced[2][1], kced[2][0], centerx+200, centery+100)
    notbot_hand = [kced[0],kced[2]] 
    bot = cards(kced[1][1], kced[1][0], centerx, centery-100), cards(kced[3][1], kced[3][0], centerx+200, centery-100)
    bot_hand = [kced[1],kced[3]]
    reveal = c.create_rectangle(centerx+75,centery-25, centerx-75,centery-175, fill="gray64") ############################
    for j in range(4):
      kced.remove(kced[0])
    if blackjack(bot_hand) == True:
      tkinter.messagebox.showinfo("You lost.",  "Bot has blackjack, you automatically lose.")
      c.delete(reveal)
      return None
    if blackjack(notbot_hand) == True and blackjack(bot_hand) == False:
      tkinter.messagebox.showinfo("You Won.",  "You just won congrats.")
      c.delete(reveal)
      return None
    hit_counter = 0
    outcome, dek = dealer(bot_hand, kced)
    Dealer_result = 0
    for i in range(len(outcome)):
      Dealer_result += convert(outcome[i][0])
    cards_left = 0
    x = 0
    y = 0
    reveal = c.create_rectangle(centerx+75,centery-25, centerx-75,centery-175, fill="gray64")
    if notbot_hand[0][0] == notbot_hand[1][0]: 
      while y == 0:
        res = tkinter.messagebox.askyesno('Yes|No', 'Do you want to split your cards?')
        if res == True:
          notbot_hand, dek = split(notbot_hand, dek, centerx, centery+200)
          y = 1
          x = 1
        if res == False:
          y = 2
    ############################
    deltay = centery + 200
    while x == 0:
      for l in range(len(notbot_hand)):
        if notbot_hand[l][0] == "Ace":
          notbot_hand[l][0] = ace_convertion()
      a = tkinter.messagebox.askyesno('prompt', "Do you want an extra card?") 
      if a == True:
        notbot_hand.append(kced[0])
        if hit_counter % 3 == 0:
          cards(notbot_hand[-1][1], notbot_hand[-1][0], centerx, deltay)
        if hit_counter % 3 == 1:
          cards(notbot_hand[-1][1], notbot_hand[-1][0], (centerx + 200), deltay)
        if hit_counter % 3 == 2:
          cards(notbot_hand[-1][1], notbot_hand[-1][0], (centerx + 400), deltay)
          deltay += 100
        kced.remove(kced[0])
        hit_counter += 1
        cards_left += 1
      if a == False:
        x = 1
      if hit_counter >= 8: #if you're the luckiest mf that gets 4 aces and chooses all 1s, 4 twos, and 3 threes.
        x = 1
    result = 0
    if y == 0 or y == 2:
      for i in range(hit_counter+2):
        result += convertion(notbot_hand[i][0])
    if result > 21:
      c.delete(reveal) 
      tkinter.messagebox.showinfo("Game over! You lost.", "Game over! You lost.")
      return None
    if Dealer_result == 21  and result != 21:
      c.delete(reveal)
      tkinter.messagebox.showinfo("You lost! Dealer has 21", "You lost! Dealer has 21")
      return None
    if result == 21 and Dealer_result != 21:
      c.delete(reveal)
      tkinter.messagebox.showinfo("You win", "You win")
      return None
    if Dealer_result > result and Dealer_result < 21:
      c.delete(reveal)
      tkinter.messagebox.showinfo("You lose!", "You lose!")
      return None
    if Dealer_result == result:
      c.delete(reveal)
      tkinter.messagebox.showinfo("Tie.", "Tie.")
      return None
    if Dealer_result < result and result < 21:
      c.delete(reveal)
      tkinter.messagebox.showinfo("You win", "You win")
      return None
    if Dealer_result > 21:
      c.delete(reveal)
      tkinter.messagebox.showinfo("You win", "You win")
      return None


play = tkinter.Button(c, text="Play", command=simulation, height = HEIGHT//125, width = WIDTH//100, font=buttonFont)
play.place(x = 14, y = 680)

window.mainloop()


#def write_slogan():
    #print("Tkinter is easy to use!")

#slogan = tk.Button(c, text="Hello", command=write_slogan, height = HEIGHT//100, width = WIDTH//75)
#slogan.place(x = 760, y = 0)

#card function takes number/str and suit and returns that card as a printed one
#hit or stay / split as buttons
# play/ play again as a button
# something to represent deck shuffling, maybe a text on a deck of cards

#exit()
#python3 -i blackjacksim.py
