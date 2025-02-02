// Add smooth transitions for task completion and deletion
document.addEventListener('DOMContentLoaded', function() {
    const taskItems = document.querySelectorAll('.task-item');

    taskItems.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.backgroundColor = '#e0e0e0';
        });

        item.addEventListener('mouseout', () => {
            item.style.backgroundColor = '#f9f9f9';
        });
    });
});