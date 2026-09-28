const inputNumber = document.getElementById("input-number");
const dataForm = document.getElementById("numberGuessForm")
const submitBotton = document.getElementById("submit-buton");
const hint = document.getElementById("hint")
const attempts = document.getElementById("attempts");

function randomNumber(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
const machineNumber = randomNumber(1,100);

hint.classList.remove("warning", "success", "lose");

let count = 0;

dataForm.addEventListener("submit", function(event){
    event.preventDefault();

    const userNumber = parseInt(inputNumber.value);
    
    count = count + 1; 
    hint.classList.remove("warning");
    if(count === 5 && userNumber !== machineNumber){
        hint.textContent=`You lose! The number was ${machineNumber}`;
        hint.classList.add("lose");
        submitBotton.disabled = true;
    }
    else{
        if (userNumber < machineNumber){
            hint.textContent = `Too Low!`;
            hint.classList.add("warning");
        }
        else if (userNumber > machineNumber){
            hint.textContent=`Too High!`
            hint.classList.add("warning");
        }
        else{
            hint.textContent=`You Win!`
            hint.classList.add("success");
            submitBotton.disabled = true;
        }
    }
   attempts.textContent=` ${5 - count}`;
});