from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

media_player = QMediaPlayer()
url = QUrl.fromLocalFile("/home/gruand69/Dev/english/media/dialog1/1.mp3")
content = QMediaContent(url)
media_player.setMedia(content)
media_player.play()