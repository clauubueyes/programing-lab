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

for (let i=0; i<tasks.length ; i++){
    const res = `${i + 1}. [] ${tasks[i].title}`;
    console.log(res); 
}