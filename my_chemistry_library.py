import json
import streamlit as st

st.markdown("""
    <style>
        .header {
            background-color: lightgray;
            color: black;
            padding: 10px;
            text-align: center;
            font-size: 24px;
        }
    </style>
    <div class="header">THE PROJECT OF GIAIC</div>
""", unsafe_allow_html=True)

st.title('🧪My Chemistry Book library')

class MyChemistryBookCollection:
    

    def __init__(self):
        """Initialize a new book file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book from the user."""
        book_title = st.text_input("Enter book title:")
        book_author = st.text_input("Enter author:")
        publication_year = st.text_input("Enter publication year:")
        book_genre = st.text_input("Enter genre:")
        is_book_read = st.radio("Have you read this book?", ("yes", "no"))

        if st.button("Add Book"):
            new_book = {
                "title": book_title,
                "author": book_author,
                "year": publication_year,
                "genre": book_genre,
                "read": is_book_read == "yes",
            }
            self.book_list.append(new_book)
            self.save_to_file()
            st.success("Book added successfully!")

    def delete_book(self):
        """Remove a book by using its title."""
        book_title = st.text_input("Enter the title of the book to remove:")
        if st.button("Delete Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    self.book_list.remove(book)
                    self.save_to_file()
                    st.success("Book removed successfully!")
                    return
            st.warning("Book not found!")

    def find_book(self):
        
        search_type = st.radio("Search by:", ("Title", "Author"))
        search_text = st.text_input("Enter search term:").lower()

        if st.button("Search"):
            found_books = [
                book
                for book in self.book_list
                if search_text in book["title"].lower()
                or search_text in book["author"].lower()
            ]
            if found_books:
                st.write("Matching Books:")
                for index, book in enumerate(found_books, 1):
                    reading_status = "Read" if book["read"] else "Unread"
                    st.write(
                        f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                    )
            else:
                st.warning("No matching books found.")

    def update_book(self):
        """Modify the details."""
        book_title = st.text_input("Enter the title of the book you want to edit:")

        if st.button("Update Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    book["title"] = st.text_input(f"New title ({book['title']}):", value=book["title"])
                    book["author"] = st.text_input(f"New author ({book['author']}):", value=book["author"])
                    book["year"] = st.text_input(f"New year ({book['year']}):", value=book["year"])
                    book["genre"] = st.text_input(f"New genre ({book['genre']}):", value=book["genre"])
                    book["read"] = st.radio("Have you read this book?", ("yes", "no")) == "yes"
                    self.save_to_file()
                    st.success("Book updated successfully!")
                    return
            st.warning("Book not found!")

    def show_all_books(self):
        if not self.book_list:
            st.write("Your collection is empty.")
            return

        st.write("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            st.write(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )

    def show_reading_progress(self):
        """Calculate and display about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        st.write(f"Total books in collection: {total_books}")
        st.write(f"Reading progress: {completion_rate:.2f}%")

    def start_application(self):
        """Run the main user-friendly interface."""
        st.sidebar.title("Book Collection Menu")
        menu = ["Add a new book", "Remove a book", "Search for books", "Update book details", "View all books", "View reading progress"]
        choice = st.sidebar.radio("Select an option:", menu)

        if choice == "Add a new book":
            self.create_new_book()
        elif choice == "Remove a book":
            self.delete_book()
        elif choice == "Search for books":
            self.find_book()
        elif choice == "Update book details":
            self.update_book()
        elif choice == "View all books":
            self.show_all_books()
        elif choice == "View reading progress":
            self.show_reading_progress()


if __name__ == "__main__":
    book_manager = MyChemistryBookCollection()
    book_manager.start_application()


st.title("")

st.write("🧪This apps authorize, personal library not for public use")


footer = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #D3D3D3;
        text-align: center;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    <div class="footer">
        <p>Created by Engr M.Kamil Hanif | mkamilhanif789@gmail.com</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

