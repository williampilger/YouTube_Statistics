# By: will.i.am | Bom Princípio - RS - Brasil
# 2021.09.28
try:
    import os
    from os import path
    import multiplat as mp
    import backend as be
    import time
    import youtube as yt
    import json
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
        lista = be.carregaStringArray(inFile)
        count = 1
        with open(outFile, 'w') as out:
            out.writelines(f'CONT\tURL\tVisualizações\tLikes\tDeslikes\tComentários\tData\tCanal\tTitulo\tCategoria\n')
            for linha in lista:
                try:
                    data = youtube.getVideoData(linha)
                    out.writelines(f'{count}')
                    for chave in data:
                        out.writelines(f'\t{data[chave]}')
                    out.writelines('\n')
                    print(json.dumps(data, indent=4), '\n')
                    count += 1
                except:
                    pass
                #lt = ''
                #for chave in data:
                #    lt = f'{lt}{sep}{data[chave]}'
                #out.writelines(f'{lt}\n')

if __name__ == '__main__':
    inicio()
