let sec5 = document.getElementById("sec5");

function mygreen() {
    document.body.style.backgroundColor = "green";
}

function myred() {
    document.body.style.backgroundColor = "red";
}
function myblue() {
    document.body.style.backgroundColor = "blue";
}
function mypink() {
    document.body.style.backgroundColor = "pink";
}
function myorange() {
    document.body.style.backgroundColor = "orange";
}

var tab1 = [];
var tab2 = [];
var tab3 = [];
var tab4 = [];

var n = 1;
var x = 0;

document.getElementById('hello').onclick = function AddRow()
{
    var Addn = document.getElementById('show');
    var NewRow = Addn.insertRow(n);
    tab1[x] = document.getElementById("fname").value;
    tab2[x] = document.getElementById("age").value;
    tab3[x] = document.getElementById("num").value;
    tab4[x] = document.getElementById("nw").value;

    var cell1 = NewRow.insertCell(0);
    var cell2 = NewRow.insertCell(1);
    var cell3 = NewRow.insertCell(2);
    var cell4 = NewRow.insertCell(3);

    cell1.innerHTML = tab1[x];
    cell2.innerHTML = tab2[x];
    cell3.innerHTML = tab3[x];
    cell4.innerHTML = tab4[x];
    n++;
    x++;
    

        
}

let fontbtn = document.querySelector('.fontbtn');
let btn = fontbtn.querySelectorAll('.btn');
for (var i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', function () {
        let cur = document.getElementsByClassName('active');
        cur[0].className = cur[0].className.replace("active", "");
        this.className += " active";
    })
}

const form = document.getElementById('my_form');

form.addEventListener('submit', function handleSubmit(event) {
    event.preventDefault();
    form.reset();
});

document.getElementById("save").onclick = function read()
{
   document.getElementById("charu").innerHTML=localStorage.getItem("form");
};

function write()
{
    localStorage.setItem("form", document.getElementById('charu').innerHTML);
}
