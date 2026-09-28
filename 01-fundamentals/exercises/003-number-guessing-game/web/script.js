const inputNumber = document.getElementById("input-number");
const dataForm = document.getElementById("numberGuessForm")

function randomNumber(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
const machineNumber = randomNumber(1,100);

dataForm.addEventListener("submit", function(event){
    event.preventDefault();

    const userNumber = parseInt(inputNumber.value);
    console.log(typeof(userNumber));

    if(userNumber < machineNumber){
        console.log("Too Low!");
    }
    else if (userNumber > machineNumber){
        console.log("Too High!");
    }
    else{
        console.log("You Win!");
    }
});