function filtrar() {
    var texto = document.getElementById("filtro").value.toLowerCase();
    var cards = document.querySelectorAll(".card");

    cards.forEach(function(card){
        var titulo = card.querySelector("h2").innerText.toLowerCase();

        if (titulo.includes(texto)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}