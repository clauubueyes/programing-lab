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

const completeIndex = Number(prompt("Enter the number of the task to complete: "));
const indexTask = completeIndex - 1; 
tasks[indexTask].completed = true;

for (let i=0; i<tasks.length ; i++){
    let res = "";
    if(tasks[i].completed){
        res = `${i + 1}. [x] ${tasks[i].title}`;
    }else{
        res = `${i + 1}. [ ] ${tasks[i].title}`;
    } 
    console.log(res); 
}