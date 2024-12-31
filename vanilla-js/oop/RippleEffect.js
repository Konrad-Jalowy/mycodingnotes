class RippleEffect {
    constructor() {
        const buttons = document.querySelectorAll("a.ripple-effect");
        for (const b of buttons) {
            this.addListenerToButton(b);
        }
    }

    addListenerToButton = (b) => {
        b.addEventListener("click", this.addRipple);
    }

    addRipple = (event) => {
        const button = event.currentTarget;
        const span = document.createElement("span");
        const size = Math.max(button.clientWidth, button.clientHeight);

        span.style.width = span.style.height = size + "px";

        const left = event.clientX - button.offsetLeft
                        + document.documentElement.scrollLeft ;
        span.style.left = left + "px";

        const top = event.clientY - button.offsetTop
                        + document.documentElement.scrollTop;
        span.style.top = top + "px";
        
        span.classList.add("ripple-el");

        setTimeout(() => {
            span.remove();
        }, 650);
        
        button.appendChild(span);
    }
}

const rippleEffect = new RippleEffect();