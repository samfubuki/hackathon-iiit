console.log(a);
console.log(b);
console.log(`${a}.html`);

let questions = [
    {
      id: 1,
      question: "Did you travel outside in past 7 days ?",
      answer: "Yes",
      options: [
        "Yes",
        "No"
      ]
    },
    {
      id: 2,
      question: "Do you have cough or pain in throat?",
      answer: "Yes",
      options: [
        "Yes",
        "No"
      ]
    },
    {
      id: 3,
      question: "Do you have any body ache ?",
      answer: "Yes",
      options: [
        "Yes",
        "No"
      ]
    },
    {
      id: 4,
      question: "Do you have any breathing problem?",
      answer: "Yes",
      options: [
        "Yes",
        "No"
      ]
    },
    {
      id: 5,
      question: "what is your body temperature ?",
      answer: "",
      options: [
        "<= 98.7",
        "99-100",
        "100-102",
        ">= 102"
      ]
    }, 
    {
      id: 6,
      question: "Current oxygen level ?",
      answer: "",
      options: [
        ">=95%",
        "90-95%",
        "< 90%"
      ]
    },
   
  ];
  
  let question_count = 0;
  
  window.onload = function() {
    show(question_count,questions[question_count].id);
  };
  
  
  let cnt =0;
  let ans=0;
  
  let x,y;
  
  function next() {
  
    let user_answer = document.querySelector("li.option.active").innerHTML;
    if(questions[question_count].id==5)
    {
        x=user_answer;
        console.log(x);
    }
    if(questions[question_count].id==6)
    {
        y=user_answer;
        console.log(y);
    }
    // if the question is last then redirect to final page
    if (question_count == questions.length - 1) {
        if(cnt>4 && (y=='&lt; 90%' || (x=='100-102' || x=='&gt;= 102')))
        {
          alert("You need a doctor!!!");
          
          document.location.href = `${a}`;
        }
        else{
          document.location.href = `${b}`;
        }
    }
    // check if the answer is right or wrong
    if (user_answer == questions[question_count].answer) {
      ans++;
      // sessionStorage.setItem("points", points);
    }
    // console.log(points);
  
    question_count++;
    show(question_count,questions[question_count].id);
  
    
    cnt++;
    if(cnt==4)
    {
      if(ans<=1)  //not affected
      {
        //redirect to the final page with some guidelines 
        // alert("Bach gaya bhai moz kar :)");
        document.location.href = `${b}`;

      }
    }
  }
  
  
  function show(count,id) {
    let question = document.getElementById("questions");
    if(id<=4){
        let [first, second] = questions[count].options;
  
        question.innerHTML = `
        <h2>Q${count + 1}. ${questions[count].question}</h2>
        <ul class="option_group">
        <li class="option">${first}</li>
        <li class="option">${second}</li>
      </ul> 
        `;
        toggleActive();
    }
    else if(id==5){
      let [first, second,third,fourth] = questions[count].options;
      question.innerHTML = `
      <h2>Q${count + 1}. ${questions[count].question}</h2>
      <ul class="option_group">
      <li class="option">${first}</li>
      <li class="option">${second}</li>
      <li class="option">${third}</li>
      <li class="option">${fourth}</li>
    </ul> 
      `;
      toggleActive();
    }
    else{
      let [first, second,third] = questions[count].options;
      question.innerHTML = `
      <h2>Q${count + 1}. ${questions[count].question}</h2>
      <ul class="option_group">
      <li class="option">${first}</li>
      <li class="option">${second}</li>
      <li class="option">${third}</li>
    </ul> 
      `;
      toggleActive();
    }
  }
  
  function toggleActive() {
    let option = document.querySelectorAll("li.option");
    for (let i = 0; i < option.length; i++) {
      option[i].onclick = function() {
        for (let i = 0; i < option.length; i++) {
          if (option[i].classList.contains("active")) {
            option[i].classList.remove("active");
          }
        }
        option[i].classList.add("active");
      };
    }
  }