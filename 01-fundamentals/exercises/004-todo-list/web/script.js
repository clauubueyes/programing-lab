const tasks = [];

while (true){
    const taskEnter = prompt("Enter a task: ");
    if( taskEnter === "q"){
        break;
    }
    const tasksUser = {
        title: taskEnter,
        completed: false
    };
    tasks.push(tasksUser);
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
const completeIndex = Number(prompt("Enter the number of the task to complete: "));
if (isValidTask(tasks, completeIndex )) {
    const indexTask = completeIndex - 1 ; 
    tasks[indexTask].completed = true;
}else{
    console.log("That task does not exist.");
}
showTasks(tasks);

const popIndex = Number(prompt("Enter the number of the task to delete: "));
if (isValidTask(tasks, popIndex )) {
    const popTask = popIndex - 1;
    tasks.splice(popTask, 1);
}else{
    console.log("That task does not exist.");
}

showTasks(tasks);