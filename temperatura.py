import requests
 
print("\t\tBem vindo a previsão do tempo!\n\n")
print("\t\tQual o nome da cidade desejada?!\n\n")
 
nome_cidade = input("Nome da cidade: ")
print("\n\n")

# Função para geração de um report
def Gerar_report(cidade):
    url = f'https://wttr.in/{cidade}'
    try:
        data = requests.get(url)
        desenho = data.text
    except Exception as e:
        desenho = "ERRO!"
        print(f'Erro: {e}')
    print(desenho)

def pegar_temperatura(cidade):
    url = (f'https://wttr.in/{cidade}?format=%t')
    try:    
        data = requests.get(url)
        temperatura_completa = data.text
        #temp = temperatura_completa.split('+')
        temp = temperatura_completa.split('°C')
        #temp = temp[1].split('°C')
        temperatura_final = temp[0]
        print(f'Temperatura completa: {temperatura_completa}')
        print(f'Temperatura digito: {temperatura_final}')
    except Exception as e:
        print(f'Erro: {e}')
    return(int(temperatura_final))
     
Gerar_report(nome_cidade)

temperatura = pegar_temperatura(nome_cidade)
print(temperatura)
if temperatura > 40:
    print(f'temperatura de {temperatura}°, está acabando o mundo!')
elif temperatura > 28:
    print(f'Temperatura de {temperatura}°, está calor, se hidrate!')
elif temperatura > 10:
    print(f'Temperatura de {temperatura}°, está um clima agradavel, use casaco e sinta a brisa.')
elif temperatura > 0:
    print(f'Temperatura de {temperatura}°, está frio, agasalhe-se bem!')
elif  temperatura < 0:
    print(f'Temperatura de {temperatura}°, está frio, muito frio...')
else:
    print(f'Temperatura invalida')