<script>
function addTask() {
    var taskText = document.getElementById("task").value;

    if (taskText === "") {
        alert("Please enter a task");
        return;
    }

    var li = document.createElement("li");
    li.innerText = taskText + " ";

    var delBtn = document.createElement("button");
    delBtn.innerText = "Delete";
    delBtn.onclick = function () {
        li.remove();
    };

    li.appendChild(delBtn);
    document.getElementById("todoList").appendChild(li);
    document.getElementById("task").value = "";
}
</script>