function elementHasTextOnly(el){
    return el.childElementCount === 0 && Array.from(el.childNodes).length === 1
}