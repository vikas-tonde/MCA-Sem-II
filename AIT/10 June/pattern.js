function pattern1() {
    var n = 5, i, j;
    n = document.getElementById('p1').value;
    var op = "";
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= i; j++) {
            op += "* ";
        }
        op += "<br/>";
    }
    document.getElementById("p1op").innerHTML = op;
}

function pattern2() {
    var n = 5, i, j;
    n = document.getElementById('p2').value;
    var op = "";
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= (n - i); j++) {
            op += "&nbsp;&nbsp;";
        }
        for (j = 1; j <= i; j++) {
            op += "*";
        }
        op += "<br/>";
    }
    document.getElementById("p2op").innerHTML = op;
}

function pattern3() {
    var n = 5, i, j;
    n = document.getElementById('p3').value;
    var op = "";
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= (n - i); j++) {
            op += "&nbsp;&nbsp;";
        }
        for (j = 1; j <= i; j++) {
            op += "&nbsp;* ";
        }
        op += "<br/>";
    }
    document.getElementById("p3op").innerHTML = op;
}

function pattern4() {
    var n = 5, i, j;
    n = document.getElementById('p4').value;
    var op = "";
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= i; j++) {
            op += "&nbsp;&nbsp;";
        }
        for (j = 1; j <= (n - i) + 1; j++) {
            op += " *&nbsp;";
        }
        op += "<br>";
    }
    document.getElementById("p4op").innerHTML = op;
}


function pattern5() {
    var n, i, j;
    n = document.getElementById('p5').value;
    var op = "";
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j == Math.ceil(n / 2)) {
                op += "#&nbsp;";
            }
            else if (j == i || j == (n - i + 1)) {
                op += "*&nbsp;";
            }
            else {
                op += "&nbsp;&nbsp;";
            }
        }
        op += "<br/>";
    }

    var div = document.getElementById("p5op").innerHTML = op;
}