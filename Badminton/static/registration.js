
function validateName() {
	var letters = /^[A-Za-z ]*$/;
	var fname = document.getElementById("t1").value;
	if (((!letters.test(fname) || fname.length <= 2)) && fname.length>0) {
		document.getElementById("nc").innerHTML = "Name should only contain alphanumeric and be at least 3 characters long";
        flag = 1;
	} else{
		document.getElementById("nc").innerHTML = "";
        flag = 0;
	}
}


function validateUname() {
	var letters =/^[A-Za-z ]*$/;
	var uname = document.getElementById("t4").value;
	if ((!letters.test(uname) || !(uname.length > 2)) && uname.length>0) {
		document.getElementById("uc").innerHTML = "Username should only contain alphanumeric and be at least 3 characters long";
        flag = 1;
	} else {
		document.getElementById("uc").innerHTML = "";
        flag = 0;
	}
}



function validateEmail() {
	var email_exp =/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	var email = document.getElementById("t3").value;
	if (!email_exp.test(email)||(email.length >0)) 
	{
		document.getElementById("em").innerHTML = "Inavid Email";
        flag = 1;
	} else {
		document.getElementById("em").innerHTML = "";
        flag = 0;
	}
}

function validatePhone() {
	var ph_exp =/^\d{10}$/;
	var phone = document.getElementById("t2").value;
	if (!ph_exp.test(phone)||phone.length >0 && phone.length<=10) {
		document.getElementById("ph").innerHTML = "Please enter values between 0-9";
        flag = 1;
	} else {
		document.getElementById("ph").innerHTML = "";
        flag = 0;
	}
}

function validatePwd() {
	var pwd_exp =/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
	var pwd = document.getElementById("t2").value;
	if (!pwd_exp.test(pwd) || ((pwd.lenght<=12)&&(pwd.lenght>5))){
		document.getElementById("pw").innerHTML = "password contains only Upper case, Lower case, Special character and Numeric letter minimum 5 and maximum 12 letters ";
        flag = 1;
	} else {
		document.getElementById("pw").innerHTML = "";
        flag = 0;
	}
}


function validateCpwd() {
	var cpwd = document.getElementById("t6").value;
	if (pwd!=cpwd) {
		document.getElementById("cpw").innerHTML = "Password not Matched";
        flag = 1;
	} else {
		document.getElementById("cpw").innerHTML = "";
        flag = 0;
	}
}

function clear_fun() {
	document.getElementById("t1").value = "";
	document.getElementById("t2").value = "";
	document.getElementById("t3").value = "";
	document.getElementById("t4").value = "";
	document.getElementById("t5").value = "";
	document.getElementById("t6").value = "";
}