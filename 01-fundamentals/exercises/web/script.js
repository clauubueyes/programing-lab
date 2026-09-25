const inputName = document.getElementById("fname");
const inputBirthdate= document.getElementById("birthdate");
const dataForm = document.getElementById("ageCalculatorForm");

dataForm.addEventListener("submit", function(event){
    event.preventDefault();

    const name = inputName.value; 
    const birthdate = inputBirthdate.value;

    console.log(name);
    console.log(birthdate);
});