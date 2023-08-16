async function getCategories() {
    const request = await fetch(`http://${window.location.hostname}:${window.location.port}/api/v1/book/categories`);
    const categories = await request.json();

    categories.forEach(category => CategoriesToHTML(category))
}

function CategoriesToHTML({
                                id,
                                category,
                          }) {
    let categories = document.getElementById('category_drop_menu')

    categories.insertAdjacentHTML('beforeend', `
        <li style="border-width: medium">
            <div class="btn-group dropend d-flex justify-content-between mb-1">
                <a class="dropdown-item btn menu btn-lg"
                    href="http://${window.location.hostname}:${window.location.port}/book/catalog/?category=${category}" 
                    type="button">${category}</a>
                <ul class="dropdown-menu bg-secondary p-1 bg-opacity-75 ms-1" id="${category}"
                        style="border: 1px solid black">                    
                </ul>
            </div>
        </li>
    `)
}


window.addEventListener('DOMContentLoaded', getCategories);
