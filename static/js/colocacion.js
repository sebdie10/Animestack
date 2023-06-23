imagen = "https://pics.filmaffinity.com/Bleach_Serie_de_TV-235942666-large.jpg"

dic = {
    'Bleach':{
        'imagen' : "https://pics.filmaffinity.com/Bleach_Serie_de_TV-235942666-large.jpg",
        'ID' : "1",
    },
    'Naruto' :{
        'imagen':"https://www.formulatv.com/images/series/posters/100/135/dest_1.jpg",
        'ID':"2"
    }

}

nombre= "Bleach"

content = document.getElementById("content")



for(clave in dic){ //for para iterar el diccionario 
    img = ''
    ID1 = 0

    Object.entries(dic[clave]).forEach(([key, value]) => { //iterar en las claves del diccionario
        //console.log(value)
        if(key == 'imagen'){
            img = value
        }else if(key == 'ID'){
            ID1 = value
        }
      });

    content.innerHTML += `<div class="animes"><img src="${img}" alt="">
    <p>${clave}</p>
    <p>${ID1}</p>
    </div>`
    
}






/*content.innerHTML += `<img src="${imagen}" alt="">
<p>${nombre}</p>`

*/

