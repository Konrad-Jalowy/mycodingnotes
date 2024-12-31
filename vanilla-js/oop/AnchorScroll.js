class AnchorScroll extends HTMLAnchorElement {
    connectedCallback(){
        this.addEventListener("click", function(e){
            e.preventDefault();
            const anchor = this.getAttribute('href');
            document.querySelector(anchor).scrollIntoView({
                behavior: 'smooth'
            });
        });
    }
}

customElements.define('custom-anchor', AnchorScroll, {extends: 'a'});