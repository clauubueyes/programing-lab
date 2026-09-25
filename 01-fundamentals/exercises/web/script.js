const inputName = document.getElementById("fname");
const inputBirthdate= document.getElementById("birthdate");
const dataForm = document.getElementById("ageCalculatorForm");


dataForm.addEventListener("submit", function(event){
    event.preventDefault();

    const currentDate = new Date();

    const currentYear = currentDate.getFullYear();
    const currentDay = currentDate.getDate();
    const currentMonth = currentDate.getMonth() + 1;

    const birthdate = new Date(inputBirthdate.value);

    const birthYear = birthdate.getFullYear() ; 
    const birthDay = birthdate.getDate();
    const birthMonth = birthdate.getMonth() + 1;

    console.log(birthYear);
    console.log(birthMonth);
    console.log(birthDay);
    console.log(birthdate);
    
    const name = inputName.value; 
    console.log(name);
});