"""import pygame
import random

pygame.init()

pygame.mixer.music.load("bgmsc.wav")
gmovrsnd= pygame.mixer.Sound("gameover.wav")
gmovr= pygame.mixer.Sound("govr.wav")
sfxwing= pygame.mixer.Sound("sfx_wing.wav")
sfxscr= pygame.mixer.Sound("sfx_point.wav")

#pygame.mixer.music.play(-1)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
dw=600
dh=476
screen=pygame.display.set_mode([dw,dh])
pygame.display.set_caption('Flappy Blue Bird')
pimg=[pygame.image.load(str(i)+'.png') for i in range(1,5)]
clock=pygame.time.Clock()
vec=pygame.math.Vector2
bg=pygame.image.load('bg.png')
bw=bg.get_width()
blist=[[50,310],[60,300],[70,290],[80,280],[90,270],[100,260],[110,250],[120,240],[130,230],[140,220],[150,210],[160,200],[170,190],[180,180],
       [190,170],[200,160],[210,150],[220,140],[230,130],[240,120],[250,110],[260,100],[270,90],[280,80]
       ,[290,70],[300,60],[310,50]]
class Bird(pygame.sprite.Sprite):
   def __init__(self,game):
      super(Bird,self).__init__()
      self.image=pimg[0]
      self.image=pygame.transform.scale(self.image,(45,35))
      self.rect=self.image.get_rect()
      self.vel=vec(0,0)
      self.rect.center=(dw//2,dh//2)
      self.acc=vec(0,0)
      self.pos=vec(self.rect.center)
      self.fc=0
   def update(self):
      self.acc=vec(0,2.5)
      self.vel=vec(0,0)
      keys=pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
#         pygame.mixer.Sound.play(sfxwing)
         self.acc.y=-2.0
         if self.fc+2<28:
            self.fc+=2
            self.image=pimg[self.fc//7]
            self.image=pygame.transform.scale(self.image,(85,65))
         else:
            self.fc=0
      else:
         self.image=pimg[0]
         self.image=pygame.transform.scale(self.image,(85,65))
      self.vel+=self.acc
      self.pos+=self.vel+0.5*self.acc
      if self.pos.y<=0+self.rect.width//2:
         self.pos.y=0+self.rect.width//2
      if self.pos.y>=dh-self.rect.width//2:
         self.pos.y=dh-self.rect.width//2
      self.rect.center=self.pos
      self.mask=pygame.mask.from_surface(self.image)
class TBlock(pygame.sprite.Sprite):
   def __init__(self,x,h1):
      super(TBlock,self).__init__()
      self.image=pygame.image.load('tp.png')
      self.image=pygame.transform.scale(self.image,(80,h1))
      self.rect=self.image.get_rect()
      self.rect.x,self.rect.y=x,0
   def update(self):
      self.rect.x-=2
      self.mask1=pygame.mask.from_surface(self.image)
class BBlock(pygame.sprite.Sprite):
   def __init__(self,x,h2):
      super(BBlock,self).__init__()
      self.image=pygame.image.load('bp.png')
      self.image=pygame.transform.scale(self.image,(80,h2))
      self.rect=self.image.get_rect()
      self.rect.x,self.rect.y=x,dh-self.rect.height
   def update(self):
      self.rect.x-=2
      self.mask2=pygame.mask.from_surface(self.image)
class Game:
   def __init__(self):
      self.msg("Press Enter to Play",dw-400,dh-100,white,40)
      wait=1
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
            pygame.display.flip()
      self.bgx=0
      self.x=650
      self.h1=180
      self.h2=180
      self.score=0
      self.gover=0
      self.last=pygame.time.get_ticks()
   def blockgen(self):
      x=random.randint(620,650)
      h=random.choice(blist)
      h1=h[0]
      h2=h[1]
      self.tblock=TBlock(x,h1)
      self.tblocks=pygame.sprite.Group()
      self.tblocks.add(self.tblock)
      self.all_sprites.add(self.tblock)
      self.bblock=BBlock(x,h2)
      self.bblocks=pygame.sprite.Group()
      self.bblocks.add(self.bblock)
      self.all_sprites.add(self.bblock)
   def new(self):
      pygame.mixer.music.play(-1) 
      self.bird=Bird(self)
      self.all_sprites=pygame.sprite.Group()
      self.all_sprites.add(self.bird)
      self.tblock=TBlock(self.x,self.h1)
      self.tblocks=pygame.sprite.Group()
      self.tblocks.add(self.tblock)
      self.all_sprites.add(self.tblock)
      self.bblock=BBlock(self.x,self.h2)
      self.bblocks=pygame.sprite.Group()
      self.bblocks.add(self.bblock)
      self.all_sprites.add(self.bblock)
      self.score=0
      self.gover=0
   def msg(self,text,x,y,color,size):
      self.font=pygame.font.SysFont('georgia',size,bold=1)
      msgtxt=self.font.render(text,1,color)
      msgrect=msgtxt.get_rect()
      msgrect.center=x//2,y//2
      screen.blit(msgtxt,(msgrect.center))
   def pause(self):
      wait=1
      pygame.mixer.music.pause()
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("Paused",dw-100,dh-100,white,40)
         pygame.display.flip()
         
      pygame.mixer.music.unpause()
   def over(self):
      pygame.mixer.music.stop()
      pygame.mixer.Sound.play(gmovrsnd)
      pygame.mixer.Sound.play(gmovr)
      wait=1
      self.gover=1
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("Game Over !",dw-415,dh-100,white,70)
         self.msg("Press Enter to Play Again",dw-500,dh+200,white,40)
         pygame.display.flip()
      self.new()
   def scores(self):
         self.msg("Score:"+str(self.score),dw-130,200,green,30)

   def update(self):
     self.all_sprites.update()
     #hits1=pygame.sprite.spritecollide(self.bird,self.bblocks,False,pygame.sprite.collide_mask)
     #hits2=pygame.sprite.spritecollide(self.bird,self.tblocks,False,pygame.sprite.collide_mask)
     col2 = pygame.sprite.spritecollideany(self.bird, self.bblocks)
     col1 = pygame.sprite.spritecollideany(self.bird, self.tblocks)
     #if hits1 or hits2:
      #  self.over()
     if col2 or col1:
        self.over()
     relx=self.bgx%bw+5
     screen.blit(bg,(relx-bw+3,0))
     if relx<dw:
        screen.blit(bg,(relx,0))
     self.bgx-=2
     if self.bblock.rect.x<dw//2 and self.tblock.rect.x<dw//2:
        self.blockgen()
        self.score+=1
        pygame.mixer.Sound.play(sfxscr)

   def draw(self):
      self.all_sprites.draw(screen)
      self.scores()
   def event(self):
      for event in pygame.event.get():
         clock.tick(60)
         if event.type==pygame.QUIT:
            pygame.quit()
            quit()
         if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
               if event.key==pygame.K_RETURN:
                  self.pause()
   def run(self):
      while 1:
         self.event()
         self.update()
         self.draw()
         pygame.display.flip()
g=Game()
while g.run:
   g.new()
   g.run()
"""
import pygame                                           #Importing the pygame library
import random

pygame.init()

pygame.mixer.music.load("bgmsc.wav")
gmovrsnd= pygame.mixer.Sound("gameover.wav")
gmovr= pygame.mixer.Sound("govr.wav")
sfxwing= pygame.mixer.Sound("sfx_wing.wav")
sfxscr= pygame.mixer.Sound("sfx_point.wav")

#pygame.mixer.music.play(-1)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
dw=600
dh=476
screen=pygame.display.set_mode([dw,dh])
pygame.display.set_caption('Flappy Blue Bird')
pimg=[pygame.image.load(str(i)+'.png') for i in range(1,5)]
clock=pygame.time.Clock()
vec=pygame.math.Vector2
bg=pygame.image.load('bg.png')
bw=bg.get_width()
blist=[[50,310],[60,300],[70,290],[80,280],[90,270],[100,260],[110,250],[120,240],[130,230],[140,220],[150,210],[160,200],[170,190],[180,180],
       [190,170],[200,160],[210,150],[220,140],[230,130],[240,120],[250,110],[260,100],[270,90],[280,80]
       ,[290,70],[300,60],[310,50]]
class Bird(pygame.sprite.Sprite):
   def __init__(self,game):
      super(Bird,self).__init__()
      self.image=pimg[0]
      self.image=pygame.transform.scale(self.image,(75,55))
      self.rect=self.image.get_rect()
      self.vel=vec(0,0)
      self.rect.center=(dw//2,dh//2)
      self.acc=vec(0,0)
      self.pos=vec(self.rect.center)
      self.fc=0
   def update(self):
      self.acc=vec(0,1.5)
      self.vel=vec(0,0)
      keys=pygame.key.get_pressed() #SEE
      if keys[pygame.K_SPACE]:
#         pygame.mixer.Sound.play(sfxwing)
         self.acc.y=-2.0
         if self.fc+2<28:
            self.fc+=2
            self.image=pimg[self.fc//7]
            self.image=pygame.transform.scale(self.image,(75,55))
         else:
            self.fc=0
      else:
         self.image=pimg[0]
         self.image=pygame.transform.scale(self.image,(75,55))
      self.vel+=self.acc
      self.pos+=self.vel+0.4*self.acc
      if self.pos.y<=0+self.rect.width//2:  #SEE line 59-64
         self.pos.y=0+self.rect.width//2
      if self.pos.y>=dh-self.rect.width//2:
         self.pos.y=dh-self.rect.width//2
      self.rect.center=self.pos
      self.mask=pygame.mask.from_surface(self.image)
class TBlock(pygame.sprite.Sprite): #See Sprite
   def __init__(self,x,h1):
      super(TBlock,self).__init__()
      self.image=pygame.image.load('tp.png')
      self.image=pygame.transform.scale(self.image,(80,h1))
      self.rect=self.image.get_rect()
      self.rect.x,self.rect.y=x,0
   def update(self):
      self.rect.x-=2
      self.mask1=pygame.mask.from_surface(self.image)
class BBlock(pygame.sprite.Sprite):
   def __init__(self,x,h2):
      super(BBlock,self).__init__()
      self.image=pygame.image.load('bp.png')
      self.image=pygame.transform.scale(self.image,(80,h2))
      self.rect=self.image.get_rect()
      self.rect.x,self.rect.y=x,dh-self.rect.height
   def update(self):
      self.rect.x-=2
      self.mask2=pygame.mask.from_surface(self.image)
          
               
class Game:

 
   def __init__(self):
      self.msg("Press Enter to Play",dw-400,dh-100,white,40)
      self.load_data()
      wait=1
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
            pygame.display.flip()
      self.bgx=0
      self.x=650
      self.h1=180
      self.h2=180
      self.score=0
      self.gover=0
      self.last=pygame.time.get_ticks()
      
   def load_data(self):
       with open('high_score.txt','w') as f:
           try:
               self.highscore = int(f.read())
           except:
               self.highscore = 0
       self.msg("High Score: "+str(self.highscore),dw-400,dh-200,white,40)

     
      

    
   def blockgen(self):
      x=random.randint(620,650)
      h=random.choice(blist)
      h1=h[0]
      h2=h[1]
      self.tblock=TBlock(x,h1)
      self.tblocks=pygame.sprite.Group()
      self.tblocks.add(self.tblock)
      self.all_sprites.add(self.tblock)
      self.bblock=BBlock(x,h2)
      self.bblocks=pygame.sprite.Group()
      self.bblocks.add(self.bblock)
      self.all_sprites.add(self.bblock)
   def new(self):
      pygame.mixer.music.play(-1) 
      self.bird=Bird(self)
      self.all_sprites=pygame.sprite.Group()
      self.all_sprites.add(self.bird)
      self.tblock=TBlock(self.x,self.h1)
      self.tblocks=pygame.sprite.Group()
      self.tblocks.add(self.tblock)
      self.all_sprites.add(self.tblock)
      self.bblock=BBlock(self.x,self.h2)
      self.bblocks=pygame.sprite.Group()
      self.bblocks.add(self.bblock)
      self.all_sprites.add(self.bblock)
      self.score=0
      self.gover=0
      
   def msg(self,text,x,y,color,size):
      self.font=pygame.font.SysFont('georgia',size,bold=1)
      msgtxt=self.font.render(text,1,color)
      msgrect=msgtxt.get_rect()
      msgrect.center=x//2,y//2
      screen.blit(msgtxt,(msgrect.center))
   def pause(self):
      wait=1
      pygame.mixer.music.pause()
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("Paused",dw-165,dh-100,white,40)
         pygame.display.flip()
         
      pygame.mixer.music.unpause()
      
   def scores(self):
      self.msg("Score:"+str(self.score),dw-130,200,green,30)
      
   def over(self):
      pygame.mixer.music.stop()
      pygame.mixer.Sound.play(gmovrsnd)
      pygame.mixer.Sound.play(gmovr)
      wait=1
      self.gover=1
      while wait:
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               quit()
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RETURN:
                  wait=0
         self.msg("Game Over !",dw-315,dh+10,white,50)
         self.msg("Press Enter to Play Again",dw-500,dh+200,white,40)

         if self.score > self.highscore:
             self.highscore = self.score
             self.msg("NEW HIGH SCORE!",dw-330,dh-400,red,35)
             with open('high_score.txt','w') as f:
                 f.write(str(self.highscore))
         else:
             self.msg('High Score: ' + str(self.highscore),dw-225,dh-190,red,30)
         pygame.display.flip()
         
      self.new()
         
             
   def update(self):
     self.all_sprites.update()
     hits1=pygame.sprite.spritecollide(self.bird,self.bblocks,False,pygame.sprite.collide_mask)
     hits2=pygame.sprite.spritecollide(self.bird,self.tblocks,False,pygame.sprite.collide_mask)
     #col2 = pygame.sprite.spritecollideany(self.bird, self.bblocks)
     #col1 = pygame.sprite.spritecollideany(self.bird, self.tblocks)
     if hits1 or hits2:
        self.over()
     #if col2 or col1:
       # self.over()
     relx=self.bgx%bw+5
     screen.blit(bg,(relx-bw+3,0))
     if relx<dw:
        screen.blit(bg,(relx,0))
     self.bgx-=2
     if self.bblock.rect.x<dw//2 and self.tblock.rect.x<dw//2:
        self.blockgen()
        self.score+=1
        pygame.mixer.Sound.play(sfxscr)

   def draw(self):
      self.all_sprites.draw(screen)
      self.scores()
   def event(self):
      for event in pygame.event.get():
         clock.tick(60)
         if event.type==pygame.QUIT:
            pygame.quit()
            quit()
         if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
               if event.key==pygame.K_RETURN:
                  self.pause()
   def run(self):
      while 1:
         self.event()
         self.update()
         self.draw()
         pygame.display.flip()
g=Game()
while g.run:
   g.new()
   g.run()
