document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  
  });

  document.addEventListener('DOMContentLoaded', function() {
    // Carousel 
    var elems = document.querySelectorAll('.carousel');
    M.Carousel.init(elems,  {indicators: true,
      dist:-400});

 });

 document.addEventListener('DOMContentLoaded', function() {
  // Modal
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems, {});
  });

