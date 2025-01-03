var lis = document.querySelectorAll(".content ul li");

[...lis]
    .filter(li => li.textContent.includes("2"))
    .forEach(li => li.style.fontWeight = "bold");