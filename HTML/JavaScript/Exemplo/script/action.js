console.log("se n funcionar a mãe do tales é uma...");


var nome = "";
var idade = 0;
var birthYear = document.getElementById("i-birthYear");
const response = document.getElementById("response")

function Welcome(){
    idade = 2024 - birthYear.value;

    console.log("se n funcionar a mãe do tales é uma...");

    if ( idade >= 18 ){
        console.log("Você pode ter CNH");
        
        response.textContent = 'Você pode ter CNH';
 
        alert('Você pode ter CNH');

    }
    else {
        console.log("Haha,criança....você ainda não pode ter CNH");
        console.log(`Faltam ${18 - idade} para fazer 18 anos`);

        response.textContent = 'Haha,criança....você ainda não pode ter CNH' +
        `\nFaltam ${18 - idade} para fazer 18 anos`;
    }

}

