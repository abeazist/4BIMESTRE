let menuMobile = document.getElementById("menu-mobile")
let menuDesktop =  document.getElementById("menu-desktop")

function menu() {
    if (menuDesktop.getAttribute("src") === "")
    {
        menuDesktop.setAttribute ("src", "./")
        menuMobile.style.left = '-100%'
    }
    else if (menuDesktop.getAttribute("src")=== "")
    {
        menuDesktop.setAttribute("src", "")
        menuMobile.style.left = '0%'

    }
    
}