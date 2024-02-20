const hamb = document.querySelector("#hamb");
const popup = document.querySelector("#popup");
const menu = document.querySelector("#menu").cloneNode(true); // Опція true для клонування вмісту
const body = document.body;

hamb.addEventListener("click", hamburgerHandler);

function hamburgerHandler(e) {
    e.preventDefault();
    popup.classList.toggle("open");
    hamb.classList.toggle("active");
    body.classList.toggle("noscroll");
    if (popup.classList.contains("open")) {
        renderPopup();
    } else {
        popup.innerHTML = ''; // Очистити вміст попапу при закритті
    }
}

function renderPopup() {
    popup.appendChild(menu);
}

// Додати обробник подій для закриття меню при кліку на хрестик
popup.addEventListener("click", function (e) {
    if (e.target.classList.contains("close")) {
        popup.classList.remove("open");
        hamb.classList.remove("active");
        body.classList.remove("noscroll");
        popup.innerHTML = ''; // Очистити вміст попапу при закритті
    }
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Плавний перехід на початок сторінки
}
