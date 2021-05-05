import os 
import speech_recognition as sr
import keyboard

def abrir(caminho):
    path = caminho
    path = os.path.realpath(path)
    os.startfile(path)


def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        microfone.pause_threshold = 0.5
        microfone.energy_threshold = 800
        audio = microfone.listen(source, None)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnkownValueError:
        print("Não entendi")
    return frase

def main():
    Materias = "c:/Users/andre/OneDrive/Área de Trabalho/USP/Materiais USP/Terceiro Semestre/"
    Caminhos = ["Calculo 3", "Computação para Automação", "Engenharia e Meio Ambiente", "Fisica 3", 
    "Fisica Experimental A", "Intro ao Projeto de Sistemas Mecanicos", "Mecanica 2", "Probabilidade"]
    keywords = ["cálculo", "computação", "meio ambiente", "física", "física experimental", "sistemas mecânicos","mecânica","probabilidade"]
    sair = ""


    print("ctrl+enter to start...")
    keyboard.wait('ctrl+enter')
    while True:
        pasta = ouvir_microfone()
        i = 0
        for palavra_chave in keywords:
            if pasta == palavra_chave:
                abrir(Materias + Caminhos[i])
            i += 1
        if pasta == "iniciação":
            abrir("c:/Users/andre/OneDrive/Área de Trabalho/USP/Materiais USP/IC")
        print("ctrl+enter to start...")
        keyboard.wait('ctrl+enter')

arquivo = open('config.txt','r')
conteudo =arquivo.readlines()
print(conteudo)