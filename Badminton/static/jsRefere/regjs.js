// reg.js

// Function to validate the name field
function validateName() {
    var nameInput = document.getElementById('t1');
    var nameError = document.getElementById('nc');
    
    var namePattern = /^[A-Za-z ]+$/; // Regular expression for letters only
    
    if (!namePattern.test(nameInput.value)) {
        nameError.textContent = 'Name should only contain letters';
        return false;
    } else if (nameInput.value.trim() === '') {
        nameError.textContent = 'Name is required';
        return false;
    } else {
        nameError.textContent = '';
        return true;
    }
}

// Function to validate the email field
function validateEmail() {
    var emailInput = document.getElementById('t2');
    var emailError = document.getElementById('em');
    
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;    
    if (!emailPattern.test(emailInput.value)) {
        emailError.textContent = 'Enter a valid email address';
        return false;
    } else {
        emailError.textContent = '';
        return true;
    }
}

// Function to validate the password field
function validatePwd() {
    var pwdInput = document.getElementById('t3');
    var pwdError = document.getElementById('pwd');
    
    var pwdPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
    
    if (!pwdPattern.test(pwdInput.value)) {
        pwdError.textContent = 'Password must have at least 8 characters, one uppercase letter, one digit, and one special character';
        return false;
    } else {
        pwdError.textContent = '';
        return true;
    }
}

// Function to validate confirm password field
function validateCpwd() {
    var pwdInput = document.getElementById('t3');
    var cpwdInput = document.getElementById('confirmpassword');
    var cpwdError = document.getElementById('cpwd');

    if (pwdInput.value !== cpwdInput.value) {
        cpwdError.textContent = 'Passwords do not match';
        return false;
    } else {
        cpwdError.textContent = '';
        return true;
    }
}

// Function to perform overall form validation before submission
function checkall() {
    event.preventDefault();

    var nameValid = validateName();
    var emailValid = validateEmail();
    var passwordValid = validatePwd();
    var confirmPasswordValid = validateCpwd();

    if (nameValid && emailValid && passwordValid && confirmPasswordValid) {
        swal.fire({
            title: 'Registered Successfully',
            text: 'Congratulations, you are registered!',
            icon: 'success'
        }).then(function() {
            // If you want to redirect, you can use window.location.href
            window.location.href = '../templates/login.html';
        });
    } else {
        swal.fire({
            title: 'Error',
            text: 'Please fill in all required fields with valid data.',
            icon: 'error'
        });
    }
}

// Attach event listeners to input fields to trigger validation
document.getElementById('t1').addEventListener('keyup', validateName);
document.getElementById('t2').addEventListener('keyup', validateEmail);
document.getElementById('t3').addEventListener('keyup', validatePwd);
document.getElementById('confirmpassword').addEventListener('keyup', validateCpwd);
