song_list = "DRIVERS LICENSE, DON`T PLAY, AFTERGLOW, SWEET MELODY, AFTERGLOW, STREETS, AFTERGLOW, YOU BROKE ME FIRST"

played_songs = []

songs = song_list.split(", ")

for index in range(len(songs)):
    played_songs.append(songs[index])
    if played_songs.count(songs[index]) > 1:
        print(f"{index+1} {songs[index]} уже пели")
    else:
        print(f"{index+1} {songs[index]}")
