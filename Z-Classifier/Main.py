import pandas as pd
from os import system
from time import sleep
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

LB = LabelEncoder()
KNN = KNeighborsClassifier(n_neighbors=3)
RFC = RandomForestClassifier()

SYMPTOMS = pd.read_csv('SYMPTOMS.csv')
X1 = SYMPTOMS.drop('Result', axis=1)
Y1 = SYMPTOMS.Result

X1['skin_tone'] = LB.fit_transform(X1['Old_skin_tone'])
X1['eye_color'] = LB.fit_transform(X1['Old_eye_color'])
X1['mental_health'] = LB.fit_transform(X1['Old_mental_health'])
X1 = X1.drop(['Old_skin_tone', 'Old_eye_color', 'Old_mental_health'], axis=1)
RFC.fit(X1, Y1)

TYPE = pd.read_csv('TYPE.csv')
X2 = TYPE.drop('Result', axis=1)
Y2 = TYPE.Result
KNN.fit(X2, Y2)

system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
print('[0] Comum')
sleep(0.5)
print('[1] Acinzentado')
sleep(0.5)
print('[2] Pálida\n')
sleep(1)
ST = int(input("[Número] Como está a cor de pele do paciente?: "))

system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
print('[0] Comum')
sleep(0.5)
print('[1] Esmeralda')
sleep(0.5)
print('[2] Vermelho')
sleep(0.5)
print('[3] Branco\n')
sleep(1)
YC = int(input("[Número] Qual a cor dos olhos do paciente?: "))

system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
print('[0] Ruim')
sleep(0.5)
print('[1] Bom')
sleep(0.5)
print('[2] Horrivel\n')
sleep(1)
MH = int(input("[Número] Como está o estado mental do paciente?: "))

system('cls')
RESULT = RFC.predict([[ST,YC,MH]])
system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
print(f'Resultado[{RESULT[0]}]')
sleep(0.5)
print(f'Precisão[{RFC.score(X1, Y1)}]\n')
sleep(1)
if RESULT[0] == 'Zombie':
    input('[NÚMERO/TEXTO] Continuar: ')

elif RESULT[0] == 'Infected':
    print('Seja cuidadoso, o paciente pode se transformar em um zumbi a qualquer momento...')
    exit()

elif RESULT[0] == 'Human':
    print('O paciente não foi infectado...')
    exit()

system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
TL = float(input("[Número] Qual o tamanho dos dentes do zumbi?: "))
if TL > 3.5: TL = 3.5
sleep(0.5)
NL = float(input("[Número] Qual o tamanho das unhas do zumbi?: "))
if NL > 4.5: NL = 4.5
sleep(0.5)
EW = float(input("[Número] Qual a largura das orelhas do zumbi?: "))
if EW > 8.5: EW = 8.5
sleep(0.5)

system('cls')
RESULT = KNN.predict([[TL,NL,EW]])
system('cls')

print('[SmarTech] - [Z-Classifier]\n')
sleep(1)
print(f'Resultado[{RESULT[0]}]')
sleep(0.5)
print(f'Precisão[{KNN.score(X2, Y2)}]\n')
sleep(1)
print('[Processo de contenção iniciado]')