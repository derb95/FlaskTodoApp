document.addEventListener("DOMContentLoaded", () => {
    console.log("Flask Todo App Loaded!");
});

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
