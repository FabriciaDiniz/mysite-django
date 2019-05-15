//pegar a div add_opcoes e
var div = document.querySelector('#add_opcoes');

document.querySelector('#add_opcao').addEventListener('click', function(event) {
    //adicionar mais um campo de input como child
    var campo_input = document.createElement('input').addClass('opc');
    div.appendChild(campo_input);

});