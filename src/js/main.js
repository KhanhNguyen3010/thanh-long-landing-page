import confetti from 'canvas-confetti';

window.openModal = function (modalId) {
    const modal = document.getElementById(modalId);
    const modalContent = document.getElementById(modalId + 'Content');

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    // Delay for animation
    setTimeout(() => {
        modal.classList.remove('opacity-0');
        if (modalContent) {
            modalContent.classList.remove('scale-95');
            modalContent.classList.add('scale-100');
        }
    }, 10);
    document.body.style.overflow = 'hidden';
};

window.closeModal = function (modalId) {
    const modal = document.getElementById(modalId);
    const modalContent = document.getElementById(modalId + 'Content');

    modal.classList.add('opacity-0');
    if (modalContent) {
        modalContent.classList.remove('scale-100');
        modalContent.classList.add('scale-95');
    }
    setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }, 300);
};

document.addEventListener('DOMContentLoaded', () => {
    // Setup click outside to close for all modals
    const modalIds = ['canadaModal', 'irelandModal', 'usaModal', 'litvaModal', 'consultModal', 'portugalModal', 'usaJ1Modal', 'usaF1Modal'];
    modalIds.forEach(id => {
        const modal = document.getElementById(id);
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    window.closeModal(id);
                }
            });
        }
    });

    // --- Google Sheets Integration ---
    // Thay bằng Web App URL của bạn sau khi Deploy Google Apps Script
    // Điền ID của Google Sheet khách hàng vào đây (Ví dụ: '1BxiMVs0XRYFgwnTE...').
    // Nếu để trống (''), dữ liệu sẽ chạy về file Sheet mặc định của bạn.
    const CLIENT_SHEET_ID = '';
    const GOOGLE_APP_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz2PLmCSzMrQ0I-0vQqIb-9ki271deaxwikOcN1A-88sKULLeWeYCqEwg5FlNmxa7rd/exec';

    window.handleFormSubmit = function (event) {
        event.preventDefault();
        const form = event.target;

        // Xóa thông báo lỗi cũ
        form.querySelectorAll('.error-msg').forEach(el => el.remove());
        form.querySelectorAll('.error-input').forEach(el => {
            el.classList.remove('error-input', '!border-red-500', '!text-red-600', '!ring-red-500/20');
        });
        form.querySelectorAll('.error-label').forEach(el => {
            el.classList.remove('error-label', '!text-red-500');
        });

        // Kiểm tra hợp lệ
        if (!form.checkValidity()) {
            const invalidInputs = form.querySelectorAll(':invalid');
            invalidInputs.forEach(input => {
                if (input.classList.contains('hidden-input')) {
                    const trigger = input.parentElement.querySelector('.dropdown-trigger');
                    if (trigger) trigger.classList.add('error-input', '!border-red-500', '!text-red-600', '!ring-red-500/20');
                } else {
                    input.classList.add('error-input', '!border-red-500', '!text-red-600', '!ring-red-500/20');
                }

                const errorMsg = document.createElement('p');
                errorMsg.className = 'error-msg text-red-500 text-[11px] mt-1 ml-4 md:ml-4 mb-2 font-medium block w-full';
                errorMsg.innerText = input.title || input.validationMessage || 'Vui lòng chọn một mục.';

                input.parentElement.appendChild(errorMsg);

                const label = input.parentElement.querySelector('label');
                if (label) {
                    label.classList.add('error-label', '!text-red-500');
                }
            });
            return;
        }

        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;

        // Hiển thị trạng thái loading
        submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-[20px]">refresh</span> Đang gửi...';
        submitBtn.disabled = true;

        const formData = new FormData(form);
        if (CLIENT_SHEET_ID) {
            formData.append('sheetId', CLIENT_SHEET_ID);
        }

        // Gửi data dưới dạng URLSearchParams để Apps Script có thể đọc được bằng e.parameter
        fetch(GOOGLE_APP_SCRIPT_URL, {
            method: 'POST',
            body: new URLSearchParams(formData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.result === 'success') {
                    // Chuyển hướng sang trang cảm ơn
                    window.location.href = 'cam-on.html';
                } else {
                    alert('Có lỗi xảy ra: ' + data.error);
                    submitBtn.innerHTML = originalBtnText;
                    submitBtn.disabled = false;
                }
            })
            .catch(error => {
                alert('Có lỗi xảy ra khi gửi dữ liệu. Vui lòng thử lại sau.');
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            });
    };

    // Active Navigation Highlight
    const path = window.location.pathname;
    let currentPath = path;
    if (path === '/' || path === '') {
        currentPath = '/index.html';
    }

    // Desktop nav
    const desktopLinks = document.querySelectorAll('header nav.hidden.md\\:flex > a');
    desktopLinks.forEach(link => {
        const href = link.getAttribute('href');
        let linkPath = href;
        if (href === '/' || href === '') linkPath = '/index.html';

        if (currentPath === linkPath) {
            if (href === '/programs.html') {
                link.classList.remove('bg-primary/10', 'text-primary');
                link.classList.add('bg-primary', 'text-white');
                const dots = link.querySelectorAll('.bg-secondary');
                dots.forEach(dot => {
                    dot.classList.remove('bg-secondary');
                    dot.classList.add('bg-white');
                });
            } else {
                link.classList.remove('text-on-surface-variant', 'after:w-0');
                link.classList.add('text-primary', 'after:w-full');
            }
        }
    });

    // Mobile nav
    const mobileLinks = document.querySelectorAll('#mobileMenu nav > a');
    mobileLinks.forEach(link => {
        const href = link.getAttribute('href');
        let linkPath = href;
        if (href === '/' || href === '') linkPath = '/index.html';

        if (currentPath === linkPath) {
            link.classList.remove('text-on-surface');
            link.classList.add('text-primary');
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Custom Dropdown Logic
    document.querySelectorAll('.custom-dropdown').forEach(dropdown => {
        const trigger = dropdown.querySelector('.dropdown-trigger');
        const menu = dropdown.querySelector('.dropdown-menu');
        const hiddenInput = dropdown.querySelector('input[type="text"]');
        const selectedText = dropdown.querySelector('.selected-text');
        const icon = dropdown.querySelector('.dropdown-icon');

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = !menu.classList.contains('invisible');

            // Close all others
            document.querySelectorAll('.dropdown-menu').forEach(m => {
                m.classList.add('opacity-0', 'invisible', 'translate-y-2');
                const pIcon = m.closest('.custom-dropdown').querySelector('.dropdown-icon');
                if (pIcon) pIcon.classList.remove('rotate-180');
            });

            if (!isOpen) {
                menu.classList.remove('opacity-0', 'invisible', 'translate-y-2');
                if (icon) icon.classList.add('rotate-180');
            }
        });

        dropdown.querySelectorAll('.option-item').forEach(item => {
            item.addEventListener('click', (e) => {
                e.stopPropagation();

                const val = item.getAttribute('data-value');
                const text = item.innerText;

                hiddenInput.value = val;
                selectedText.innerText = text;
                selectedText.classList.remove('text-transparent', 'text-on-surface-variant');
                selectedText.classList.add('text-on-surface');

                menu.classList.add('opacity-0', 'invisible', 'translate-y-2');
                if (icon) icon.classList.remove('rotate-180');

                // Trigger validity styling updates if needed
                trigger.classList.remove('error-input', '!border-red-500', '!text-red-600', '!ring-red-500/20');
                const errorMsg = dropdown.querySelector('.error-msg');
                if (errorMsg) errorMsg.remove();

                const label = dropdown.querySelector('.dropdown-label');
                if (label) {
                    label.classList.remove('error-label', '!text-red-500');
                    label.classList.add('peer-valid:top-1', 'peer-valid:text-xs');
                }

                // Add valid state to trigger fake focus/valid styles if floating
                dropdown.classList.add('is-filled');
            });
        });
    });

    document.addEventListener('click', () => {
        document.querySelectorAll('.dropdown-menu').forEach(m => {
            m.classList.add('opacity-0', 'invisible', 'translate-y-2');
            const icon = m.closest('.custom-dropdown').querySelector('.dropdown-icon');
            if (icon) icon.classList.remove('rotate-180');
        });
    });

    // Hiệu ứng pháo hoa trên trang cảm ơn
    if (window.location.pathname.includes('cam-on.html')) {
        const duration = 3500;
        const end = Date.now() + duration;
        const colors = ['#0077b6', '#00b4d8', '#90e0ef', '#ffb703', '#fb8500'];

        (function frame() {
            confetti({
                particleCount: 5,
                angle: 60,
                spread: 55,
                origin: { x: 0, y: 0.8 },
                colors: colors,
                zIndex: 9999
            });
            confetti({
                particleCount: 5,
                angle: 120,
                spread: 55,
                origin: { x: 1, y: 0.8 },
                colors: colors,
                zIndex: 9999
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
    }
});
