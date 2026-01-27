let employees=[];
let employeeList=document.getElementById('employee-list');
let form=document.getElementById('employee-form');
if(localStorage.getItem('employees')) {
    employees = JSON.parse(localStorage.getItem('employees'));
    displayEmployees();
}
form.addEventListener('submit', addEmployee);

function addEmployee(e) {
    e.preventDefault();

    let employeeId = document.getElementById('employee-id').value;
    let name = document.getElementById('name').value;
    let department = document.getElementById('department').value;
    let email = document.getElementById('email').value;
    let salary = document.getElementById('salary').value;

    if (!employeeId || !name || !department || !email || !salary) {
        alert('Please fill all fields');
        return;
    }

    if (!validateEmail(email)) {
        alert('Invalid email');
        return;
    }

    if (isNaN(salary)) {
        alert('Invalid salary');
        return;
    }

    let employee = {
        employeeId,
        name,
        department,
        email,
        salary
    };

    employees.push(employee);
    localStorage.setItem('employees', JSON.stringify(employees));
    displayEmployees();
    form.reset();
}

function displayEmployees() {
    employeeList.innerHTML = '';
    employees.forEach((employee, index) => {
        let row = `<tr>
            <td>${index + 1}</td>
            <td>${employee.employeeId}</td>
            <td>${employee.name}</td>
            <td>${employee.department}</td>
            <td>${employee.email}</td>
            <td>${employee.salary}</td>
            <td><button class="delete-btn" onclick="deleteEmployee(${index})">Delete</button></td>
        </tr>`;
        employeeList.innerHTML += row;
    });
}

function deleteEmployee(index) {
    if (confirm('Are you sure you want to delete this employee?')) {
        employees.splice(index, 1);
        localStorage.setItem('employees', JSON.stringify(employees));
        displayEmployees();
    }
}

function validateEmail(email) {
    let re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
}