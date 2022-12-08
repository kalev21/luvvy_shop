window.onscroll = () => {
    const header = document.querySelector('.header');
    const Y = window.scrollY

    if(Y > 300) {
        header.classList.add('header_fixed');
    } else if (Y < 100) {
        header.classList.remove('header_fixed');
    }
};
