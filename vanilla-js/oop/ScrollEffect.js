class ScrollEffect {
    constructor() {
        const links = document.querySelectorAll('a[href^="#"]');
        for (const link of links) {
            this.addListenerToLink(link);
        }
    }

    addListenerToLink = (link) => {
       link.addEventListener("click", this.addScrollEffect);
    }

    addScrollEffect = (e) => {
        e.preventDefault();
        const anchor = e.target.getAttribute('href');
        document.querySelector(anchor).scrollIntoView({
            behavior: 'smooth'
        });
    }
}