const inputName = document.getElementById("fname");
const inputBirthdate= document.getElementById("birthdate");
const dataForm = document.getElementById("ageCalculatorForm");

console.log(inputName);
console.log(inputBirthdate);
console.log(dataForm);

dataForm.addEventListener("submit", function(event){
    event.preventDefault();
    console.log("Funcion correcta");
});