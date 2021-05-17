function check(){
    var q1 = document.quiz.q1.value;
    var q2 = document.quiz.q2.value;
    var q3 = document.quiz.q3.value;
    var score = 0;

        if(q1 == "Random Access Memory"){
            score++;
        }
        if(q2 == "16 GB 4400mhz"){
            score++;
        }
        if(q3 == "Volatile"){
            score++;
        }

    document.getElementById("submission").style.visibility = "visible"
    document.getElementById("user_score").innerHTML = "You scored: " + score;
}