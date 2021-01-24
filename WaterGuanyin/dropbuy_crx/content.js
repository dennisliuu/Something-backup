var div = document.createElement('div');
document.body.appendChild(div);
div.id = "dropbydiv"
div.style.width = '30%';
div.style.height = '30%';
div.style.position = 'fixed';
div.style.right = '2%';
div.style.bottom = '30%';
div.style.zIndex = '99';

var button = document.createElement('button');
document.body.appendChild(button);
button.id = "dropbybtn"
button.style.width = '10%';
button.style.height = '10%';
button.style.position = 'fixed';
button.style.right = '2%';
button.style.bottom = '2%';
button.style.zIndex = '99';
button.style.cursor = 'pointer';
button.style.outline = 'none';
button.style.border = 'none';
button.style.background = 'url("https://dropbuy.global/static/img/index-story-monster.0822557.png")'
button.style.backgroundSize = 'contain'
button.style.backgroundRepeat = 'no-repeat'

document.getElementById("dropbybtn").addEventListener("click", myFunction);

function decode(encodedString) {
    let tmpElement = document.createElement('span');
    tmpElement.innerHTML = encodedString;
    return tmpElement.innerHTML;
}

function myFunction() {
    div.innerText = "Waiting..."
    var xhr = new XMLHttpRequest();
    // xhr.open('POST', 'https://cors-anywhere.herokuapp.com/http://buy.testcat.ga/get-page-info', true);
    xhr.open('POST', 'http://127.0.0.1:6999/get-page-info', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
        let json = JSON.parse(decode(this.responseText))
        let new_table = ""
        new_table += '<table class="table table-sm table-dark"> <thead> <tr><th scope="col">名字</th> <th scope="col">價格</th> <th scope="col">描述</th> <th scope="col">圖片</th> </tr> </thead> <tbody> <tr>'
        new_table += `<td>${json.title}</td>`
        new_table += `<td>${json.price}</td>`
        let clean_json_description = document.createElement("div");
        clean_json_description.innerHTML = json.description;
        new_table += `<td>${clean_json_description.innerText.slice(0,150)}</td>`
        new_table += `<td><img src=${json.main_images} style="width: 80px"></td>`
        new_table += '</tr></tbody></table>'
        div.innerHTML = new_table
    };
    xhr.send('item_url=' + window.location.href)
}