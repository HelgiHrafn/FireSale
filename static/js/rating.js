function load_stars(avg_rating){

    const rating_rounded = Math.round(avg_rating)

    const stars = document.getElementById("stars")
    for(i=0; i<rating_rounded; i++){
        let star = document.createElement("span");
        star.classList.add("fa")
        star.classList.add("fa-star")
        star.classList.add("checked")
        stars.appendChild(star)
    }
    for(i=0; i<5-rating_rounded; i++){
        let star = document.createElement("span");
        star.classList.add('fa')
        star.classList.add('fa-star')
        stars.appendChild(star)
    }
}

const rating = document.getElementById("rating-number").innerHTML

load_stars(rating)