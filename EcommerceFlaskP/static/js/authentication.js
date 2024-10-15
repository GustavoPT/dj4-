document.getElementById('show-login').addEventListener('click', function() {
    lf  = document.getElementById('login-form')
    lf.classList.add('active');
    document.getElementById('register-form').classList.remove('active');
});

document.getElementById('show-register').addEventListener('click', function() {
    document.getElementById('register-form').classList.add('active');
    document.getElementById('login-form').classList.remove('active');
});


// get the password
// make a re