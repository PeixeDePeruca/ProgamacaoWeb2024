const questions = [
    {
        question: 'Qual é o nome da personagem?',
        a: 'Alice Shimada',
        b: 'Anzu Kadotani',
        c: 'Yukari Akiyama',
        d: 'Miho Nishizumi',
        answer: 'a',
        img: '../images/Alice_boko.gif'
    },
    {
        question: 'Esse uniforme é de qual escola?',
        a: 'Pravda High School',
        b: 'Saunders',
        c: 'Saint Gloriana',
        d: 'Kuromorimine',
        answer: 'd',
        img: '../images/Uniforme.png'
    },
    {
        question: 'Qual é a nação tema da escola Kuromorimine?',
        a: 'França',
        b: 'Estados Unidos',
        c: 'Alemanha',
        d: 'Japão Imperial',
        answer: 'c',
        img: '../images/Kuromorimine_beer.png'
    },
    {
        question: 'Quem é a irmã de Maho Nishizumi?',
        a: 'Erika Itsumi',
        b: 'Miho Nishizumi',
        c: 'Koume Akaboshi',
        d: 'Shiho Nishizumi',
        answer: 'b',
        img: '../images/Maho.gif'
    },
    {
        question: 'Esse é o emblema de qual escola?',
        a: 'Pravda',
        b: 'Kuromorimine',
        c: 'Oorai',
        d: 'Jatkosota',
        answer: 'a',
        img: '../images/Pravda.png'
    },
    {
        question: 'Essa música é tema de qual escola?',
        a: 'Jatkosota',
        b: 'Oorai',
        c: 'Pravda',
        d: 'Anzio',
        answer: 'd',
        img: '../images/'
    },
    {
        question: 'Que "tanque" é esse?',
        a: 'Pershing',
        b: 'Tiger 1',
        c: 'Churchill',
        d: 'Panzer 3',
        answer: 'b',
        img: '../images/Tiger_gup.png'
    }
];

let round = 1;
const roundHTML = document.getElementById('round');
const question = document.getElementById('question');
const altA = document.getElementById('altA');
const altB = document.getElementById('altB');
const altC = document.getElementById('altC');
const altD = document.getElementById('altD');
const timerHTML = document.getElementById('timer');
const questionImage = document.getElementById('img');
let timerID = undefined;
let countdownID = undefined;

function updateInfos() {
    question.textContent = questions[round - 1].question;
    altA.textContent = questions[round - 1].a;
    altB.textContent = questions[round - 1].b;
    altC.textContent = questions[round - 1].c;
    altD.textContent = questions[round - 1].d;
    questionImage.src = questions[round - 1].img || '';
    roundHTML.textContent = round;

    startTimer();
}

function startTimer() {
    clearInterval(countdownID);
    clearTimeout(timerID);

    //let timeLeft = 18; // Defina o tempo desejado em segundos
    timerHTML.textContent = timeLeft;

    countdownID = setInterval(() => {
        timeLeft--;
        timerHTML.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(countdownID);
        }
    }, 1000);

    timerID = setTimeout(timeOut, timeLeft * 1000);
}

function answer(alt) {
    clearInterval(countdownID);
    clearTimeout(timerID);

    if (alt === questions[round - 1].answer) {
        console.log('Acertou');

        if (round < questions.length) {
            round++;
            updateInfos();
        } else {
            alert('Acabaram as questões! Parabéns :D');
            window.location.replace('../html/index.html');
        }
    } else {
        console.log('Errou');
    }
}

function timeOut() {
    alert('O tempo acabou! 😨');
    window.location.replace('../html/index.html');
}

updateInfos();
