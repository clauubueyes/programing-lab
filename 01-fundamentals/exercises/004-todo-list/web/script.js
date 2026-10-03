const form = document.getElementById("add-task");
const taskInput = document.getElementById("title-task");
const taskList = document.getElementById("tasks");
const errorMessage = document.getElementById("error");

const tasks = [];
function addTask(tasks, taskTitle){
    const task = {
        title: taskTitle,
        completed: false
    };
    tasks.push(task);
    return task;
}
function createTaskElement(newTask) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    span.textContent = `[ ] ${newTask.title}`;
    li.append(span);
    return {
        li: li,
        span: span
    };
}
function toggleTask(newTask) {
    newTask.completed = !newTask.completed;
}
function updateTaskElement(newTask, span) {
    if(newTask.completed){
        span.textContent = `[x] ${newTask.title}`;
    }
    else{
        span.textContent = `[ ] ${newTask.title}`;
    }
}
function deleteTask(tasks, newTask) {
    const index = tasks.indexOf(newTask);
    tasks.splice(index, 1);
}
function createCompleteButton(newTask, span) {
    const completeButton = document.createElement("button");
    completeButton.textContent = "complete";
    completeButton.addEventListener("click", function(){
        toggleTask(newTask);
        updateTaskElement(newTask, span);
    });
    return completeButton;
}
function createDeleteButton(tasks, newTask, li){
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "delete";
    deleteButton.addEventListener("click", function(){
        deleteTask(tasks, newTask);
        li.remove();
    });
    return deleteButton;
}
form.addEventListener("submit", function(event){
    event.preventDefault();

    const task = taskInput.value.trim(); 
    
    if (task ===""){
        errorMessage.textContent="You cannot enter an empty task.";
    }
    else{
        errorMessage.textContent="";
        const newTask = addTask(tasks, task);
        const {li, span} = createTaskElement(newTask);
        
        const completeButton = createCompleteButton(newTask, span);
        const deleteButton = createDeleteButton(tasks, newTask, li);
        
        li.append(completeButton);
        li.append(deleteButton);
        taskList.append(li);
        taskInput.value = "";
    }
});
{/*
const tasks = [];
function addTask(tasks, taskTitle){
    const task = {
        title: taskTitle,
        completed: false
    };
    tasks.push(task);
}


function showTasks(tasks){
    for (let i=0; i<tasks.length ; i++){
    let res = "";
    if(tasks[i].completed){
        res = `${i + 1}. [x] ${tasks[i].title}`;
    }
    else{
        res = `${i + 1}. [ ] ${tasks[i].title}`;
    } 
    console.log(res); 
    }
}
function isValidTask(tasks, indexInput){
    const index = indexInput - 1 ;
    return !(index < 0 ||index >= tasks.length || Number.isNaN(index))
}
function  completeTask(indexInput, tasks){
    const index = indexInput - 1 ; 
    tasks[index].completed = true;
}
function deleteTask(indexInput, tasks){
    const index = indexInput - 1;
    tasks.splice(index, 1);
}

let running = true; 
while(running){
    console.log("1. Add task\n2. Show tasks\n3. Complete task\n4. Delete task\n5. Exit");
    const option = Number(prompt("Enter an option: "));
    switch ( option){
        case 1: 
            const taskEnter = prompt("Enter a task: ");
            addTask(tasks, taskEnter);
            break;
        case 2: 
            showTasks(tasks);
            break;
        case 3: 
            const completeIndex = Number(prompt("Enter the number of the task to complete: "));
            if (isValidTask(tasks, completeIndex )) {
                completeTask(completeIndex, tasks);
            }else{
                console.log("That task does not exist.");
            }
            showTasks(tasks);
            break;
        case 4: 
            const popIndex = Number(prompt("Enter the number of the task to delete: "));
            if (isValidTask(tasks, popIndex )) {
                deleteTask(popIndex, tasks);
            }else{
                console.log("That task does not exist.");
            }
            showTasks(tasks);
            break;
        case 5: 
            console.log("Bye!");
            running = false;
            break;     
        default: 
            console.log("Invalid option");  
            break;     
    }
}

*/}
