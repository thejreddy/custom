
  async function getQuestion() {
  k = getNumber() ;
console.log(k)

}


async function postData() {
  subcode = document.getElementById("subcode").innerHTML
  score=document.getElementById("score").innerHTML
  console.log(subcode)
  console.log(score)
  let datar = {
            "subcode": subcode,
            "score": score,
          }
  const url=''
    // Default options are marked with *
  const response = await fetch('http://127.0.0.1:8000/updatescore/', {

    method: "POST",
    headers:{
      'Accept': 'application/json',
     'Content-Type':'application/json',
     'X-Requested-With':'XMLHttpRequest'
    },
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(datar)

    // body data type must match "Content-Type" header
  }) .then(response => console.log(response))
}
async function getNumber() {
  let response = await fetch('http://127.0.0.1:8000/solomon/',{
    method: 'get',
    headers:{
      'X-Requested-With':'XMLHttpRequest',
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
  })
  let data = await response.json()

  set=[]
  j=0
  for(k=1;k<16;k++){
      a=100+k
      for(i=1;i<2;i++) {
      evalu=eval('data.scoresa[0].a'+a+i)
      if(evalu>1){
        set [j+1] =a*10+i
        j=j+1
      }

  }

  }
    console.log(set)
    let items = Array.from(set);
    jam= items[Math.floor(Math.random() * items.length)];
    console.log(jam)

    question_fetched=eval('data.a'+jam+'[0]'+'.quest')
    question_code=eval('data.a'+jam+'[0]'+'.questcode')
    option1_fetched = eval('data.a'+jam+'[0]'+'.option1')
    option2_fetched = eval('data.a'+jam+'[0]'+'.option2')
    option3_fetched = eval('data.a'+jam+'[0]'+'.option3')
    option4_fetched = eval('data.a'+jam+'[0]'+'.option4')
    option1_correct =eval('data.a'+jam+'[0]'+'.option1_correct')
    option2_correct =eval('data.a'+jam+'[0]'+'.option2_correct')
    option3_correct =eval('data.a'+jam+'[0]'+'.option3_correct')
    option4_correct =eval('data.a'+jam+'[0]'+'.option4_correct')

    document.getElementById("questdisp").innerHTML= question_fetched;
    document.getElementById("label1").innerHTML = option1_fetched;
    document.getElementById("label2").innerHTML = option2_fetched;
    document.getElementById("label3").innerHTML = option3_fetched;
    document.getElementById("label4").innerHTML = option4_fetched;
    document.getElementById("subcode").innerHTML = 'a'+jam;
    if (option1_correct)
    document.getElementById("span").innerHTML = 'a'+option1_correct;
    if (option2_correct)
    document.getElementById("span").innerHTML = 'b'+option2_correct;
    if (option3_correct)
    document.getElementById("span").innerHTML = 'c'+ option3_correct;
    if (option4_correct)
    document.getElementById("span").innerHTML = 'd'+option4_correct;

    document.getElementById('flexRadioDefault1').checked= false;
    document.getElementById('flexRadioDefault2').checked= false;
    document.getElementById('flexRadioDefault3').checked= false;
    document.getElementById('flexRadioDefault4').checked= false;

    postData();
    onTimesUp();
    
    startTimer();

}

window.onload = function() {
  var ex1 = document.getElementById('flexRadioDefault1');
  var ex2 = document.getElementById('flexRadioDefault2');
  var ex3 = document.getElementById('flexRadioDefault3');
  var ex4  = document.getElementById('flexRadioDefault4');


ex1.onclick = handler1;
ex2.onclick = handler2;
ex3.onclick = handler3;
ex4.onclick = handler4;
}



function scoreobtained(x){
  document.getElementById("score").innerHTML = x;
}

function handler1() {

  k = document.getElementById("span").innerHTML
  console.log(k)
  if(k=="atrue"){
document.getElementById("label1").innerHTML =document.getElementById("label1").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
scoreobtained(1);
}
else{
  document.getElementById("label1").innerHTML =document.getElementById("label1").innerHTML+ "<span class ='badge rounded-pill bg-warning text-dark'>Wrong</span>";

if(k=='btrue'){
  document.getElementById("label2").innerHTML= document.getElementById("label2").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
  scoreobtained(0);
}
if(k=='ctrue'){
    document.getElementById("label3").innerHTML= document.getElementById("label3").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);
}
if(k=='dtrue'){
    document.getElementById("label4").innerHTML= document.getElementById("label4").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);
}
}
}

function handler2() {
  k = document.getElementById("span").innerHTML
  console.log(k)
  if(k=="btrue"){
document.getElementById("label2").innerHTML =document.getElementById("label2").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
scoreobtained(1);
}
else{
  document.getElementById("label2").innerHTML =document.getElementById("label2").innerHTML+ "<span class ='badge rounded-pill bg-warning text-dark'>Wrong</span>";
if(k=='atrue'){
  document.getElementById("label1").innerHTML= document.getElementById("label1").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
  scoreobtained(0);
}
if(k=='ctrue'){
    document.getElementById("label3").innerHTML= document.getElementById("label3").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);
}
if(k=='dtrue'){
    document.getElementById("label4").innerHTML= document.getElementById("label4").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);
}
}
}


function handler3() {
  k = document.getElementById("span").innerHTML
  console.log(k)
  if(k=="ctrue"){
document.getElementById("label3").innerHTML =document.getElementById("label3").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
scoreobtained(1);
}
else{
  document.getElementById("label3").innerHTML =document.getElementById("label3").innerHTML+ "<span class ='badge rounded-pill bg-warning text-dark'>Wrong</span>";
if(k=='atrue'){
  document.getElementById("label1").innerHTML= document.getElementById("label1").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
  scoreobtained(0);

}
if(k=='btrue'){
    document.getElementById("label2").innerHTML= document.getElementById("label2").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);

}
if(k=='dtrue'){
    document.getElementById("label4").innerHTML= document.getElementById("label4").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);

}
}
}

function handler4() {
  k = document.getElementById("span").innerHTML
  console.log(k)
  if(k=="dtrue"){
document.getElementById("label4").innerHTML =document.getElementById("label4").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
scoreobtained(1);
}
else{
  document.getElementById("label4").innerHTML =document.getElementById("label4").innerHTML+ "<span class ='badge rounded-pill bg-warning text-dark'>Wrong</span>";
if(k=='atrue'){
  document.getElementById("label1").innerHTML= document.getElementById("label1").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
  scoreobtained(0);

}
if(k=='btrue'){
    document.getElementById("label2").innerHTML= document.getElementById("label2").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);

}
if(k=='ctrue'){
    document.getElementById("label3").innerHTML= document.getElementById("label3").innerHTML+ "<span class ='badge rounded-pill badge-success' >Correct</span>";
    scoreobtained(0);
}}}
