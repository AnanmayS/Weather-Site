
window.addEventListener("DOMContentLoaded", () => {
    const background = document.getElementById("general").innerHTML;

    if (background == "Clouds") {
        console.log(background)
        document.body.style.backgroundImage = "url('https://wallpaperaccess.com/full/1385461.jpg')"
    } else if(background == "Clear") {
        console.log(background)
        document.body.style.backgroundImage = "url('https://papers.co/wallpaper/papers.co-sn72-blue-sky-color-blur-gradation-25-wallpaper.jpg')"
    } else if(background == "Snow") {
        console.log(background)
        document.body.style.backgroundImage = "url('https://cdn.wallpapersafari.com/13/82/Pf8tBd.png')"
    } else if(background == "Rain") {
        console.log(background)
        document.body.style.backgroundImage = "url('https://wallpaperaccess.com/full/2926584.jpg')"
    } else if(background == "Drizzle") {
        console.log(background)
        document.body.style.backgroundImage = "url('https://wallpaperaccess.com/full/2926584.jpg')"
    } else {
        console.log(background)
        document.body.style.backgroundImage = "url('https://papers.co/wallpaper/papers.co-sn72-blue-sky-color-blur-gradation-25-wallpaper.jpg')"
    } 
})