async function getBook(book_id) {
    const res_book = await fetch(`http://${window.location.hostname}:8000/api/v1/book/book_for_detail/${book_id}/`);
    const book = await res_book.json();

    BookToHTML(book);
}


function BookToHTML({
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
    document.title = `${title}`
    const book_card = document.getElementById('book')

    let authors_list = []
    let categories_list = []

    for (const element of authors) {
        authors_list.push(element["author"])
    }
    for (const element of categories) {
        categories_list.push(element["category"])
    }

    if (!jacket){
        jacket = "http://127.0.0.1:8000/static/img/unknown_book.png"
    }

    if (!long_description){
        long_description = "Описание отсутствует"
    }
    if (!published_date){
        published_date = "Неизвестно"
    }

    authors = authors_list.join(", ")

    let urlCategories = categories_list.map(category => {
        return {
            name: category,
            url: `http://${window.location.hostname}:8000/book/catalog/?category=${category}`
        };
    });

    let clickableCategories = []

    for (let i = 0; i < urlCategories.length; i++) {
        clickableCategories.push(`<a href="${urlCategories[i]["url"]}" class="link-dark link-offset-2 
            link-underline-opacity-25 link-underline-opacity-100-hover"
            >${urlCategories[i]["name"]}</a>`)
    }

    clickableCategories = clickableCategories.join(", ")
    console.log(clickableCategories)

    book_card.insertAdjacentHTML('beforeend',`
        <div class="row justify-content-between p-5 clearfix ">
            <div class="col-4" id="general_photo" style="position: relative">     
                <img src="${jacket}" 
                    class="col-md-6 float-md-start mb-3 ms-md-3 cursor" alt="..." 
                    data-bs-toggle="modal" data-bs-target="#gph${id}"
                    style="width: 100%; max-width: 500px">
            </div>            
            <div class="col-7">
                <h5 class="card-title d-flex justify-content-between" id="book_card_title">${title}</h5>
                <ul class="list-group list-group-flush" style="height: 220px">                           
                    <li class="list-group-item">                            
                        Авторы: <b>${authors}</b>                     
                    </li>     
                    <li class="list-group-item">                            
                        Категории: <b>${clickableCategories}</b>                     
                    </li>           
                    <li class="list-group-item">                            
                        ISBN: <b>${isbn}</b>                  
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
                
                <div class="d-flex justify-content-between mt-1">
                    
                </div>
            </div>
            <h5>Описание:</h5>
            <p class="card-text">${long_description}</p>
        </div>
        
        <div class="modal fade" id="gph${id}" tabindex="-1" aria-labelledby="gph${id}" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-body">
                        <div class="d-flex justify-content-end mb-1">
                            <button type="button" class="btn-close" data-bs-dismiss="modal"
                            aria-label="Закрыть" style="outline: none;box-shadow: none"></button>
                        </div>
                        <img src="${jacket}" alt="..." style="width:100%;max-width:1400px"">
                    </div>                       
                </div>
            </div>
        </div>
    `)
}


let url = window.location.href.split('/');

if (url[url.length - 1] === '') {
    url = url[url.length - 2]
} else {
    url = url[url.length - 1]
}

getBook(url).then()

