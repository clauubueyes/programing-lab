const textInput = document.getElementById("input");
const characterCounter = document.getElementById("character-counter");

textInput.addEventListener("input", function(){
    const textForm = textInput.value;
    const length = textForm.length;

    characterCounter.textContent = `${length}`;
});