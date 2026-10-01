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
    }else{
        res = `${i + 1}. [ ] ${tasks[i].title}`;
    } 
    console.log(res); 
}

}
const completeIndex = Number(prompt("Enter the number of the task to complete: "));
const indexTask = completeIndex - 1;

if (indexTask < 0 || indexTask >= tasks.length || Number.isNaN(completeIndex)) {
    console.log("That task does not exist.");
}else{
    tasks[indexTask].completed = true;

}
showTasks(tasks);

const popIndex = Number(prompt("Enter the number of the task to delete: "));
const popTask = popIndex - 1; 
if (popTask < 0 || popTask >= tasks.length || Number.isNaN(popIndex)) {
    console.log("That task does not exist.");
}else{
    tasks.splice(popTask, 1);
}

showTasks(tasks);