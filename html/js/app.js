'use strict'

const grande = document.querySelector('.grande')
const punto = document.querySelectorAll('.punto')

//cuando hago click en cada punto
 //saber la aposicion de ese punto
 //Aplicar un transform tralateX al grande 
 //QUITAR la clase activo de TODOS puntos
 //AÑADIR la clase activo al punto que hemos hecho CLICK

 //recorrer todos los puntos
 punto.forEach( ( cadaPunto , i )=> {
        //asignamos un click a cada punto
        punto[i].addEventListener('click',()=>{
                
                //posisicon es 0 transformX es 0
                //posiciion es 1  transformX es -50%
                //operacion = posicion *-50
                
                //gguardar la posicion de cada punto
                let posicion = i
                //calculando el espacio que debe desplazarse el grande
                let operacion = posicion  * -50

                //movemos el grand
                grande.style.transform = `translateX(${ operacion }%)` 

                //recorremos todos los punto
                punto.forEach( ( cadaPunto , i )=>{
                        //quitamos la calse activo a todos los punto
                        punto[i].classList.remove('activo') 
                })
                //añadir la clase activo en el putno que hemos hecho click
                punto[i].classList.add('activo') 
        })
 })





 ( condicion ) ? 'hola' : 'adiós'