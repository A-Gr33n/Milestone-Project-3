document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  
  });

  document.addEventListener('DOMContentLoaded', function() {
    // Carousel 
    var elems = document.querySelectorAll('.carousel');
    M.Carousel.init(elems,  {indicators: true, duration:200 });

 });

 document.addEventListener('DOMContentLoaded', function() {
  // Modal
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems, {});
  });

