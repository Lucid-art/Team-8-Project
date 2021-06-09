const stealth = document.querySelector("#stealth");
const striker = document.querySelector("#striker");
const redsamurai =  document.querySelector("#red-samurai");
const bmo =  document.querySelector("#bmo");


//where the code is saved to localstorage

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "stealth") {
  document.body.classList.add("stealth-theme");
}else if (currentTheme == "striker") {
  document.body.classList.add("striker-theme");
}else if (currentTheme == "redsamurai") {
  document.body.classList.add("red-samurai-theme");
}else if (currentTheme == "bmo") {
  document.body.classList.add("bmo-theme"); 
}

stealth.addEventListener("click", function () {
  document.body.classList.toggle("stealth-theme"); //where the css id should go

  let theme = "light";
  if (document.body.classList.contains("stealth-theme")) {
    theme = "stealth";
  }
  localStorage.setItem("theme", theme);
});

//striker

striker.addEventListener("click", function () {
  document.body.classList.toggle("striker-theme");

  let theme = "light";
  if (document.body.classList.contains("striker-theme")) {
    theme = "striker";
  }
  localStorage.setItem("theme", theme);// this is pretty esentail <-- dislexia
});
  

//redsamurai

redsamurai.addEventListener("click", function () {
  document.body.classList.toggle("red-samurai-theme");

  let theme = "light";
  if (document.body.classList.contains("red-samurai-theme")) {
    theme = "redsamurai";
  }
  localStorage.setItem("theme", theme);
}); 

//BMO theme
bmo.addEventListener("click", function () {
  document.body.classList.toggle("bmo-theme");

  let theme = "light";
  if (document.body.classList.contains("bmo-theme")) {
    theme = "bmo";
  }
  localStorage.setItem("theme", theme);
}); 