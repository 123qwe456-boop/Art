class ArtGallery:
    def __init__(self, gallery_name, location):
        """
        Parameterized constructor to initialize the gallery details.
        Automatically sets up an empty list to store artworks.
        """
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []  
        print(f"\n Welcome to '{self.gallery_name}' located in {self.location}!")

    def add_artwork(self, title, artist):
        """Method to add a new artwork to the collection."""
        artwork = {"title": title, "artist": artist}
        self.artworks.append(artwork)
        print(f" Success: '{title}' by {artist} has been added.")

    def view_artworks(self):
        """Method to display all artworks currently in the collection."""
        if not self.artworks:
            print("\nEmpty: There are currently no artworks in the collection.")
            return

        print(f"\n--- {self.gallery_name} Collection ---")
        for index, art in enumerate(self.artworks, start=1):
            print(f"{index}. \"{art['title']}\" — by {art['artist']}")
        print("-" * len(self.gallery_name))

    def search_artwork(self, search_title):
        """Method to search for an artwork by its title."""
        for art in self.artworks:
            if art['title'].lower() == search_title.lower():
                print(f" Found: \"{art['title']}\" by {art['artist']} is in the gallery.")
                return
        print(f" Not Found: \"{search_title}\" is not in our collection.")

    def __del__(self):
        """
        Destructor method called automatically when the object is deleted 
        or when the program finishes executing.
        """
        print(f"\n ArtGallery System Closing: Cleaning up and locking gates for '{self.gallery_name}'. Good-bye!")


def main():
    name = input("Enter the name of your Art Gallery: ")
    location = input("Enter the gallery location: ")
    my_gallery = ArtGallery(name, location)

    while True:
        print("\n=== Main Menu ===")
        print("1. Add Artwork")
        print("2. View Collection")
        print("3. Search for Artwork")
        print("4. Exit Program")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            title = input("Enter artwork title: ").strip()
            artist = input("Enter artist name: ").strip()
            if title and artist:
                my_gallery.add_artwork(title, artist)
            else:
                print(" Error: Title and Artist fields cannot be blank.")

        elif choice == '2':
            my_gallery.view_artworks()

        elif choice == '3':
            search_title = input("Enter the title of the artwork to search for: ").strip()
            if search_title:
                my_gallery.search_artwork(search_title)
            else:
                print(" Error: Search term cannot be blank.")

        elif choice == '4':
            print("\nExiting the Manager Application...")
            del my_gallery 
            break
        else:
            print(" Invalid Selection. Please pick a number from 1 to 4.")


if __name__ == "__main__":
    main()
