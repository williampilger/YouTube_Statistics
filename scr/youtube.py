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

    def getVideoData(self, videoID):
        data = self.yt.videos().list(part='statistics', id=videoID).execute()
        data.update(self.yt.videos().list(part='snippet', id=videoID).execute())
        return data