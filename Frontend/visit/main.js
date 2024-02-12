const hamb = document.querySelector("#hamb");
const popup = document.querySelector("#popup");
const menu = document.querySelector("#menu").cloneNode(1);
const body = document.body;

hamb.addEventListener("click", hamburgerHandler);

function hamburgerHandler(e) {
    e.preventDefault();
    popup.classList.toggle("open");
    hamb.classList.toggle("active");
    body.classList.toggle("noscroll")
    renderPopup();
}

function renderPopup() {
    popup.appendChild(menu);
}


function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Плавний перехід на початок сторінки
}