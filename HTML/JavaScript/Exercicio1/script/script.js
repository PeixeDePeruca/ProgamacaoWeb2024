const userName = document.getElementById('i-name');
const birthDate = document.getElementById('i-birthDate');
const orders = document.getElementById('i-orders');
const submit = document.getElementById('i-submit');
const valorProduto = document.getElementById('i-valor');
const greeting = document.getElementById('i-name');
const birthDateOutput = document.createElement('p');

// divs
const container = document.getElementById('conteiner');
const container2 = document.getElementById('block');

submit.onclick = formSubmit;

function formSubmit() {
    // Verificar nome de usuário.
    if (userName.value.length < 3 || userName.value.length > 18) {
        alert('O nome deve conter entre 3 e 18 letras.');
        return;
    }

    let valor;
    if (orders.value === 'omelete') {
        valor = 12.50;
    } else if (orders.value === 'macarrao') {
        valor = 15.00;
    }

    // Atualizar a saudação, valor da refeição e data de nascimento
    greeting.textContent = "Olá: " + userName.value;
    valorProduto.textContent = "O Valor da sua refeição foi: R$" + valor.toFixed(2);
    birthDateOutput.textContent = "Data de Nascimento: " + birthDate.value;

    // Adicionar a data de nascimento ao container2 se ainda não estiver lá
    if (!container2.contains(birthDateOutput)) {
        container2.appendChild(birthDateOutput);
    }

    // Mostrar o segundo container e ocultar o primeiro
    container.style.display = 'none';
    container2.style.display = 'block';
}
