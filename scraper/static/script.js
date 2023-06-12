function setLink(event, element) {
  event.preventDefault(); // Disable default link behavior
  var link = element.getAttribute("href");
  document.getElementById("link").value = link;
}

function clearInput() {
  document.getElementById("link").value = "";
}