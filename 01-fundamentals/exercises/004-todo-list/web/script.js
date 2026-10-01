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

for (const task of tasks){
    const res = `Title: ${task.title}\nCompleted: ${task.completed}`;
    console.log(res); 
}