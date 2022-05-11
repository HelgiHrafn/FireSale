function load_stars(avg_rating){
    console.log(1)
    const pTag = document.getElementById("rating-number")
    const rating_text = document.createTextNode(avg_rating.toString())
    pTag.appendChild(rating_text)

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
load_stars(4.4)