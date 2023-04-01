// 验证网址是否可以访问
function isUrlAvailable(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', url, false);
    xhr.send();
    return xhr.status == 200;
}

// 如果网站可以访问,文字背景变绿
function checkUrl() {
    var url = document.getElementById("url").value;
    if (isUrlAvailable(url)) {
        document.getElementById("url").style.backgroundColor = "green";
    } else {
        document.getElementById("url").style.backgroundColor = "red";
    }
}

// 对列表中的网址进行验证
function checkUrls() {
    // 获取网址列表
    
    var result = "";
    for (var i = 0; i < urls.length; i++) {
        if (isUrlAvailable(urls[i])) {
            result += urls[i] + " is available";  
        } else {
            result += urls[i] + " is not available";
        }
    }
    document.getElementById("result").value = result;
}
