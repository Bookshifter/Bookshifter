function search_filter() {
  console.log('search_filter 1x')
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('search-bar');
    filter = input.value;
    ul = document.getElementById("filter-list");
    li = ul.getElementsByTagName('li');
  
    // Loop through all list items, and hide those who don't match the search query
    
    for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
        console.log('item voltou')
      } else {
        li[i].style.display = "none";
        console.log('item sumiu')
      }
    }
  }

function openDropdown() {
    var dropdownTrigger = document.getElementById("trigger-search");
    if (dropdownTrigger) {
        dropdownTrigger.click();
    }
}