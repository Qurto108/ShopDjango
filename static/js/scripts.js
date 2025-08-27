function performSearch() {
  const searchTerm = document.getElementById("searchInput").value.toLowerCase();
  const resultsContainer = document.getElementById("results");

  if (searchTerm.trim() === "") {
    resultsContainer.innerHTML =
      '<div class="no-results">Введите запрос для поиска</div>';
    return;
  }
  $.ajax({
    method: "GET",
    url: `/search?q=${searchTerm}`,
    success: function (response) {
      if (response["count"] == 0){
        resultsContainer.innerHTML = '<div class="no-results">Ничего не найдено</div>';
      } else {
        resultsContainer.innerHTML = null
        response['result'].forEach((product) => {
            let card = document.createElement('div')
            card.className = 'card'
            card.innerHTML = `
            <h4>${product['title']}<h4/>
            <p>${product['price']}<p/>
            `

            resultsContainer.appendChild(card)
        })
        
      }
    },
  });
}

// Поиск при нажатии Enter
document
  .getElementById("searchInput")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      performSearch();
    }
  });
