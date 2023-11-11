from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        """Initialize a PhotoAlbum with a given number of pages."""
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        """Create a PhotoAlbum based on the total number of photos."""
        return cls(ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        """Add a photo to the album and return a success message or a no-free-slots message."""
        for i, page in enumerate(self.photos):
            if len(page) < self.MAX_PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"

        return "No more free slots"

    def display(self) -> str:
        """Display the contents of the photo album in a visually appealing format."""
        separator = "-" * 11 + "\n"
        album_content = [" ".join("[]" for _ in page) + "\n" + separator for page in self.photos]
        return separator + "".join(album_content).strip()


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
#
