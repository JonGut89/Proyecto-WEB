
const nombre = document.getElementById("name")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", (e)=>{
        e.preventDefault()
        let warnings = "";
        let entrar = false
        let pyEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        parrafo.innerHTML = ""
        if(nombre.value.length < 4){
                alert("Nombre muy corto")
                warnings += 'El nombre no es válido <br>';
                entrar = true
        }
        console.log (pyEmail.test(email.value))
        if(!pyEmail.test(email.value)){
                warnings += 'El mail no es valido <br>'
        }
        if(pass.value.length < 8){
                warnings += 'La contraseña no es válida <br>';
                entrar = true
        }
        if(entrar){
                parrafo.innerHTML = warnings
        }else{
                parrafo.innerHTML = "Enviado!"
        }
})

//https://www.w3resource.com/javascript/form/email-validation.php