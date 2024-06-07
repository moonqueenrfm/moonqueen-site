
function clue1_moonset(){
    const bg = document.querySelector('body');
    bg.style.background = 'linear-gradient(180deg, rgba(2,0,36,1) 0%, rgba(9,42,121,1) 42%, rgba(147,0,255,1) 86%)';
    const moonqueen = document.querySelector('.moonqueen');
    moonqueen.style.color = 'white';
    const splash = document.querySelector('.splash');
    splash.style.color = 'white';
    const h1 = document.querySelector('h1');
    h1.style.color = 'white';
    const links = document.querySelectorAll('nav a');
    links.forEach((link)=>{
        link.style.color = 'white';
    });
}