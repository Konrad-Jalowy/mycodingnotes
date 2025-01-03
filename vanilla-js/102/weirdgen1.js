//weird but works...
function ajax(url) {

    let xhr = new XMLHttpRequest();

    xhr.open("GET", url);

    return xhr;

}

function *showData(url) {

    let result = yield ajax(url);

    document.querySelector("#para").textContent = result;

}

function makeRequest(url, gen) {

    let it = gen(url);

    let xhr = it.next().value;

    xhr.onload = function() {
        if(xhr.status === 200) {
            it.next(xhr.responseText);
        }
    };

    xhr.send();

}

makeRequest("https://api.chucknorris.io/jokes/random", showData);