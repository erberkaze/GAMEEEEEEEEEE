import pygame


def CheckCollision(x,y,treasureX,treasureY):
    global screen , textWin
    collisionState = False
    if y >= treasureY and y <= treasureY + 40 :
        if x >= treasureX and x <= treasureX +35 : 
            y = 650
            collisionState = True
        elif x + 35 >= treasureX and x + 35 <= treasureX + 35:
            y = 650
            collisionState = True
    elif y + 40 >= treasureY and y + 40 <= treasureY + 40 :
        if x >= treasureX and x <= treasureX + 35 :
            y = 650
            collisionState = True
        elif x+35 >= treasureX and x+35 <= treasureX + 35:
            y = 650
            collisionState = True
    return collisionState, y


pygame.init()##pygame sistemini çalıştırmak için

screen = pygame.display.set_mode((900,700))#bir pencere açmak için kullanıyoruz içine yazdığımız değer ise boyutu

finished = False#bu oyunun bitip bitmediğini kontrol etmesi için

x = 450-35/2    
y = 650



#array = [0,1,2,3,4,5,"HELLO"]

#print (pygame.K_SPACE) bu basılan tuşun hangi indexe sahip olduğunu gösteriyor lazım olabiliyor

#yeniliyor ikidebir

playerImage = pygame.image.load("player.png")         
playerImage = pygame.transform.scale(playerImage,(30,30))#koyduğumuz resmin boyutunu ayarlıyoruz
playerImage = playerImage.convert_alpha()#alpha tam olarak png ye çevirmesine yardımcı oluyor   

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage,(900,700))
screen.blit(backgroundImage,(0,0))

treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage,(35,40))
treasureImage = treasureImage.convert_alpha()
treasureX = 450 - 35/2
treasureY = 50


enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(35,40))
enemyImage = enemyImage.convert_alpha()
enemyX = 100
enemyY = 580-10

screen.blit(treasureImage,(treasureX,treasureY))

font = pygame.font.SysFont("comicsans",60)#yazının fontunu 

level = 1

enemyNames = {0:"Max",1:"Jilly",2:"Greg",3:"Diane"}

frame = pygame.time.Clock()

collisionTreasure = False
collisionEnemy = False
movingRight = True

enemies = [(enemyX,enemyY,movingRight)]#(enemyX,enemyY,movingRight)


while finished == False :#oyun bitmediyse v.b
    for event in pygame.event.get(): #oyunda olan bütün eventleri bir bir dolaşıp kontrol ediyor
        if event.type == pygame.QUIT:#event type ı olan bi variable haline geliyo ve yürüme koşma v.b her durum için bi değer alıyo
            finished = True
            

    pressedKeys = pygame.key.get_pressed()#herhangi bi tuşa basılma durumu     
    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies :
        if enemyX >= 800 - 35 :
            movingRight = False
        elif enemyX <= 100:
            movingRight = True
        if movingRight == True:
            enemyX += 5*level
        else:
            enemyX -= 5*level
        enemies[enemyIndex] = (enemyX,enemyY,movingRight)
        enemyIndex += 1
    
    if pressedKeys[pygame.K_SPACE] == 1:
        y -= 5
        
    
    #rectOne = pygame.Rect(x,y,30,30)#x,y,width,height sırası ile yazılıcak içine rect dikdörtgen sağlıyo

    color = (0,0,255)#r,g,b methodu ile kullandık burada

    white = (255,255,255)


    #screen.fill(white)# arka planı boyuyor

    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(x,y))#koymak istediğimiz resmi ve pozisyonu

    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies :
        screen.blit(enemyImage,(enemyX,enemyY))
        collisionEnemy,y = CheckCollision(x,y,enemyX,enemyY)
        if collisionEnemy == True :
            name = enemyNames[enemyIndex]
            textLose = font.render("Seni öldüren kişi "+name,True,(255,0,0))
            screen.blit(textLose,(450-textLose.get_width()/2,350 - textLose.get_height()/2))
            pygame.display.flip()
            frame.tick(1)

        frame.tick(30)
        enemyIndex += 1
        
    collisionTreasure,y = CheckCollision(x,y,treasureX,treasureY)#function un çağırılması
    
    if collisionTreasure == True :
        level += 1
        enemies.append((enemyX-50*level,enemyY-50*level,False))
        textWin = font.render("Seviye "+str(level),True,(0,0,0))#ne yazacağımızı ve yazının rengi v.b
        screen.blit(textWin,(450 - textWin.get_width()/2,350 - textWin.get_height()/2))#bunun sebebi tam yazıyı ortalamak için textin height ve width ini alıyoruz
        pygame.display.flip()
        frame.tick(1)# great job yazısını uzun süre görmek için yaptık
    
    
        
       
    #pygame.draw.rect(screen,color,rectOne)#draw komutu nereye yazıcağımızı rengini ve hangi objeyi
    pygame.display.flip()#en son screen update i için
    frame.tick(30) #buradaki hıza göre senin hareketlerin yavaşlayıp hızlanıyor
    
    
