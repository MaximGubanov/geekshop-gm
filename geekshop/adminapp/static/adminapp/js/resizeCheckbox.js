let ch = document.querySelectorAll('input[type="checkbox"]');

ch.forEach(element => {
    element.classList.remove('form-control')
});

console.log('enabled script');