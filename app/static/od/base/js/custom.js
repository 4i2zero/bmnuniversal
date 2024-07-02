import { Tooltip, Toast, Popover } from 'bootstrap';

// Import Bootstrap modules

// Initialize tooltips
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new Tooltip(tooltipTriggerEl);
});

// Initialize toasts
const toastElList = [].slice.call(document.querySelectorAll('.toast'));
toastElList.map(function (toastEl) {
    return new Toast(toastEl);
});

// Initialize popovers
const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
popoverTriggerList.map(function (popoverTriggerEl) {
    return new Popover(popoverTriggerEl);
});

// Your custom JavaScript code goes here

// Example: Add a click event listener to a button
const button = document.querySelector('#myButton');
button.addEventListener('click', function () {
    // Do something when the button is clicked
});