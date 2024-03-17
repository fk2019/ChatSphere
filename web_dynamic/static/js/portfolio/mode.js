// toggle dark-white mode
document.addEventListener("DOMContentLoaded", function() {
  const icon = document.querySelector('.icon');
  const body = document.querySelector('body');
  const ln = document.querySelectorAll('.ln');
  const top = document.querySelector('.top');
  const brands = document.querySelectorAll('.br');

  const toggleHover = (el, theme) => {
    el.addEventListener('mouseover', function() {
      el.style.color = '#018786';
    })
    el.addEventListener('mouseout', function() {
      if (theme === 'dark') {
        el.style.color = 'rgba(255, 255, 255, 0.9)';
      } else if (theme ==='white') {
        el.style.color = '#333';
      }else{
        el.style.color = '#b0bec5';
      }
    })
  }
  icon.addEventListener('click', function() {
    if (icon.classList.contains('fa-moon')) {
      icon.classList.remove('fa-solid');
      icon.classList.remove('fa-moon');
      icon.classList.add('fa-regular');
      icon.classList.add('fa-sun');
      body.style.color = 'rgba(255, 255, 255, 0.9)';
      body.style.backgroundColor = 'rgba(18, 18, 18, 0.8)';
      ln.forEach((a) => {
        a.style.color = 'rgba(255, 255, 255, 0.9)'
        toggleHover(a, 'dark');
      });
      top.style.color = '#b0bec5';
      brands.forEach((b) => {
        b.style.color = '#b0bec5';
        toggleHover(b, 'brands');
      });

    } else {
      icon.classList.remove('fa-regular');
      icon.classList.remove('fa-sun');
      icon.classList.add('fa-solid');
      icon.classList.add('fa-moon');
      body.style.backgroundColor = 'rgba(255, 255, 255, 1)';
      body.style.color = 'rgba(0, 0, 0, 0.8)';
      ln.forEach((a) => {
        a.style.color = 'rgba(0, 0, 0, 0.8)'
        toggleHover(a, 'white');
      });
      brands.forEach((b) => {
        b.style.color = '#333';
        toggleHover(b, 'white');
      });
      top.style.color = '#333';
    }
  });
});
