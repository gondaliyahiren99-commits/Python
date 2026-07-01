document.addEventListener('DOMContentLoaded', () => {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize Popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Bookmark Toggle Logic
    const bookmarkBtns = document.querySelectorAll('.bookmark-btn');
    bookmarkBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const icon = this.querySelector('i');
            if (icon.classList.contains('bi-bookmark')) {
                icon.classList.remove('bi-bookmark');
                icon.classList.add('bi-bookmark-fill', 'text-primary');
                showToast('Job saved to your profile.');
            } else {
                icon.classList.remove('bi-bookmark-fill', 'text-primary');
                icon.classList.add('bi-bookmark');
                showToast('Job removed from saved list.');
            }
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                navbar.classList.add('shadow-sm');
                navbar.style.background = 'rgba(255,255,255,0.98)!important';
            } else {
                navbar.classList.remove('shadow-sm');
                navbar.style.background = 'rgba(255,255,255,0.9)!important';
            }
        });
    }
});

// Global Toast Notification
function showToast(message, type = 'success') {
    // Create toast container if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(toastContainer);
    }

    const toastId = 'toast-' + Math.random().toString(36).substr(2, 9);
    
    // Icon based on type
    let iconClass = 'bi-check-circle-fill text-success';
    if(type === 'error') iconClass = 'bi-exclamation-triangle-fill text-danger';

    const toastHTML = `
        <div id="${toastId}" class="toast align-items-center bg-white border-0 shadow-lg slide-up" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body d-flex align-items-center gap-2">
                    <i class="bi ${iconClass} fs-5"></i>
                    <span class="fw-medium">${message}</span>
                </div>
                <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    `;

    toastContainer.insertAdjacentHTML('beforeend', toastHTML);
    const toastElement = document.getElementById(toastId);
    const toast = new bootstrap.Toast(toastElement, { delay: 3000 });
    toast.show();

    // Clean up DOM after hide
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove();
    });
}
