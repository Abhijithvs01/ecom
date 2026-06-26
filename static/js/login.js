document.addEventListener("DOMContentLoaded", function () {

    // Password show/hide
    const passwordInput = document.querySelector('input[name="password"]');

    // Disable button after submit
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {
            const btn = form.querySelector("button[type='submit']");
            btn.disabled = true;
            btn.innerText = "Logging in...";
        });
    }
});