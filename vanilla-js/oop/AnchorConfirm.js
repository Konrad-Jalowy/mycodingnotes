class AnchorConfirm extends HTMLAnchorElement {
    connectedCallback(){
        this.addEventListener("click", function(e){
            if(!confirm("Do you want to leave this site?"))
                e.preventDefault();
        });
    }
}

customElements.define('custom-anchor', AnchorConfirm, {extends: 'a'});