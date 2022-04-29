from flask import Flask, render_template
from random import seed
from random import randint
import os,sys

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
pathApp = os.getcwd()
aleatoire=[1,2,3,4,5,6,7]
for i in range(7):
	aleatoire[i]=randint(1,2)
	if aleatoire[i] == 1:
		aleatoire[i] = 'HIGH'
	else:
		aleatoire[i] = 'LOW'	
print (pathApp)
with open(pathApp+'/templates/Donnees.txt','w')as f:
	f.write("Date  Heure  Statut du capteur \r 21/04/2022 18h41:22 "+str(aleatoire[0])+" \r 21/04/2022 18h42:23 "+str(aleatoire[1])+" \r 21/04/2022 18h43:16 "+str(aleatoire[2])+" \r 21/04/2022 18h43:35 "+str(aleatoire[3])+" \r 21/04/2022 18h43:42 "+str(aleatoire[4])+" \r 21/04/2022 18h43:48 "+str(aleatoire[5])+" \r 21/04/2022 18h43:59 "+str(aleatoire[6])+"\r")
	
valeurs=open(pathApp+'/templates/Donnees.txt').read()

table=valeurs.split()

tableau = [s.replace("LOW","aucun mouvement detecte").replace("HIGH","mouvement detecte!")for s in table]
#tableau = [s.replace("HIGH","mouvement detecte!") for s in table] 



date=tableau[0]
heure=tableau[1]
statut=tableau[2]
ligne1=tableau[-3:]
Ligne1=(' '.join(ligne1))

ligne2=tableau[-6:-3]
Ligne2=(' '.join(ligne2))

ligne3=tableau[-9:-6]
Ligne3=(' '.join(ligne3))

ligne4=tableau[-12:-9]
Ligne4=(' '.join(ligne4))

ligne5=tableau[-15:-12]
Ligne5=(' '.join(ligne5))

ligne6=tableau[-18:-15]
Ligne6=(' '.join(ligne6))

os.remove(pathApp+'/templates/Donnees.txt')

@app.route('/rapport')
def home():
   return render_template('index.html',date=date,
   					heure=heure,
   					statut=statut,
   					ligne1=Ligne1,
   					ligne2=Ligne2,
   					ligne3=Ligne3,
   					ligne4=Ligne4,
   					ligne5=Ligne5,
   					ligne6=Ligne6)
if __name__ == '__main__':
   app.run()


