const correoElectronico  = document.getElementById('correoelectronico');
const mensaje = document.getElementById('mensaje');
const registro = document.getElementById('contacto');
const parrafo = document.getElementById('warningId')

registro.addEventListener("submit", e=>{
  e.preventDefault()
  let warning = ""
  let entrar = false
  let regexcorreoElectronico = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/ 
  parrafo.innerHTML = ""


  
   // console.log(regexcorreoElectronico.test (correoElectronico.value))
   if(!regexcorreoElectronico.test (correoElectronico.value)){
    warning +='El correo electronico no es valido<br>'
     entrar = true
}
  
   if(mensaje.length == 0){
    warning +='Falta completar mensaje'
    entrar = true 
  }
 
  if(entrar){
  parrafo.innerHTML = warning
}else{
  parrafo.innerHTML = "Enviado"
}


})
