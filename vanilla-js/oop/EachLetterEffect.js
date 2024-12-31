class EachLetterEffect {
    constructor(){
        const headings = document.querySelectorAll('.each-letter-effect');
        for (const heading of headings) {
            this.turnContentToSpans(heading);
        }
    }

    turnContentToSpans(heading){
        const lettersArr = heading.textContent.split('');
        heading.innerHTML = '';
        heading.append(this.createSpansFromArr(lettersArr));
    }

    createSpansFromArr(arr){
        const fragment = new DocumentFragment();
        arr.map((letter, i) => {
        fragment.append(this.createSpanElement(letter, i));
        });
        return fragment;
    }

    createSpanElement(letter, i){
        const span = document.createElement("span");
        span.textContent = letter;
        span.style.transitionDelay = `${i*40}ms`;
        return span;
    }
}