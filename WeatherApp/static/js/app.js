var input = d3.select("#scroll");

input.on("click", function() {
    d3.event.preventDefault();
})

// var element_to_scroll_to = document.getElementById('anchorName2');
// // Or:
// var element_to_scroll_to = document.querySelectorAll('.my-element-class')[0];
// // Or:
// var element_to_scroll_to = $('.my-element-class')[0];
// // Basically `element_to_scroll_to` just have to be a reference
// // to any DOM element present on the page
// // Then:
// element_to_scroll_to.scrollIntoView();id="filter-btn"