const inputNumber = document.getElementById("input-number");

function randomNumber(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
const machineNumber = randomNumber(1,100);
console.log(machineNumber);