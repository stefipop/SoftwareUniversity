from project.album import Album
from typing import List


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for album in self.albums:
            if album.published:
                return "Album has been published. It cannot be removed."

            if album_name == album.name:
                self.albums.remove(album)

                return f"Album {album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self) -> str:
        result = [f"Band {self.name}"] + [a.details() for a in self.albums]

        return "\n".join(result)
