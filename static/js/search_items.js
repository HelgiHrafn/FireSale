
$(document).ready(function() {
    $("#searchbar").keyup(function(event) {
    if (event.keyCode === 13) {
        $("#search_btn").click();
    }
    });
    $('#search_btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#searchbar').val(); //Sækja value i search bar
        $.ajax( {
            url: '/firesale?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) { // Populate-a gögnin hér
                var newHtml = resp.data.map(d => {

                    return `<div class="each item">
                                <a href="/firesale/${d.id}">
                                    <button class = button-single-item>
                                    <span class="image-container">
                                       <img class="item-sell-img" src="${d.firstImage}" alt="Image of iteam found via search query"/>
                                    </span>
                                    <span class="item-sell-name">${d.name}</span>
                                    <span class="item-sell-price">${d.price}</span>
                                    </button>
                                </a>
                            </div>`
                });
                $('.button-sell-all-items').html(newHtml.join(''));
                $('#searchbar').val('');
            },
            error: function(xhr,status,error) {
                // TODO: Nánari villuskýring
                console.error(error)
            }
        })
    });
});

