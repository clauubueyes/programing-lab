const tasks = [];

const task1 = {
    title: "Learning JS",
    completed: false
}; 
const task2 = {
    title: "Learning CSS",
    completed : false
};

tasks.push(task1, task2);


for (const task of tasks){
    const res = `Title: ${task.title}\n\nCompleted: ${task.completed}`;
    console.log(res); 
}