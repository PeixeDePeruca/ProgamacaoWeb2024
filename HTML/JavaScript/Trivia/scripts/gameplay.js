
        const questions = [
            {
                question: 'Qual é o estilo musical?',
                a: 'Jazz',
                b: 'Pop',
                c: 'MPB',
                d: 'Samba',
                answer: 'b'
            },
            {
                question: 'Quem é o cantor?',
                a: 'Stevie Wonder',
                b: 'James Hetfield',
                c: 'Eddie Vedder',
                d: "Jack Black",
                answer: 'd'
            },
            {
                question: 'Qual é o estilo musical?',
                a: 'Jazz',
                b: 'Pop',
                c: 'MPB',
                d: 'Samba',
                answer: 'c'
            },
            {
                question: 'Essa música vem de qual filme?',
                a: 'Velozes e Furiosos 3 Desafio em Tóquio',
                b: 'Irmão Urso 2',
                c: 'A era do Gelo 3',
                d: 'Rio 2',
                answer: 'b'
            },
            {
                question: 'Quem é o cantor?',
                a: 'Tim Maia',
                b: 'MC Marcinho',
                c: 'Padre Fabio de Melo',
                d: 'Gal Costa',
                answer: 'a'
            },
            {
                question: 'Essa fala é o bordão de qual personagem?',
                a: 'Jack Sparrow',
                b: 'Jake o Cão',
                c: 'Peter Griffin',
                d: 'Homer Simpson',
                answer: 'd'
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
        let timerID = undefined;
        let countdownID = undefined;

        function updateInfos() {
            question.textContent = questions[round - 1].question;
            altA.textContent = questions[round - 1].a;
            altB.textContent = questions[round - 1].b;
            altC.textContent = questions[round - 1].c;
            altD.textContent = questions[round - 1].d;
            roundHTML.textContent = round;

            startTimer();
        }

        function startTimer() {
            clearInterval(countdownID);
            clearTimeout(timerID);

            let timeLeft = 10; // Defina o tempo desejado em segundos
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
                    alert('Acabaram as questões');
                    window.location.replace('../html/index.html');
                }
            } else {
                console.log('Errou');
            }
        }

        function timeOut() {
            alert('O tempo acabou.');
            window.location.replace('../html/index.html');
        }

        updateInfos();