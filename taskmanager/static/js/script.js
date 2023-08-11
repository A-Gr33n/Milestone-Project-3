document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });


  var instance = M.Carousel.init({
    fullWidth: true,
    indicators: true
  });