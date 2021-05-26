import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


gamma = 0.9 # indirim faktörü
boyut = 50 # çevrenin boyutu (boyut*boyut)

odulListesi = []
adımListesi= []
komsuListesi=[]

# engel.txt oluşturma-----------------------------------------------------------------------------------------------------------------
# Oluşturulan çevrenin tüm özelliklerini bir txt dosyasına yazdırır.
def engelYazdirma(cevre):

    engelDosyasi = open("engel.txt", "w")
    a=1
    for i in range(boyut):
        for j in range(boyut):

            if cevre[i, j] == -5:
                engelDosyasi.write(str(a)+"  ->  ("+str(i) + "," + str(j) + ",Engel)\n")
            elif cevre[i, j] == 0:
                engelDosyasi.write(str(a)+"  ->  ("+str(i) + "," + str(j) + ",GİRİŞ)\n")
            elif cevre[i, j] == 999:
                engelDosyasi.write(str(a)+"  ->  ("+str(i) + "," + str(j) + ",ÇIKIŞ)\n")
            else:
                engelDosyasi.write(str(a)+"  ->  ("+str(i) + "," + str(j) + ",Yol)\n")
            a+=1

    engelDosyasi.close()
#-----------------------------------------------------------------------------------------------------------------



# Komşu bulma-----------------------------------------------------------------------------------------------------------------
# Üzerinde bulunduğu kareden hamle yapılabilecek tüm koşuları döndürür.
def gecisBulucu(x):
   # Parametre olarak gönderilen "x" değeri anlık durumu nitelemektedir.
   # Veriler "S(a) = a-1" formatında olduğu için "x" değeri 1 arttırılır.
  x = x+1
  komsuListesi.clear()
  i =int((x-1)/boyut)
  j=int((x-1)%boyut)

 
  # Yine "S(a) = a-1" formatından ötürü durum değil de indeks döndürmek amacıyla -1 azaltılmıştır.
  if i==0 and j==0:
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x+boyut)
    return komsuListesi
    

  if i==0 and j==boyut-1:
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x-2)
    komsuListesi.append(x+boyut-2)
    return komsuListesi

  if i==0 and (j>0 and j<boyut):
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x+boyut)
    komsuListesi.append(x-2)
    komsuListesi.append(x+boyut-2)
    return komsuListesi
    

  if i==boyut-1 and j==0:
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x-boyut)
    return komsuListesi
    

  if i==boyut-1 and j==boyut-1:
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x-2)
    komsuListesi.append(x-boyut-2)
    return komsuListesi
       

  if i==boyut-1 and (j>0 and j<boyut):
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x-2)
    komsuListesi.append(x-boyut-2)
    komsuListesi.append(x-boyut)
    return komsuListesi
   

  if (i>0 and i<boyut) and j==0:
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x+boyut)
    komsuListesi.append(x-boyut)
    return komsuListesi
    

  if (i>0 and i<boyut) and j==boyut-1:
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x-2)
    komsuListesi.append(x-boyut-2)
    komsuListesi.append(x+boyut-2)
    return komsuListesi
   
  
  else:
    komsuListesi.append(x-boyut-1)
    komsuListesi.append(x+boyut-1)
    komsuListesi.append(x)
    komsuListesi.append(x-2)
    komsuListesi.append(x-boyut-2)
    komsuListesi.append(x-boyut)
    komsuListesi.append(x+boyut-2)
    komsuListesi.append(x+boyut)
    return komsuListesi
#-----------------------------------------------------------------------------------------------------------------




# başlangıç verisi alma------------------------------------------------------------------------------------------------------------------------------------
# başlangıç ve bitiş durum değerlerini kullanıcıdan almak için eklenen bloktur.
# bu bölüm için "tkinter" import edilmiştir.
# "Başla" butonuna basılınca alınan durum verilerine göre Q-Learning algoritması başlar.
root = tk.Tk()
root.title("Başlangıç-Bitiş Seçme")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight-100, positionDown-100))
canvas1 = tk.Canvas(root, width=400, height=300,  relief='raised')
canvas1.pack()

photo = tk.PhotoImage(file = r"robot.png")
photoimage = photo.subsample(9,9)

label1 = tk.Label(root, text='Başlangıç ve Bitiş Durumu Seçiniz.')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Başlangıç:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 120, window=entry1)

label3 = tk.Label(root, text='Bitiş:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(200, 180, window=entry2)

x1= entry1.get()
x2=entry2.get()

returnList = list()

def tamam():
    
    returnList.append(entry1.get())
    returnList.append(entry2.get())
    root.destroy()

button1 = tk.Button(text='Başla', command=tamam,
                     bg='#cfcfcf', image = photoimage, font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 240, window=button1)

root.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------

# Çevre tanımlama-----------------------------------------------------------------------------------------------------------------------------
cevreMatrisi = np.ones(boyut*boyut)
cevreMatrisi[:int(boyut*boyut*0.3)] = 0

np.random.shuffle(cevreMatrisi)
cevreMatrisi = (np.random.rand(boyut*boyut) > 0.3).astype(int)
cevreMatrisi = np.where(cevreMatrisi == 1, 3, cevreMatrisi)
cevreMatrisi = np.where(cevreMatrisi == 0, -5, cevreMatrisi)
cevreMatrisi = cevreMatrisi.reshape((boyut,boyut))

kontrolMatris = np.zeros((boyut*boyut,boyut*boyut), dtype=bool)

# ------------------------------------------------------------------------------------------------------------------------------------

# Q-Table'ın başlangıç tanımlaması
Q = np.array(np.zeros([boyut*boyut, boyut*boyut]))


# Q-Learning fonksiyonu------------------------------------------------------------------------------------------------------------------------------------
# Q-Learning algoritmasının işlendiği fonksiyondur.
# Yol öğrenilerek uygun rota hesabı buranın içerisinde yapılır.
def yolBul(baslangicNoktasi, bitisNoktasi):
    adimSayisi = 0
    toplamPuan = 0
    
    # Konum değerleri durum değerine çevrilmiştir. 
    bitisDurumu = bitisNoktasi - 1
    baslangicDurumu = baslangicNoktasi - 1

    cevreMatrisi[int(bitisDurumu/boyut)][bitisDurumu % boyut]=999
    cevreMatrisi[int(baslangicDurumu/boyut)][baslangicDurumu % boyut]=0
    
    

    engelYazdirma(cevreMatrisi)
   
    
    # Ödül tablosu (reward table) tanımlama
    rewards = np.array(np.zeros([boyut*boyut, boyut*boyut]))
    
    for i in range(0, boyut):
        for j in range(0, boyut):
            if(i != boyut-1):
                rewards[i*boyut+j][(i+1)*boyut+j] = cevreMatrisi[i+1][j]  # alt
            if(i != 0):
                rewards[i*boyut+j][(i-1)*boyut+j] = cevreMatrisi[i-1][j]  # üst
            if(j != 0):
                rewards[i*boyut+j][i*boyut+(j-1)] = cevreMatrisi[i][j-1]  # sol
            if(j != boyut-1):
                rewards[i*boyut+j][i*boyut+(j+1)] = cevreMatrisi[i][j+1]  # sağ
            if(j != boyut-1 and i != 0):
                rewards[i*boyut+j][(i-1)*boyut+(j+1)] = cevreMatrisi[i-1][j+1]  # sağ üst
            if(j != 0 and i != 0):
                rewards[i*boyut+j][(i-1)*boyut+(j-1)] = cevreMatrisi[i-1][j-1]  # sol üst
            if(j != boyut-1 and i != boyut-1):
                rewards[i*boyut+j][(i+1)*boyut+(j+1)] = cevreMatrisi[i+1][j+1]  # sağ alt
            if(j != 0 and i != boyut-1):
                rewards[i*boyut+j][(i+1)*boyut+(j-1)] = cevreMatrisi[i+1][j-1]  # sol alt

    print(cevreMatrisi)
    print("************************************************")
    print(rewards)
    print("************************************************")
    
    
    # -----------Q-Learning algoritması-----------

    anlikDurum = baslangicDurumu
   
    
    for i in range(3000000):
        # Çalışmasını görmek amacıyla print yapıldı.
        if (i%100000==0):
            print(i)
       
        
        # Anlık durumdan yapılabilecek tüm hamleler için tanımlanmıştır (engeller, normal geçişler veya çıkış karesi).
        hamleler = []
        
        
                   
        for j in gecisBulucu(anlikDurum):
          
          if rewards[anlikDurum, j] != 0 and kontrolMatris[anlikDurum,j]!=True:
                hamleler.append(j)
               
                
        
        # Rastgele bir hamle (sağ,sol,ileri,geri,çapraz) seçerek o doğrultuda çalışır.
        sonrakiDurum = np.random.choice(hamleler)
       
       
        # Q-Learning formülü
        Q[anlikDurum, sonrakiDurum] = rewards[anlikDurum,
                                                   sonrakiDurum] + gamma * (Q[sonrakiDurum, np.argmax(Q[sonrakiDurum, ])])
       
        #Engel ise anlık durum olarak baslangicDurumu atanacak , engel degilse sonrakiDurum atanacak
        if rewards[anlikDurum,sonrakiDurum]==-5 or rewards[anlikDurum,sonrakiDurum]==999:
           
            if (rewards[anlikDurum,sonrakiDurum]==-5):

                kontrolMatris[:,sonrakiDurum]=True
                toplamPuan += -5
                
            
            else:
                toplamPuan += 5

               
            # if ve else için ortak adım
            adimSayisi+=1
            adımListesi.append(adimSayisi)
            odulListesi.append(toplamPuan)
            anlikDurum=baslangicDurumu
            adimSayisi = 0
            toplamPuan=0
            
                                       
        else:
            toplamPuan+=3        
            anlikDurum= sonrakiDurum
            adimSayisi+=1
            
         
         
    # Yol listesinin tanımı
    yol = [baslangicDurumu]

    
    # Çıkış noktasına ulaşana kadar bir yol oluşturur.
    while(sonrakiDurum != bitisDurumu):

        
        sonrakiDurum = np.argmax(Q[baslangicDurumu, ])
        
        yol.append(sonrakiDurum)
        
        baslangicDurumu = sonrakiDurum

    return yol
# ------------------------------------------------------------------------------------------------------------------------------------


bulunanYol = yolBul(int(returnList[0]), int(returnList[1]))
print("************************************************")
print("Bulunan Yol : ")
for i in bulunanYol:
    print("K"+str(i+1),end=" ")
print("************************************************\n")

# Grafik işlemleri------------------------------------------------------------------------------------------------------------------------------------
fig ,axs = plt.subplots(2)
plt.figure(figsize=(20,100))
axs[0].plot(odulListesi)
axs[0].set_xlabel("Bölüm")
axs[0].set_ylabel("Ödül")

axs[1].plot(adımListesi)
axs[1].set_xlabel("Bölüm")
axs[1].set_ylabel("Adım")

axs[0].grid(True)
axs[1].grid(True)

plt.show()
# ------------------------------------------------------------------------------------------------------------------------------------


# 2d goruntu fonksiyonu-------------------------------------------------------------------------------------------
'''
import pygame
import sys
def goruntu():
    screen_width = 800
    screen_heigth = 800

    # gridSize=16 (boyut=50 için)
    gridsize = 16
    grid_width = screen_width / gridsize
    grid_height = screen_heigth / gridsize

    engelRenk = (250, 0, 0)
    gecisRenk = (255, 163, 163)
    giris_renk = (0, 83, 250)
    cikis_renk = (0, 250, 58)
    yol_renk = (255, 250, 92)

    def drawGrid(surface, cevreMatrisi):

        for i in range(0, boyut):
            for j in range(0, boyut):
                if cevreMatrisi[i][j] == -5:
                    light = pygame.Rect(
                        (j * gridsize, i * gridsize,), (gridsize, gridsize))
                    pygame.draw.rect(surface, engelRenk, light)
                if cevreMatrisi[i][j] == 3:
                    dark = pygame.Rect(
                        (j * gridsize, i * gridsize,), (gridsize, gridsize))
                    pygame.draw.rect(surface, gecisRenk, dark)
                if ((i*boyut+j) in bulunanYol):
                    yol = pygame.Rect(
                        (j * gridsize, i * gridsize,), (gridsize, gridsize))
                    pygame.draw.rect(surface, yol_renk, yol)
                if cevreMatrisi[i][j] == 0:
                    giris = pygame.Rect(
                        (j * gridsize, i * gridsize,), (gridsize, gridsize))
                    pygame.draw.rect(surface, giris_renk, giris)
                if cevreMatrisi[i][j] == 999:
                    cikis = pygame.Rect(
                        (j * gridsize, i * gridsize,), (gridsize, gridsize))
                    pygame.draw.rect(surface, cikis_renk, cikis)

    pygame.init()
    screen = pygame.display.set_caption('Q-Learning')
    screen = pygame.display.set_mode((screen_width, screen_heigth))
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface, cevreMatrisi)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(surface, (0, 0))

        pygame.display.update()


goruntu() 
'''
import pygame
import sys
def goruntu():
    screen_width = 1200
    screen_heigth = 900
    # gridSize=24, gridSize2=18 (boyut=50 için)
    gridsize = 24
    gridsize2 =18


    engelRenk = (250, 0, 0)
    #gecisRenk = (255, 163, 163)
    gecisRenk = (204, 166, 137)
    giris_renk = (0, 83, 250)
    cikis_renk = (0, 250, 58)
    yol_renk = (255, 250, 92)
    


    def drawGrid(screen, cevreMatrisi):
        engelImg = pygame.image.load('engel.png')
        engelImg.convert()
        
        gecisImg = pygame.image.load("gecis.png")
        gecisImg.convert()
        
        girisImg = pygame.image.load("giris.png")
        girisImg.convert()
        
        cikisImg = pygame.image.load("cikis.png")
        cikisImg.convert()
        
        yolImg = pygame.image.load("yol.png")
        yolImg.convert()

        
        for i in range(0, boyut):
            for j in range(0, boyut):
                
                if cevreMatrisi[i][j] == -5:
                    engel = engelImg.get_rect()
                    engel.center = (j * gridsize+12, i * gridsize2+9)
                    screen.blit(engelImg, engel)
                    pygame.draw.rect(screen, engelRenk, engel,1)
                    
                if cevreMatrisi[i][j] == 3:
                    gecis = gecisImg.get_rect()
                    gecis.center = (j * gridsize+12, i * gridsize2+9)
                    screen.blit(gecisImg, gecis)
                    pygame.draw.rect(screen, gecisRenk, gecis,1)
                    
                if ((i*boyut+j) in bulunanYol):
                    yol = yolImg.get_rect()
                    yol.center = (j * gridsize+12, i * gridsize2+9)
                    screen.blit(yolImg, yol)
                    pygame.draw.rect(screen, yol_renk, yol,1)
                    
                if cevreMatrisi[i][j] == 0:
                    giris = girisImg.get_rect()
                    giris.center = (j * gridsize+12, i * gridsize2+9)
                    screen.blit(girisImg, giris)
                    pygame.draw.rect(screen, giris_renk, giris,1)
                        
                if cevreMatrisi[i][j] == 999:
                    cikis = cikisImg.get_rect()
                    cikis.center = (j * gridsize+12, i * gridsize2+9)
                    screen.blit(cikisImg, cikis)
                    pygame.draw.rect(screen, cikis_renk, cikis,1)
                    

    pygame.init()
    screen = pygame.display.set_caption('Q-Learning')
    screen = pygame.display.set_mode((screen_width, screen_heigth))
    drawGrid(screen, cevreMatrisi)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(screen, (0, 0))

        pygame.display.update()


goruntu() 
# ----------------------------------------------------------------------------------------------------------------