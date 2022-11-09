const nombreApellido  = document.getElementById('nombreapellido');
const correoElectronico  = document.getElementById('correoelectronico');
const contrasenia  = document.getElementById('contrasenia');
const registro = document.getElementById('registro');
const parrafo = document.getElementById('warningId')

registro.addEventListener("submit", e=>{
    e.preventDefault()
    let warning = ""
    let entrar = false
    let regexcorreoElectronico = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/ 
    parrafo.innerHTML = ""

    //  console.log(nombreApellido.value.length <6)
    if(nombreApellido.value.length <6){
       warning += 'El Nombre y Apellido no es válido <br>'
       entrar = true   
    }
    
    
   // console.log(regexcorreoElectronico.test (correoElectronico.value))
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
