import pygame # type: ignore
import vlc # type: ignore
import time
#function to play audio using pygame
def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.muic.play()

    #Wait until audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    #Function to play video using VLC
    def play_audio(video_file):
        #Initialize VLC instance
        instance = vlc.Instance()

        #Create meida player
        player=instance.media_player_new()

        #create a media object for tthe video
        media = instance.media_new(video_file)

        #Set meida to player
        player.set_media(media)

        #Play video
        player.play()

        #keep playing until video is finished
        while player.is_playing():
            time.sleep(1)

#            
