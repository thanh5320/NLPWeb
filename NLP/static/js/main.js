var slide = document.querySelector(".slide");
var image = ["{% static 'image/wrg.png' %}","{% static 'image/tran.png' %}","{% static 'image/sum.png' %}","{% static 'image/post.png' %}"];

var i = image.length;

function next(){
    if(i<image.length){
        i = i+1;
    }
    else{
        i = 1;
    }
    slide.innerHTML ='<img src ="'+ image[i-1] +'">';
}

setInterval(next, 1500)