document.getElementById('show-login').addEventListener('click', function(event) {
    event.preventDefault();
    document.querySelector('.signup-container').style.display = 'none';
    document.querySelector('.login-container').style.display = 'block';
});

document.getElementById('show-signup').addEventListener('click', function(event) {
    event.preventDefault();
    document.querySelector('.signup-container').style.display = 'block';
    document.querySelector('.login-container').style.display = 'none';
});
