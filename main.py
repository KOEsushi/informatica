import turtle as t
import os
t.speed(0)
def base():
  t.forward(75)
  t.backward(75)

def paal():
  t.left(90)
  t.forward(100)
  t.backward(100)

def support():
  t.forward(10)
  t.right(135)
  t.forward(14.14213562)
  t.right(135)
  t.forward(10)
  t.left(180)
  t.left(90)

def hangyboi():
  t.forward(100)
  t.right(90)
  t.forward(100)
  
  
def support2():
  t.backward(90)
  t.right(135)
  t.forward(14.14213562)
  t.right(135)
  t.forward(10)
  t.right(90)
  t.forward(75)
  t.right(90)

def hanger():
  t.forward(10)
  t.right(90)
  t.circle(10)
  t.up()
  t.left(90)
  t.forward(20)
  t.left(45)
  t.down()
  for i in range(45):
    t.forward(0.5)
    t.right(1)
  t.left(135)
  t.forward(15)
  t.backward(15)
  t.right(135)
  for i in range(45):
    t.forward(0.5)
    t.right(1)
  t.right(90)
  for i in range(45):
    t.forward(0.5)
    t.right(1)
  t.left(45)
  t.forward(15)
  t.backward(15)
  t.right(45)
  for i in range(45):
    t.forward(0.5)
    t.right(1)
  t.right(90)
  for i in range(90):
    t.forward(0.5)
    t.right(1)
  t.left(20)
  t.forward(20)
  t.backward(20)
  t.left(45)
  t.forward(20)
  t.backward(20)
  t.right(45)
#Ik definiëer alle turtle actie. Ik gebruik elke defenitie maar 1 keer, dus het is eigenlijk niet nodig, maar ik vond het wel zo overzichtelijk om alle codes van turtle bovenin te hebben staan.
guessed = ""
fout = ""
fout_msg = ""
z = 0
#we maken een aantal functies aan, die we later gebruiken
drommels = 0
print ("Welkom bij galmansmennnekinders!")
print ("Raad met letters het geheime woord!")
print ("'?' = hele woord raden")
print ("'QQ' of 'qq' = het spel verlaten")
while True:
  woord = input("kies een woord") #we maken de functie "woord" aan.
  if not (woord.isalpha()):
    print("nee, alleen letters!") #we laten de gebruiker net zo lang een woord invullen, totdat deze volledig uit letters bestaat.
  else:
    os.system('cls') # we verschonen de output
    break #als het gekozen woord uit letters bestaat, breaken we de loop, en kan de rest van de code aan het werk.
  
for i in range(6): #we maken een for i in range loop aan, 5 foute pogingen, en daarna nog één keer om de eindtekst te weergeven.
  while i<6: #we maken een while loop aan die we alleen breken als de gebruiker een foute gok heeft gegeven. dan wordt i één groter. als deze uiteindelijk 6 is, zal de while loop zichzelf afsluiten. 
    msa = ""        # we refreshen voor elke gok de functie "msa".
    drommels+=1     # elke gok wordt er bij "drommels" (het aantal pogingen) 1 opgeteld.
    for g in woord:   # voor elke waarde in het gekozen woord, wordt alles een keer uitgevoerd.
      if g in guessed:  # als deze waarde uit het woord (een van de letters) al een keer geraden is, en dus in de functie "guessed" zit, zal deze letter uit "woord" bij "msa" worden opgeteld.
        msa = msa + g
      else:
        msa = msa + "_" + " " # als deze letter niet in "guessed" zit en dus niet geraden is, zal hij een laag streepje printen.
        
    if msa == woord:          # als msa precies gelijk is aan woord, dus elke letter in "woord", zit in "guessed" en is dus opgeteld aan "msa", zal het programma de gebruiker naar een eindscherm brengen.
      print("goed gedaan, zoon!")
      i = 6
      drommels -= 1 # omdat je hier nog niet gegokt hebt, maar wel al een nieuwe loop in gegaan bent, zou hij er nog 1 beurt bij optellen. daarom trekken we die eraf.
      break
    
    
    print(msa)
    print("foute letters: " + fout)
    gok = input("Raad maar raak!")  # hier mag je beginnen met raden. alle fout geraden letter worden weergeven, evenals de goede letters.
    
    if (gok == "QQ") or (gok == "qq"): # als de input QQ of qq is, zal het programma afsluiten, dan wordt i = 7 en zal de while loop afsluiten en zal hij naar het "if i == 7" eindscherm gaan
      print("Oke, dan niet he.")
      i = 7
    
    elif (gok == "help") or (gok == "Help") or (gok == "HELP"):
      print("'?' = hele woord raden")
      print("'QQ' of 'qq' = het spel verlaten")
      drommels-=1    # instructies voor hoe alle opdrachten werken. we halen 1 van het aantal beurten af, zodat dit niet als beurt wordt opgeteld.
      
    
    elif len(gok)>1:
      print("1 letter per keer! Als je het hele woord wilt raden, typ: '?' ")
      drommels -=1  # Als de input meer dan 2 tekens bevat, zal hij een foutmelding geven en geen beurten optellen.
      
    elif gok == "?":
      gok = input("Raad da woord")
      if gok == (woord):
        print("goed gedaan, mijn jongen!")
        i = 6
        msa = woord # als de input een vraagteken is, zal de mogelijkheid om meerdere tekens in te voeren; het hele woord te raden
        
                              
      else:
        gok = " " + gok + " "
        break # als het woord niet het juiste woord was, zal er voor en achter de gok een spatie worden gezet, zodat deze als geheel woord bij de foute letters wordt opgeteld.
      
    elif not (gok.isalpha()):
      print("Alleen letters of '?'") # als er tekens worden ingevoerd die geen letters zijn geven een foutmelding. hij geeft als output dat je wel ? kan invoeren.
      drommels -=1
    elif gok in msa:
      print("die heb je al goed!")
      drommels-=1 # als de input van de gebruiker in msa zit en dus al is geraden, zegt het systeem dat dit woord al geraden is.
    elif gok in woord:
     
      guessed = guessed + gok # als de input in het te raden woord zit, zal deze input bij de goed geraden letters: "guessed", worden opgeteld.
      
    elif gok in fout:
      print("die heb je al geraden.")
      drommels -=1    # als de input in fout zat, was deze al fout geraden en zegt het systeem: "NEE".
    
    
    
    else:
      break # als de input fout is, zal de while loop breken.
  
  if i < 6:  # 5 keer kan dit herhaald worden. dit zit niet meer in de while loop, dit zit in de for i in range loop.

    fout = fout + gok # dit kan alleen bereikt worden als de input fout is. dit betekend dat de gok fout is. alle fouten worden bij elkaar opgeteld, door de fouten bij de gok op te tellen.
    
    if i == 0:
      base()
    elif i == 1: 
      paal()
    elif i == 2:
      support()
    elif i == 3:
      hangyboi()
    elif i == 4:
      support2()
    elif i == 5:
      hanger()
      print("je bent een slecht man")
      break # na 5 fouten wordt het volledige galgje getekend. hierna breakt de functie, dan is i = 5 en zal hij naar het "i == 5" eindscherm gaan.
    
  else:
    break # als i == een waarde hoger dan of gelijk aan 6, zal hij geen turtle gebruiken en zal hij direct naar het eindscherm gaan.
if i == 6:
  print("je hebt het woord geraden in: " + str(drommels) + " keer.")
  print(msa) # i == 6 als het woord geraden is. dan gaat het hier naartoe.
elif i == 7:
  i = 7 # als je "QQ" intypt, zal i == 7 worden en zal hij naar dit eindscherm gestuurd worden. ik heb na de elif nog even i = 7 getypt omdat python per se wat wou.
else: 
  print("jammer! het geheime woord was: " + woord) # als i == 5 gaat hij hierheen. dit is het scherm als je het fout hebt geraden, en hangt.
  
    

  
