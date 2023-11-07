function searchBooks() {
    input = document.getElementById("search-book-input");
    query = input.value.toLowerCase();
    window.location.href="/search?query=" + query;
}