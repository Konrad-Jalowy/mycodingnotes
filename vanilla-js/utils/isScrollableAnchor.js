function isScrollableAnchor(el){
    return el.matches('a[href^="#"]') && (document.querySelector(el.getAttribute("href")) !== null);
}