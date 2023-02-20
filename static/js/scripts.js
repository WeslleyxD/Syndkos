
// const modal = document.querySelector(".modal");
// const modal_content = document.querySelector(".modal-content");
// const show_form = document.querySelector('.show-form');

// show_form.addEventListener('click', (event) => {
//     event.preventDefault();
//     modal.style.display = 'block';

//     fetch(show_form.attributes.id.value, {
//         method: 'GET',
//         // body: formData,
//         headers: {
//             "X-Requested-With": "XMLHttpRequest"
//           },
//     })
//     .then(response => response.json())
//     .then(data => {
//         modal_content.innerHTML = data['html_form']


//     })
//     .catch(error => console.error(error));
// });

// const category_send = document.querySelector(".category_send");
// category_send.addEventListener('submit', (event) => {
//     event.preventDefault();
//     modal.style.display = 'none';

// });





// // (function(win,document){
// //     if (document.querySelector("#category_form")) {
// //         let form = document.querySelector("#category_form");
    
// //         function sendForm(event)
// //         {
// //             event.preventDefault();
// //             console.log(form.action)
// //             let data = new FormData(form);
// //             let ajax = new XMLHttpRequest();
// //             let token = document.querySelectorAll('input')[0].value;
// //             ajax.open('POST', form.action);
// //             ajax.setRequestHeader('X-CSRF-TOKEN', token);
// //             ajax.send(data)
// //             ajax.onreadystatechange = function ()
    
// //             {
// //                 if (ajax.status === 200 && ajax.readyState === 4){
// //                     console.log('Cadastrou!');
// //                 }
// //             } 
// //         }
// //         form.addEventListener('submit', sendForm, false);
// //     }
// // })(window, document)



// // const openModalButton = document.getElementById("open-modal-btn");
// // const modal = document.getElementById("modal");

// // openModalButton.addEventListener("click", () => {
// //     fetch("http://127.0.0.1:8000/products/minha/", {
// //         method: "GET",
// //         headers: {
// //             "X-Requested-With": "XMLHttpRequest"
// //         }
// //     }).then(response => {
// //         if (response.ok) {
// //             response.json().then(data => {
// //                 // Aqui, utilize o conteúdo retornado pela view para preencher o seu modal
// //                 modal.innerHTML = data;
// //                 modal.style.display = "block";
// //             });
// //         }
// //     });
// // });



// // const form = document.getElementById('category-form');
// // const csrf = document.querySelectorAll('input')[0].value;
// // form.addEventListener('submit', (event) => {
// //     event.preventDefault();
// //     // console.log(form)
// //     // console.log(input)
// //     const formData = new FormData(form);
// //     console.log(form.action)

// //     fetch(form.action, {
// //         method: 'POST',
// //         body: formData,
// //         headers: {
// //             'X-CSRF-TOKEN': csrf,
// //             "X-Requested-With": "XMLHttpRequest"
// //           },
// //     })
// //     .then(response => response.json())
// //     .then(data => {
// //         if (data.errors) {
// //             const messageElement = document.getElementById('teste');
// //             messageElement.innerHTML = data.errors.name[0];
            
// //         } else {
// //             const messageElement = document.getElementById('teste');
// //             messageElement.innerHTML = data.map(item => `<li>${item.name}</li>`).join('');

// //         }
// //             // Iterate over numeric indexes from 0 to 5, as everyone expects.
// //             // messageElement.innerText = data[i].name;
// //     })
// //     .catch(error => console.error(error));
// // });



// // // Obter o modal
// // const modal = document.querySelector(".modal");

// // // Obter o elemento de fechar o modal
// // const span = document.querySelector(".close");

// // // Obter o botão que abre o modal
// // window.addEventListener('click', function(event) {
// //     if (event.target == modal) {
// //       modal.style.display = "none";
// //     }
// //   });

// // const btnModal = document.querySelector("#category-modal-update");
// // btnModal.addEventListener('click', (event) => {
// //     event.preventDefault();

// //     modal.style.display = "block";

// //     fetch(btnModal.href, {
// //         method: 'GET',
// //         headers: {
// //             "X-Requested-With": "XMLHttpRequest"
// //           },
// //     })
// //     .then(response => response.text())
// //     .then(data => {
// //         const category_form = JSON.parse(data)

// //         const modal_content = document.querySelector(".modal-content");
// //         // modal_content.action = btnModal.href
        
// //         // console.log(category_form)

// //         let newDiv = document.createElement("p");
        
// //         newDiv.innerHTML = category_form['form_html']
// //         modal_content.appendChild(newDiv)

// //     })
// //     .catch(error => console.error(error));
// // });


// // const modal_contentt = document.querySelector(".modal-content");
// // modal_contentt.addEventListener('submit', (event) => {
// //     modal.style.display = "block";
// // });



// // // Quando o usuário clicar no botão, abrir o modal


// // // Quando o usuário clicar em <span> (x), fechar o modal


// // // Quando o usuário clicar em qualquer lugar fora do modal, fechar o modal





// // const modal_1 = document.querySelector(".modal_1");

// // // Obter o elemento de fechar o modal
// // const span_1 = document.querySelector(".close_1");

// // // Obter o botão que abre o modal
// // window.addEventListener('click', (event) => {
// //     if (event.target == modal) {
// //       modal.style.display = "none";
// //     }
// //   });






// const modal = document.querySelector(".show-form");
// // const btnModal = document.querySelector("modal_1");
// modal.addEventListener('click', (event) => {
//     event.preventDefault();

//     fetch('/manager/category/', {
//         method: 'GET',
//         headers: {
//             "X-Requested-With": "XMLHttpRequest"
//           },
//     })
//     .then(response => response.text())
//     .then(data => {
//         let modal_book = document.querySelector(".modal")
//         modal_book.style.display = 'block';


//         console.log(data)
//         let modal_content = document.querySelector(".modal-content")
//         modal_content.html = data.html_form

        
//     })
//     .catch(error => console.error(error));
// });




const meuElemento = document.getElementById("$0");
console.log($0)