const inputNumber = document.getElementById("input-number");
const dataForm = document.getElementById("numberGuessForm")
const submitBotton = document.getElementById("submit-buton");
const hint = document.getElementById("hint")
const attempts = document.getElementById("attempts");

function randomNumber(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
const machineNumber = randomNumber(1,100);
 let count = 0;
dataForm.addEventListener("submit", function(event){
    event.preventDefault();

    const userNumber = parseInt(inputNumber.value);
    

    count = count + 1; 

    if(count === 5 && userNumber !== machineNumber){
         hint.textContent=`You lose! The number was ${machineNumber}`;
        submitBotton.disabled = true;
    }
    else{
        if (userNumber < machineNumber){
            hint.textContent = `Too Low!`;
        }
        else if (userNumber > machineNumber){
            hint.textContent=`Too High!`
        }
        else{
            hint.textContent=`You Win!`
            submitBotton.disabled = true;
        }
    }
   attempts.textContent=` ${5 - count}`;
});