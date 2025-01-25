document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');
    const vmName = document.getElementById('vm-name');

    // Display the virtual machine name
    vmName.textContent = 'Running on VM: ' + window.location.hostname;

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const taskInput = document.getElementById('task-input');
        const taskName = taskInput.value.trim();

        if (taskName) {
            const listItem = document.createElement('li');
            listItem.textContent = taskName;
            taskList.appendChild(listItem);
            taskInput.value = '';
        }
    });
});