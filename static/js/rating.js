function addStarsNav(div, rating_rounded){
    for(i=0; i<rating_rounded; i++){
        let star = document.createElement("span");
        star.classList.add("fa")
        star.classList.add("fa-star")
        star.classList.add("checked")
        div.appendChild(star)
    }
    for(i=0; i<5-rating_rounded; i++){
        let star = document.createElement("span");
        star.classList.add('fa')
        star.classList.add('fa-star')
        div.appendChild(star)
    }
}
function load_stars(avg_rating){

    const rating_rounded = Math.round(avg_rating)

    const stars = document.getElementById("stars")
    addStarsNav(stars, rating_rounded)
}

var rating = document.getElementById("rating-number").innerHTML

load_stars(rating)