import gdown

google_drive_links = ['https://drive.google.com/file/d/1SoVhR2FheMH9NwOsfMiD6OpEuEHVm_ez/view?usp=share_link']

def Load_video():
    """This load video from google drive and save it to data/row directory"""

    for i, link in enumerate(google_drive_links):
        print(link)
        output= 'data/row/video/emotion'+ str(i)+'.mp4'
        gdown.download(link, output, quiet=False)
