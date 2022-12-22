import audio_effects as ae
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play_sound



in_path = 'QA0101.mp3'
ex_path = 'QA0101_slower.mp3'
sound = AudioSegment.from_file(in_path)    

speed_change_ratio = 0.7
slower_sound = ae.speed_down(sound, speed_change_ratio)

slower_sound.export(ex_path, format="mp3")
