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

document.addEventListener("DOMContentLoaded", function () {
    var menu = document.getElementById("list_menu");
    var block = document.querySelector('.block2');
    var additionalMargin = 30;
    var offset = menu.offsetTop;
    var prev_offset = offset;

    function fixMenu() {
        if (window.pageYOffset > offset) {
            menu.classList.add("fixed");
        } else {
            menu.classList.remove("fixed");
        }
    }

    function handleScroll() {
        fixMenu();
        // Додаткова перевірка, чи користувач прокрутив сторінку вгору
        if (window.pageYOffset < offset) {
            menu.classList.remove("fixed");
            block.style.marginTop = "0px";
        } else {
            block.style.marginTop = (additionalMargin + 70) + "px";
            if (window.innerWidth < 500) {
                block.style.marginTop = (additionalMargin + 120) + "px";
            }
        }
    }

    function handleResize() {
        var windowWidth = window.innerWidth;

        if (windowWidth < 768) {
            menu.classList.remove("fixed");
            offset = menu.offsetTop;
            fixMenu();
            if(windowWidth < 450) {
                block.style.marginTop = (additionalMargin + 20 + 80) + "px";
            }
            block.style.marginTop = (additionalMargin + 80) + "px";
        }
        else {
            menu.classList.remove("fixed");
            offset = menu.offsetTop;
            fixMenu();

            // Встановлення різних значень block.style.marginTop в залежності від розміру екрану
            if (windowWidth < 992) {
                block.style.marginTop = (additionalMargin + 40) + "px";
            }
            else {
                block.style.marginTop = (additionalMargin + 70) + "px";
            }
        }
    }

    // Викликаємо функцію handleScroll при прокрутці сторінки
    window.addEventListener("scroll", handleScroll);

    // Викликаємо функцію handleScroll та handleResize при зміні розміру вікна
    window.addEventListener("resize", function () {
        handleScroll();
        handleResize();
    });
});

