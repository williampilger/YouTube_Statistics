# By: will.i.am | Bom Princípio - RS - Brasil
# 2021.09.28
try:
    import os
    from os import path
    import multiplat as mp
    import backend as be
    import time
    import youtube as yt
except:
    print("Biblioteca necessária não disponível.\n\nEstamos finalizando.")
    quit()

def inicio():
    mp.limpar_terminal()
    print(' By: will.i.am        ->      github.com/williampilger\n\n\n  ')
    inFile = input('Informe o nome do arquivo do qual deseja importar a lista de vídeos: ')
    outFile = inFile+".out.csv"
    sep = '\t'
    if(path.isfile(inFile)):
        conf = be.appConfig('config.ini')
        youtube = yt.YouTube(conf.get('chaveAPI'))
        with open(inFile, 'r') as arquivo:
            with open(outFile, 'w') as out:
                for linha in arquivo:
                    data = youtube.getVideoData(linha)
                    
                    lt = ''
                    for chave in data:
                        lt = f'{lt}{sep}{data[chave]}'
                    out.writelines(f'{lt}\n')

if __name__ == '__main__':
    inicio()
