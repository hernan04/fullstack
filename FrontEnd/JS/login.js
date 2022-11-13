const correoElectronico  = document.getElementById('correoelectronico');
const contrasenia  = document.getElementById('contrasenia');
const login = document.getElementById('login');
const parrafo = document.getElementById('warningId')

login.addEventListener("submit", e=>{
    e.preventDefault()
    let warning = ""
    let entrar = false
    let regexcorreoElectronico = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/ 
    parrafo.innerHTML = ""

     //console.log(regexcorreoElectronico.test (correoElectronico.value))
     if(!regexcorreoElectronico.test (correoElectronico.value)){
        warning +='El correo electrónico no es valido<br>'
         entrar = true
    }
    if(contrasenia.value.length < 8){
        warning +='La contraseña no es válida<br>'
         entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warning
    }else{
        parrafo.innerHTML = "Enviado"
    }
})