$(document).ready(function() {
    getSearchBooks()
    $("#search_start").on('click', function () {
        getSearchBooks()
    })
})

function getSearchBooks(query_params = window.location.search) {
    let books_cards = $('#books_cards').empty()
    $('#pagination_ul').empty()
    books_cards.append(`
        <div class="d-flex justify-content-center">
            <div class="spinner-border" role="status"
                    style="width: 4rem; height: 4rem; color: cadetblue">
                <span class="visually-hidden">Загрузка...</span>
            </div>
        </div>
    `)

    let title = $("#input_book").val()
    let author = $("#input_author").val()
    let status = $("#status").val()

    if (!query_params){
        query_params += "?"
    }

    if (title) {
        query_params += `&title=${title}`
    }
    if (author) {
        query_params += `&author=${author}`
    }
    if (status !== "Null" && status) {
        query_params += `&status=${status}`
    }

    $.ajax({
        type: "GET",
        url: `http://${window.location.hostname}:${window.location.port}/api/v1/book/catalog/${query_params}`,
        dataType: "json",
        success: function (data) {
            let books_cards = $("#books_cards").empty()
            let pagination_ul = $('#pagination_ul').empty()

            if (data["count"] === 0) {
                books_cards.append(`
                    <h3>К сожалению, ничего не нашлось по вашему запросу =(</h3>
                `)
                return
            }
            data["results"].forEach(book => BooksToHTML(book))

            pagination_ul.append(`
                <li class="page-item" id="previous_page">
                    <a class="page-link" href="#" aria-label="Предыдущая">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
            `)

            let previous_page = $('#previous_page')
            if (data["page"] === 1) {
                previous_page.addClass("disabled")
            } else {
                previous_page.on('click', function () {
                    getSearchBooks(
                        `${query_params}&page=${data['page'] - 1}`)
                })
            }

            pagination_ul.append(`
                    <li class="page-item" id="page_1" >
                        <a class="page-link" href="#">1</a>
                    </li>
                `)
                if (1 === data['page']) {
                    $(`#page_1`).addClass('active')
                } else {
                    $(`#page_1`).on('click', function () {
                        getSearchBooks(
                            `${query_params}&page=1`)
                    })
                }
            if (data["page"] < 7){
                for (let page = 2; page <= data["page"]; ++page){
                        pagination_ul.append(`
                        <li class="page-item" id="page_${page}" >
                            <a class="page-link" href="#">${page}</a>
                        </li>
                    `)
                    if (page === data['page']) {
                        $(`#page_${page}`).addClass('active')
                    } else {
                        $(`#page_${page}`).on('click', function () {
                            getSearchBooks(
                                `${query_params}&page=${page}`)
                        })
                    }
                }
            }
            if (data["page"] >= 7){
                pagination_ul.append(`
                    <li class="page-item">
                        <a class="page-link" aria-label="Следующая" href="#" disabled>
                            <span aria-hidden="true">...</span>
                        </a>
                    </li>
                `)
                for (let page = data["page"] - 4; page <= data["page"]; ++page){
                        pagination_ul.append(`
                        <li class="page-item" id="page_${page}" >
                            <a class="page-link" href="#">${page}</a>
                        </li>
                    `)
                    if (page === data['page']) {
                        $(`#page_${page}`).addClass('active')
                    } else {
                        $(`#page_${page}`).on('click', function () {
                            getSearchBooks(
                                `${query_params}&page=${page}`)
                        })
                    }
                }
            }

            for (let page = data["page"] + 1; page <= data["total_page"] &&
                page < data['page'] + 6;
                 ++page) {
                pagination_ul.append(`
                    <li class="page-item" id="page_${page}" >
                        <a class="page-link" href="#">${page}</a>
                    </li>
                `)
                if (page === data['page']) {
                    $(`#page_${page}`).addClass('active')
                } else {
                    $(`#page_${page}`).on('click', function () {
                        getSearchBooks(
                            `${query_params}&page=${page}`)
                    })
                }
            }

            if (data['page'] + 5 < data["total_page"]){
                pagination_ul.append(`
                    <li class="page-item">
                        <a class="page-link" aria-label="Следующая" href="#" disabled>
                            <span aria-hidden="true">...</span>
                        </a>
                    </li>
                `)
                pagination_ul.append(`
                    <li class="page-item" id="page_${data["total_page"]}" >
                        <a class="page-link" href="#">${data["total_page"]}</a>
                    </li>
                `)
                $(`#page_${data["total_page"]}`).on('click', function () {
                        getSearchBooks(
                            `${query_params}&page=${data["total_page"]}`)
                    })
            }

            pagination_ul.append(`
                <li class="page-item" id="next_page">
                    <a class="page-link" aria-label="Следующая" href="#">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            `)

            let next_page = $('#next_page')
            if (data["page"] === data["total_page"]) {
                next_page.addClass("disabled")
            } else {
                next_page.on('click', function () {
                    getSearchBooks(
                        `${query_params}&page=${data['page'] + 1}`)
                })
            }
        }
    })
}


function BooksToHTML({
                        id,
                        title,
                        isbn,
                        page_count,
                        published_date,
                        jacket,
                        short_description,
                        long_description,
                        status,
                        authors,
                        categories,
                     }) {
    const booksList = document.getElementById('books_cards');
    let authors_list = []
    let categories_list = []

    for (const element of authors) {
        authors_list.push(element["author"])
    }
    for (const element of categories) {
        categories_list.push(element["category"])
    }

    if (!jacket){
        jacket = `http://${window.location.hostname}:${window.location.port}/static/img/unknown_book.png`
    }

    if (!short_description){
        short_description = "Описание отсутствует"
    }
    if (!published_date){
        published_date = "Неизвестно"
    }

    authors = authors_list.join(", ")
    categories = categories_list.join(", ")

    booksList.insertAdjacentHTML('beforeend',`
        <div class="col-sm-4 mb-4" style="height: 700px;">
            <div class="card" id="good_${id}">
                <a class="d-flex justify-content-center"
                        style="height: 200px; padding: 20px; align-items: center; justify-content: center"  id="img_${id}"
                        href="http://${window.location.hostname}:${window.location.port}/book/${id}">
                    <img src="${jacket}" 
                     alt="Превью" style="max-width: 100%; max-height: 100%;">
                </a>                
                <div class="card-body">                    
                        <h5 class="product-title card-title" style="white-space: nowrap; overflow: hidden;
                         text-overflow: ellipsis; transform: rotate(0);">${title}
                            <a href="http://${window.location.hostname}:${window.location.port}/book/${id}"
                            class="stretched-link"></a>
                         </h5>
                        <p class="card-text" style="height: 55px; overflow: hidden;
                                text-overflow: ellipsis;">
                            ${short_description}
                        </p>
                    
                    <ul class="list-group list-group-flush" style="height: 220px">                           
                        <li class="list-group-item">                            
                            Авторы: <b>${authors}</b>                     
                        </li>     
                        <li class="list-group-item">                            
                            Категории: <b>${categories}</b>                     
                        </li>           
                        <li class="list-group-item">                            
                            Дата публикации: <b>${published_date}</b>                     
                        </li>
                        <li class="list-group-item">                            
                            Статус: <b>${status}</b>                     
                        </li>
                        <li class="list-group-item">                            
                            Количество страниц: <b>${page_count}</b>                     
                        </li>        
                    </ul>
                </div>
                <div class="card-body d-flex justify-content-between mt-5">
                    <p>ISBN: ${isbn}</p>
                    <a href="http://${window.location.hostname}:${window.location.port}/book/${id}" 
                        class="btn menu btn-outline-dark">ТЫК</a>
                </div>
            </div>
        </div>
    `);
}

function getQueryParams(param) {
    const query = window.location.search.substring(1);
    const params = query.split("&");

    for (let i = 0; i < params.length; i++) {
        let pair = params[i].split("=");
        if (pair[0] === param){ return pair[1] }
    }

    return false;
}

let new_title = getQueryParams("category")

if (new_title){
    let old_title = document.title
    document.title = decodeURI(`${old_title} - ${new_title}`)
}
