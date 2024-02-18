import os
import pygame

pygame.init()
pygame.mixer.init()

def play_song(filename):
    clock = pygame.time.Clock()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(10)  # Check playback status every 100ms

def main():
    songs = [f for f in os.listdir() if f.endswith(('.mp3', '.wav', '.ogg'))]  # Find audio files
    if not songs:
        print("No audio files found!")
        return

    print("Available songs:")
    for i, song in enumerate(songs):
        print(f"{i+1}. {song}")

    choice = int(input("Enter song number: ")) - 1
    if 0 <= choice < len(songs):
        play_song(songs[choice])
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
