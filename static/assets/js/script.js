// Add smooth transitions for task completion and deletion
document.addEventListener('DOMContentLoaded', function () {
    const taskItems = document.querySelectorAll('.task-item');

    taskItems.forEach(task => {
        task.addEventListener('click', function (e) {
            if (e.target.classList.contains('complete-btn')) {
                task.classList.add('completed');
            } else if (e.target.classList.contains('delete-btn')) {
                task.style.transition = 'opacity 0.3s ease';
                task.style.opacity = '0';
                setTimeout(() => task.remove(), 300);
            }
        });
    });
});