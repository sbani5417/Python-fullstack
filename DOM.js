
const title = document.getElementById("title");
const input = document.getElementById("nameInput");
const button = document.getElementById("btn");
const output = document.getElementById("output");
button.addEventListener("click", function () {

    let name = input.value;

    output.innerText = "Hello " + name + " 👋";

    title.style.color = "purple";
});