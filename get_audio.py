import pafy
from pydub import AudioSegment
import os


def get_audio(url):
    try:
        pafy_obj = pafy.new(url=url)
    except Exception as _ex:
        return "Please check the URL!"
    
    author = pafy_obj.author
    title = pafy_obj.title


    best_audio = pafy_obj.getbestaudio()
    audio_ext = pafy_obj.getbestaudio().extension
    
    audio_file_name = f"{title}.{audio_ext}"
    
   
    best_audio.download()
    
    if audio_ext == "mp3":
        return f"{audio_file_name} downloaded successfully!"
    else:
        audio = AudioSegment.from_file(audio_file_name)
        audio.export(f"{title}.mp3", format="mp3")
        os.remove(os.path.abspath(audio_file_name))
        return f"{title}.mp3 downloaded successfully!"


def main():
   
    url = input("Please enter a URL: ")
    
    print(get_audio(url=url))
    
    
if __name__ == "__main__":
    main()
