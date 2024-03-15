document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("register-form");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const passInput = document.getElementById("pass");
    const rePassInput = document.getElementById("re_pass");
  
    form.addEventListener("submit", function(event) {
      let valid = true;
  
      // Validate name
      if (nameInput.value.trim() === "") {
        showError(nameInput, "Name is required");
        valid = false;
      } else {
        showSuccess(nameInput);
      }
  
      // Validate email
      if (!isValidEmail(emailInput.value)) {
        showError(emailInput, "Invalid email address");
        valid = false;
      } else {
        showSuccess(emailInput);
      }
  
      // Validate password
      if (passInput.value.length < 8) {
        showError(passInput, "Password must be at least 8 characters");
        valid = false;
      } else {
        showSuccess(passInput);
      }
  
      // Validate confirm password
      if (rePassInput.value !== passInput.value) {
        showError(rePassInput, "Passwords do not match");
        valid = false;
      } else {
        showSuccess(rePassInput);
      }
  
      if (!valid) {
        event.preventDefault();
      }
    });
  
    function showError(input, message) {
      const formGroup = input.parentElement;
      const errorMsg = formGroup.querySelector(".error-message");
      formGroup.classList.add("error");
      errorMsg.innerText = message;
    }
  
    function showSuccess(input) {
      const formGroup = input.parentElement;
      formGroup.classList.remove("error");
    }
  
    function isValidEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
    }
  });
  