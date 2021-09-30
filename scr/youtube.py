from os import stat


try:
    import multiplat as mp
    import backend as be
except:
    print("Biblioteca necessária não disponível.\n\nEstamos finalizando.")
    quit()

try:
    from IPython.display import YouTubeVideo
except:
    mp.install_lib("IPython")
    mp.restart_program()

try:
    from googleapiclient.discovery import build
except:
    mp.install_lib("google-api-python-client")
    mp.restart_program()

class YouTube:
    def __init__(self, chaveAPI):
        self.yt = build('youtube','v3', developerKey=chaveAPI)

    def getVideoData(self, videoURL):
        videoID = YouTube.extraiArgumento(videoURL, 'v')
        statistics = self.yt.videos().list(part='statistics', id=videoID).execute()
        snippet = self.yt.videos().list(part='snippet', id=videoID).execute()
        #return statistics, snippet
        data = {}
        data['url'] = videoURL
        data['visualizacoes'] = statistics['items'][0]['statistics']['viewCount']
        data['likes'] = statistics['items'][0]['statistics']['likeCount']
        data['deslikes'] = statistics['items'][0]['statistics']['dislikeCount']
        data['comentarios'] = statistics['items'][0]['statistics']['commentCount']
        data['publicacao'] = snippet['items'][0]['snippet']['publishedAt']
        data['canalid'] = snippet['items'][0]['snippet']['channelId']
        data['titulo'] = snippet['items'][0]['snippet']['title']
        #data['resolucao'] = f"{snippet['items'][0]['snippet']['thumbnails']['maxres']['width']}x{snippet['items'][0]['snippet']['thumbnails']['maxres']['height']}"
        data['categoria'] = snippet['items'][0]['snippet']['categoryId']
        #data['idioma'] = snippet['items'][0]['snippet']['defaultLanguage']
        return data
    
    @staticmethod
    def extraiArgumento(url, argumento_localizar): #localiza um argumento na URL
        index_inicial = url.find("?") + 1 #localiza o '?' primeiro, evitando que o texto inicial da URL atrapalhe
        index_inicial += url[index_inicial:].find(argumento_localizar) + len(argumento_localizar) + 1
        index_final = url[index_inicial:].find("&") + index_inicial
        if(index_inicial > index_final):#caso não seja encontrado o '&' a função find retorna -1, e essa condição será atendida
            index_final = len(url)
        return url[index_inicial:index_final]
