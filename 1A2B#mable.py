import pygame,sys, pygame.font, pygame.event, pygame.draw, pygame.mixer, string
from pygame import*
from pygame.locals import*
from sys import exit
from random import random
from string import *
pygame.init()

screen=pygame.display.set_mode((395,545))
menu1=pygame.image.load("menu1.jpg").convert()
menu2pic=pygame.image.load("menu2.jpg").convert()
menu3=pygame.image.load("menu3.jpg").convert()
game=pygame.image.load("game.jpg").convert()
gameover=pygame.image.load("gameover.jpg").convert()
gameover2=pygame.image.load("gameover2.jpg").convert()
gameover3=pygame.image.load("gameover3.jpg").convert()
hhelp=pygame.image.load("help1.jpg").convert()
setdigit=pygame.image.load("setdigit.jpg").convert()
settarget=pygame.image.load("settarget.jpg").convert()
booom1=pygame.image.load("booom1.jpg").convert()
booom2=pygame.image.load("booom2.jpg").convert()
booom3=pygame.image.load("booom3.jpg").convert()
backbut=pygame.image.load("backbut.jpg").convert()
challengingbut=pygame.image.load("challengingbut.jpg").convert()
combut=pygame.image.load("combut.jpg").convert()
classicbut=pygame.image.load("classicbut.jpg").convert()
evilbut=pygame.image.load("evilbut.jpg").convert()
hhelp2=pygame.image.load("help2.jpg").convert()
helpbut=pygame.image.load("helpbut.jpg").convert()
nextbut=pygame.image.load("nextbut.jpg").convert()
startbut=pygame.image.load("startbut.jpg").convert()
ranking=pygame.image.load("ranking.jpg").convert()
rankback=pygame.image.load("rankback.jpg").convert()
getname=pygame.image.load("getname.jpg").convert()
click=pygame.mixer.Sound("click.wav")
explode=pygame.mixer.Sound("explode.wav")
keyerror=pygame.mixer.Sound("keyerror.wav")
mkeyin=pygame.mixer.Sound("keyin.wav")
wrong=pygame.mixer.Sound("wrong.wav")

pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.2)

screen.blit(menu1,(0,0))
pygame.display.update()
flag=1
state=0

def esc(x):
      v="esc"
      if x==v:
            exit()
            
##keyin
def get_key():
      while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                  return event.key
            else:
                  pass

def display_box(screen, message,place,size):
      #Print a message in a box in the middle of the screen
      fontobject = pygame.font.Font("LCDM2N__.TTF",size)
      if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (255,0,0)),place)
                                                                  #(135,207)
                                                                  #(83,242)
      pygame.display.flip()

def ask(screen, place,size):
      pygame.font.init()
      current_string = []
      display_box(screen,string.join(current_string,""), place,size)
      w=0
      while 1:
            inkey = get_key()
            if inkey == K_RETURN:
                  break
            elif inkey <= 127:
                  mkeyin.play()
                  current_string.append(chr(inkey))
            elif inkey==273:
                  click.play()
                  if 0<=w<(len(globalist)-11):
                        w+=1
                  else:
                        w=w
                  screen.blit(game,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i-w]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  pygame.display.update()
                  
            elif inkey==274:
                  mkeyin.play()
                  if 0<w<=(len(globalist)-11):
                        w-=1
                  else:
                        w=w
                  screen.blit(game,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i-w]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  pygame.display.update()                 
            
            display_box(screen,string.join(current_string,""),place,size)
      return string.join(current_string,"")

#add-pla
def keyin(pla):
      place=pla
      return ask(screen,'',place)

#Switching pages
def esct():
      global flag
      while flag==1:
            for event in pygame.event.get():
                  if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                              exit()
            flag+=1

def menu1():
      global flag
      while flag==2:
            for event in pygame.event.get():
                  if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                              exit()
                  if event.type==MOUSEBUTTONDOWN:
                        click.play()
                        screen.blit(menu2pic,(0,0))
                        pygame.display.update()
                        flag+=1
        
def menu2():
      global flag
      flag2=0
      while flag==3:
            a,b=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        #classic4
                        if 78<=a<=327 and 286<=b<=334:
                              click.play()
                              screen.blit(menu3,(0,0))
                              pygame.display.update()
                              flag+=1
                              classic_button()
                              flag2+=1
                        #challenging5
                        if 78<=a<=327 and 362<=b<=409:
                              click.play()
                              screen.blit(menu3,(0,0))
                              pygame.display.update()
                              flag+=2
                              challenging_button()
                              flag2+=1
                        #help6
                        if 240<=a<=363 and 482<=b<=518:
                              click.play()
                              screen.blit(hhelp,(0,0))
                              pygame.display.update()
                              flag+=3
                              help_button()
                              flag2+=1

                  area=0
                  a,b=pygame.mouse.get_pos()
                  if 78<=a<=327 and 286<=b<=334:
                        area=1
                  if 78<=a<=327 and 362<=b<=409:
                        area=2
                  if 240<=a<=363 and 482<=b<=518:
                        area=3
                  if area==0:
                        screen.blit(menu2pic,(0,0))
                        pygame.display.update()
                        area=0

                  while area!=0:
                        if area==1:
                              screen.blit(classicbut,(0,0))
                              pygame.display.update()
                              area=0
                        elif area==2:
                              screen.blit(challengingbut,(0,0))
                              pygame.display.update()
                              area=0
                        elif area==3:
                              screen.blit(helpbut,(0,0))
                              pygame.display.update()
                              area=0
                        else:
                              area=0
                                    
#classic
def classic_button():
      global flag
      while flag==4:
            c,d=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        #classiccomputer7
                        if 78<=c<=327 and 286<=d<=334:
                              click.play()
                              screen.blit(game,(0,0))
                              pygame.display.update()
                              flag+=3
                              classiccomputer()
                        #classicpersonal8
                        if 78<=c<=327 and 362<=d<=409:
                              click.play()
                              screen.blit(settarget,(0,0))
                              pygame.display.update()
                              flag+=4
                              classicpersonal()
                        #back to menu 2
                        if 240<=c<=363 and 482<=d<=518:
                              click.play()
                              screen.blit(menu2pic,(0,0))
                              pygame.display.update()
                              flag-=1
                              menu2()
            area=0
            if 78<=c<=327 and 286<=d<=334:
                  area=1
            if 78<=c<=327 and 362<=d<=409:
                  area=2
            if 240<=c<=363 and 482<=d<=518:
                  area=3
            if area==0:
                  screen.blit(menu3,(0,0))
                  pygame.display.update()
                  area=0

            while area!=0:
                  if area==1:
                        screen.blit(combut,(0,0))
                        pygame.display.update()
                        area=0
                  elif area==2:
                        screen.blit(evilbut,(0,0))
                        pygame.display.update()
                        area=0
                  elif area==3:
                        screen.blit(backbut,(0,0))
                        pygame.display.update()
                        area=0
                  else:
                        area=0
                        

#challenging
def challenging_button():
      global flag
      while flag==5:
            e,f=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        #challengingcomputer8
                        if 78<=e<=327 and 286<=f<=334:
                              click.play()
                              screen.blit(setdigit,(0,0))
                              pygame.display.update()
                              flag+=3
                              challengingcomputer()
                        #challengingpersona9
                        if 78<=e<=327 and 362<=f<=409:
                              click.play()
                              screen.blit(setdigit,(0,0))
                              pygame.display.update()
                              flag+=4
                              challengingpersonal()
                        #back to menu 2
                        if 240<=e<=363 and 482<=f<=518:
                              click.play()
                              screen.blit(menu2pic,(0,0))
                              pygame.display.update()
                              flag-=2
                              menu2()

            area=0
            if 78<=e<=327 and 286<=f<=334:
                  area=1
            if 78<=e<=327 and 362<=f<=409:
                  area=2
            if 240<=e<=363 and 482<=f<=518:
                  area=3
            if area==0:
                  screen.blit(menu3,(0,0))
                  pygame.display.update()
                  area=0

            while area!=0:
                  if area==1:
                        screen.blit(combut,(0,0))
                        pygame.display.update()
                        area=0
                  elif area==2:
                        screen.blit(evilbut,(0,0))
                        pygame.display.update()
                        area=0
                  elif area==3:
                        screen.blit(backbut,(0,0))
                        pygame.display.update()
                        area=0
                  else:
                        area=0

#help
def help_button():
      global flag
      while flag==6:
            g,h=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:

                        if 240<=g<=363 and 482<=h<=518:
                              click.play()
                              screen.blit(hhelp2,(0,0))
                              pygame.display.update()
                              flag+=4
                              help2()
                  area=0
                  if 240<=g<=363 and 482<=h<=518:
                        area=1
                  if area==0:
                        screen.blit(hhelp,(0,0))
                        pygame.display.update()
                        area=0

                  while area!=0:
                        if area==1:
                              screen.blit(nextbut,(0,0))
                              pygame.display.update()
                              area=0
                        else:
                              area=0
                        
def help2():
      global flag
      while flag==10:
            g,h=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        #back to menu 2
                        if 240<=g<=363 and 482<=h<=518:
                              click.play()
                              screen.blit(menu2pic,(0,0))
                              pygame.display.update()
                              flag-=7
                              menu2()
                  area=0
                  if 240<=g<=363 and 482<=h<=518:
                        area=1
                  if area==0:
                        screen.blit(hhelp2,(0,0))
                        pygame.display.update()
                        area=0

                  while area!=0:
                        if area==1:
                              screen.blit(startbut,(0,0))
                              pygame.display.update()
                              area=0
                        else:
                              area=0


#compare if every number is different
def compar(i):
      c=len(i)
      f=[]
      e=[]
      for j in range(c):
            f+=[i[j]]
      for x in range(c):
            for y in range(x+1,c):
                  if f[x]==f[y]:
                        e+=[2]
                  else:
                        e+=[3]
      if (2 in e)==True:
            return False
      else:
            return None
            
#create a random target
#check if it is ok
#what is ok
      #1.formed by different numbers
      #2.formed by enough digits
      
#add-h
def create(h):
      pretarget=random()
      midtarget=str(int(pretarget*(10**h)))
      l=len(midtarget)
      target=""
      if l!=h:
            midtarget=create(h)
      for i in range(0,h):
            target+=midtarget[i]
      if compar(target)!=None:
            target=create(h)
      return target

#check if the guess is ok
#add-h
def check(h):
      state=[]
      for i in range(len(guess)):
            if 48<=ord(guess[i])<=57:
                  state+=[1]
            else:
                  state+=[2]
      if len(guess)!=h:
            state+=[2]
      if compar(guess)!=None:
            state+=[2]
      if (2 in state)==True:
            return False

#change string into list
#add-h
def lislize(x,h):
      lis=[]
      for i in range(h):
            lis+=x[i]
      return lis

#calculate A
#add-h
def searc(h):
      checkc=[]
      for i in range(h):
            if lisg[i]==lisa[i]:
                  checkc+=[1]
      k=len(checkc)
      return k

def numA(h):
      A=searc(h)
      return A

#calculete B
def searb(h):
      checb=[]
      for i in range (h):
            t=(lisg[i] in lisa)
            if t==True:
                  checb+=[1]
      k=len(checb)
      return k

def numB(h):
      B=searb(h)-searc(h)
      return B

def checy(y,h):
      checy=[]
      if len(y)!=h:
            checy+=[2]
      if compar(y)==False:
            checy+=[2]
      if (2 in checy):
            return False
def chech(h):
      chech=[]
      h=int(h)
      if h<2 or h>9:
            chech+=[2]
      if (2 in chech):
            return False

#start
def main(y,h):
      global instep,che, place1,place2, target, guess, lisa, lisg, p, q, globalist, i, my_font
      guess=ask(screen,place1,35)
      esc(guess)
      while check(h)==False:
            screen.blit(game,(0,0))
            pygame.display.update()
            keyerror.play()
            guess=ask(screen,place1,35)
            esc(guess)
      lisa=lislize(y,h)
      lisg=lislize(guess,h)
      p=numA(h)
      q=numB(h)
      if p!=h:
            wrong.play()
            globalist+=["%s is %dA%dB!" %(guess,p,q)]
            screen.blit(game,(0,0))
            if len(globalist)<=11:
                  for i in range(len(globalist)):
                        pri=globalist[i]
                        prilist=my_font.render(pri,True,(255,0,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            else:
                  for i in range(11):
                        pri=globalist[-11+i]
                        prilist=my_font.render(pri,True,(255,0,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            instep+=1           
            pygame.display.update()
      else:
            globalist+=["Boooooooooooooooooooom"]
            globalist+=["the password is %s!" %(guess)]
            screen.blit(game,(0,0))
            if len(globalist)<=11:
                  for i in range(len(globalist)):
                        pri=globalist[i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            else:
                  for i in range(11):
                        pri=globalist[-11+i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))

            instep+=1            
            pygame.display.update()
            explode.play()
            for i in range(42):
                  if i%7==0:
                        screen.blit(booom1,(0,0))
                  elif i%7==1:
                        screen.blit(booom2,(0,0))
                  elif i%7==2:
                        screen.blit(booom3,(0,0))
                  elif i%7==3:
                        screen.blit(menu2pic,(0,0))
                  elif i%7==4:
                        screen.blit(booom1,(0,0))
                  elif i%7==5:
                        screen.blit(booom2,(0,0))
                  else:
                        screen.blit(booom3,(0,0))
                  pygame.display.update()
            
            screen.blit(gameover,(0,0))
            if len(globalist)<=11:
                  for i in range(len(globalist)):
                        pri=globalist[i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            else:
                  for i in range(11):
                        pri=globalist[-11+i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            pygame.display.update()
            
      while p!=h:
            wrong.play()
            guess=ask(screen,place1,35)
            if guess==v:
                  exit()
            while check(h)==False:
                  keyerror.play()
                  screen.blit(game,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  pygame.display.update()
                  guess=ask(screen,place1,35)
                  if guess==v:
                        exit()
            lisg=lislize(guess,h)
            p=numA(h)
            q=numB(h)
            if p!=h:
                  globalist+=["%s is %dA%dB!" %(guess,p,q)]
                  screen.blit(game,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i]
                              prilist=my_font.render(pri,True,(255,0,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i)) 
                  instep+=1
                  pygame.display.update()
            else:
                  globalist+=["Boooooooooooooooooooom"]
                  globalist+=["the password is %s!" %(guess)]
                  screen.blit(game,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))   
                  instep+=1
                  pygame.display.update()
                  explode.play()
                  for i in range(42):
                        if i%7==0:
                              screen.blit(booom1,(0,0))
                        elif i%7==1:
                              screen.blit(booom2,(0,0))
                        elif i%7==2:
                              screen.blit(booom3,(0,0))
                        elif i%7==3:
                              screen.blit(menu2pic,(0,0))
                        elif i%7==4:
                              screen.blit(booom1,(0,0))
                        elif i%7==5:
                              screen.blit(booom2,(0,0))
                        else:
                              screen.blit(booom3,(0,0))
                        pygame.display.update()

                  screen.blit(gameover,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  pygame.display.update()

def get_digit(nextone):
      global place1,place3, h, guess, lisa, lisg, p, q, globalist, i, my_font
      h=ask(screen,place3,40)
      while True:
            if h.isdigit():
                  h=h
                  break
      else:
            screen.blit(setdigit,(0,0))
            pygame.display.update()
            h=ask(screen,place3,40)
      
      if chech(h)==False:
            keyerror.play()
            screen.blit(setdigit,(0,0))
            pygame.display.update()
            h=ask(screen,place3,40)
            k=str(h)
            while chech(h)==False:
                  keyerror.play()
                  screen.blit(setdigit,(0,0))
                  pygame.display.update()
                  h=ask(screen,'',place3,40)
      h=int(h)
      screen.blit(nextone,(0,0))
      pygame.display.update
      return h

def get_target(h):
      global place1,place2, target, guess, lisa, lisg, p, q, globalist, i, my_font
      target=ask(screen,place2,40)
      y=target
      while True:
            if y.isdigit():
                  break
            else:
                  screen.blit(settarget,(0,0))
                  pygame.display.update()
                  y=ask(screen,place2,40)
      if checy(y,h)==False:
            keyerror.play()
            screen.blit(settarget,(0,0))
            pygame.display.update()
            y=ask(screen,place2,40)
            k=str(y)
            while checy(y,h)==False:
                  keyerror.play()
                  screen.blit(settarget,(0,0))
                  pygame.display.update()
                  y=ask(screen,place2,40)
                  esc(y)
      screen.blit(game,(0,0))
      pygame.display.update
      return y
      
def classiccomputer():
      global mode, place1,place2,place3, target, h, guess, lisa, lisg, p, q, globalist, i, my_font
      h=4
      target=create(4)
      y=target
      main(y,h)
      mode=1

def classicpersonal():
      global mode, place1,place2,place3, target, h, guess, lisa, lisg, p, q, globalist, i, my_font
      h=4
      target=get_target(4)
      y=target
      main(y,h)
      mode=2

def challengingcomputer():
      global mode, place1,place2,place3, target, h, guess, lisa, lisg, p, q, globalist, i, my_font
      nextone=game
      h=get_digit(nextone)
      target=create(h)
      y=target
      main(y,h)
      mode=2
           
def challengingpersonal():
      global mode, place1,place2,place3, target, h, guess, lisa, lisg, p, q, globalist, i, my_font
      nextone=settarget
      h=get_digit(nextone)
      target=get_target(h)
      y=target
      main(y,h)
      mode=2

def gameoverfunc():
      global flag
      while flag==2:
            m,n=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                              exit()
                  if event.type==MOUSEBUTTONDOWN:
                        if 239<=m<=362 and 138<=n<=174:
                              click.play()
                              screen.blit(ranking,(0,0))
                              pygame.display.update()
                              flag+=9
                              rankbut()
                        else:
                              screen.blit(menu2pic,(0,0))
                              pygame.display.update()
                              flag+=1

                  area=0
                  m,n=pygame.mouse.get_pos()
                  if 239<=m<=362 and 138<=n<=174:
                        area=1
                  if area==0:
                        screen.blit(gameover,(0,0))
                        if len(globalist)<=11:
                              for i in range(len(globalist)):
                                    pri=globalist[i]
                                    prilist=my_font.render(pri,True,(0,255,0))
                                    textrect=prilist.get_rect()
                                    screen.blit(prilist,(38,203+30*i))
                        else:
                              for i in range(11):
                                    pri=globalist[-11+i]
                                    prilist=my_font.render(pri,True,(0,255,0))
                                    textrect=prilist.get_rect()
                                    screen.blit(prilist,(38,203+30*i))
                        pygame.display.update()

                  while area!=0:
                        if area==1:
                              screen.blit(gameover2,(0,0))
                              if len(globalist)<=11:
                                    for i in range(len(globalist)):
                                          pri=globalist[i]
                                          prilist=my_font.render(pri,True,(0,255,0))
                                          textrect=prilist.get_rect()
                                          screen.blit(prilist,(38,203+30*i))
                              else:
                                    for i in range(11):
                                          pri=globalist[-11+i]
                                          prilist=my_font.render(pri,True,(0,255,0))
                                          textrect=prilist.get_rect()
                                          screen.blit(prilist,(38,203+30*i))
                              pygame.display.update()
                              area=0
                        else:
                              area=0
                                          
def get_time():
      from datetime import datetime
      return datetime.now().strftime("%m/%d")


def get_rank():
      global step, inname
      f = open("rank.txt",'r')
      text_lines=f.readlines()
      f.close()

      record=[]
      date=get_time()
      step=str(instep)
      record+=[[inname,step,date]]

      for i in range(0,len(text_lines),4):
            name=text_lines[i][:-1]
            step=text_lines[i+1][:-1]
            date=text_lines[i+2][:-1]
            record+=[[name,step,date]]

      for i in range(0,len(record)-1):
            for j in range(len(record)):
                  w=record[i][1]
                  z=record[i+1][1]
                  if int(w) > int(z):
                        record[i],record[i+1] = record[i+1],record[i]

      f= open("rank.txt",'w')
      for i in range(8):
            for j in range(3):
                  f.write(record[i][j]+'\n')
            f.write("\n")
      f.close()
      
      line=[]
      for i in range(len(record)):
            line2=''
            if len(record[i][0])>8:
                  line2+='%d. %-8s %-4s %s' %(i+1,record[i][0][:8],record[i][1],record[i][2])
            else:
                  line2+='%d. %-8s %-4s %s' %(i+1,record[i][0],record[i][1],record[i][2])
            line+=[line2]
      return line

def prirank():
      global rank
      for i in range(len(rank)):
            prirank=my_font.render(rank[i],True,(0,0,0))
            textrect=prirank.get_rect()
            screen.blit(prirank,(45,142+35*i))
      pygame.display.update()

def rankbut():
      prirank()
      global flag
      while flag==11:
            k,l=pygame.mouse.get_pos()
            for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                        if 240<=k<=363 and 482<=l<=518:
                              click.play()
                              screen.blit(gameover2,(0,0))
                              if len(globalist)<=11:
                                    for i in range(len(globalist)):
                                          pri=globalist[i]
                                          prilist=my_font.render(pri,True,(0,255,0))
                                          textrect=prilist.get_rect()
                                          screen.blit(prilist,(38,203+30*i))
                              else:
                                    for i in range(11):
                                          pri=globalist[-11+i]
                                          prilist=my_font.render(pri,True,(0,255,0))
                                          textrect=prilist.get_rect()
                                          screen.blit(prilist,(38,203+30*i))
                              pygame.display.update()
                              flag-=9
                              gameoverfunc()
                  area=0
                  if 240<=k<=363 and 482<=l<=518:
                        area=1
                  if area==0:
                        screen.blit(ranking,(0,0))
                        prirank()
                        area=0

                  while area!=0:
                        if area==1:
                              screen.blit(rankback,(0,0))
                              prirank()
                              pygame.display.update()
                              area=0
                        else:
                              area=0
      
#classiccomputer                          
guess=''
globalist=[]
lisa=[]
lisg=[]
p=0
q=0
i=0
v="esc"
che=[]
place1=(111,108)
place2=(71,245)
place3=(170,245)
my_font=pygame.font.Font("LCDM2N__.TTF",25)
instep=0
mode=0
inname=''

#classicpersonal
target=''

#challengingcomputer
h=''

#challengingpersonal

esct()
menu1()
while 1: 
      menu2()
      if mode==1:
            screen.blit(gameover,(0,0))
            if len(globalist)<=11:
                  for i in range(len(globalist)):
                        pri=globalist[i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            else:
                  for i in range(11):
                        pri=globalist[-11+i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            pygame.display.update()
            flag=2

            record=[]
            f =open("rank.txt",'r')
            text_lines=f.readlines()
            f.close()

            for i in range(0,len(text_lines),4):
                  name=text_lines[i][:-1]
                  step=text_lines[i+1][:-1]
                  date=text_lines[i+2][:-1]
                  record+=[[name,step,date]]

            least=record[7][1]
            least=int(least)
            if instep < least:
                  screen.blit(getname,(40,156))
                  pygame.display.update()
                  inname=ask(screen,(93,262),30)
                  screen.blit(gameover,(0,0))
                  if len(globalist)<=11:
                        for i in range(len(globalist)):
                              pri=globalist[i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
                  else:
                        for i in range(11):
                              pri=globalist[-11+i]
                              prilist=my_font.render(pri,True,(0,255,0))
                              textrect=prilist.get_rect()
                              screen.blit(prilist,(38,203+30*i))
            rank=get_rank()
            gameoverfunc()
                  
      else:
            screen.blit(gameover3,(0,0))
            if len(globalist)<=11:
                  for i in range(len(globalist)):
                        pri=globalist[i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            else:
                  for i in range(11):
                        pri=globalist[-11+i]
                        prilist=my_font.render(pri,True,(0,255,0))
                        textrect=prilist.get_rect()
                        screen.blit(prilist,(38,203+30*i))
            pygame.display.update()
            flag=2
            menu1()
            
      guess=''
      target=''
      globalist=[]
      lisa=[]
      lisg=[]
      che=[]
      instep=0
      p=0
      q=0
      i=0
      h=''

