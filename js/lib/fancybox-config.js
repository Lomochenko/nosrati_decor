document.addEventListener("DOMContentLoaded", function () {
      
  if (typeof Fancybox !== 'undefined') {
    Fancybox.bind("[data-fancybox]",
       {
      Images: {
        initialSize: "fit",
      },
      infinite: false,
      preload: 1,
      AnimationEffect: "fade",
      TransitionEffect: "fade",
      contentClick: "toggleCover",
      Toolbar: {
        display: {
          left: ["infobar"],
          right: ["slideshow", "thumbs", "close"],
        },
      },
    });
  } else {
    console.error("FancyBox does not loaded");
  }
},300);