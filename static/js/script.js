document.addEventListener("DOMContentLoaded", () => {
    // Check for saved theme on load
    const savedTheme = localStorage.getItem('theme');
    const btn = document.getElementById('dark-mode-toggle');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        if (btn) btn.innerHTML = '<i class="fas fa-sun"></i> Light Mode';
    }
    console.log("Flask Todo App Loaded!");
});

function toggleDarkMode() {
    const body = document.body;
    const btn = document.getElementById('dark-mode-toggle');
    body.classList.toggle('dark-mode');
    
    // Save preference to localStorage and update button
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        if (btn) btn.innerHTML = '<i class="fas fa-sun"></i> Light Mode';
    } else {
        localStorage.setItem('theme', 'light');
        if (btn) btn.innerHTML = '<i class="fas fa-moon"></i> Dark Mode';
    }
}

function editProjectName(projectId, currentName) {
    // Hide the project name link and pencil icon
    const nameLink = document.getElementById(`project-link-${projectId}`);
    const pencilBtn = document.getElementById(`edit-pencil-${projectId}`);
    
    if (nameLink) nameLink.style.display = 'none';
    if (pencilBtn) pencilBtn.style.display = 'none';
    
    // Show the edit form
    const editForm = document.getElementById(`edit-form-${projectId}`);
    if (editForm) {
        editForm.style.display = 'inline-flex';
    }
}

function cancelEdit(projectId) {
    // Show the project name link and pencil icon
    const nameLink = document.getElementById(`project-link-${projectId}`);
    const pencilBtn = document.getElementById(`edit-pencil-${projectId}`);
    
    if (nameLink) nameLink.style.display = 'inline-block';
    if (pencilBtn) pencilBtn.style.display = 'inline-block';
    
    // Hide the edit form
    const editForm = document.getElementById(`edit-form-${projectId}`);
    if (editForm) {
        editForm.style.display = 'none';
    }
}

function editTaskName(taskId, taskName) {
    // Hide the task text and pencil icon
    const taskText = document.getElementById(`task-text-${taskId}`);
    const pencilBtn = document.getElementById(`edit-pencil-task-${taskId}`);
    const taskDesc = document.getElementById(`task-desc-${taskId}`);
    const taskDue = document.getElementById(`task-due-${taskId}`);
    
    if (taskText) taskText.style.display = 'none';
    if (pencilBtn) pencilBtn.style.display = 'none';
    if (taskDesc) taskDesc.style.display = 'none';
    if (taskDue) taskDue.style.display = 'none';
    
    // Show the edit form
    const editForm = document.getElementById(`edit-task-form-${taskId}`);
    if (editForm) {
        editForm.style.display = 'inline-flex';
    }
}

function cancelTaskEdit(taskId) {
    // Show the task text and pencil icon
    const taskText = document.getElementById(`task-text-${taskId}`);
    const pencilBtn = document.getElementById(`edit-pencil-task-${taskId}`);
    const taskDesc = document.getElementById(`task-desc-${taskId}`);
    const taskDue = document.getElementById(`task-due-${taskId}`);
    
    if (taskText) taskText.style.display = 'inline-block';
    if (pencilBtn) pencilBtn.style.display = 'inline-block';
    if (taskDesc) taskDesc.style.display = 'block';
    if (taskDue) taskDue.style.display = 'inline-block';
    
    // Hide the edit form
    const editForm = document.getElementById(`edit-task-form-${taskId}`);
    if (editForm) {
        editForm.style.display = 'none';
    }
}
