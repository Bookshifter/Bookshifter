let fatecDiadema;


function initMap(){
<<<<<<< HEAD
    const mapDiv = document.getElementById('map');
    mapDiv.removeAttribute('hidden', '');
=======
>>>>>>> backend-joao
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();
    const valorSelecionado = document.getElementById("form-fatec");
    const nome_fatec = valorSelecionado.options[valorSelecionado.selectedIndex].text
    
<<<<<<< HEAD
=======
    
    // adicionar ambas lat e long na entidade fatec
    
>>>>>>> backend-joao
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: -23.68677960423178, lng: -46.628339988195634}
    });
<<<<<<< HEAD
  
=======
    /** 
     * 
     * Usar a URL do Postman
     * fetch('https://jsonplaceholder.typicode.com/posts').then(function (response) {
    // The API call was successful!
    console.log('success!', response);
    }).catch(function (err) {
    // There was an error
    console.warn('Something went wrong.', err);
    });
     * 
    */

    

>>>>>>> backend-joao
    document.getElementById('btn-rota').addEventListener('click', () => {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    });

<<<<<<< HEAD
=======



>>>>>>> backend-joao
    directionsRenderer.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsRenderer);
    
    const userMarker = addUserLocationMarker(map, directionsService, directionsRenderer);
    
<<<<<<< HEAD
    fatecDiadema = createFatecMarker(map, -23.673520792926038, -46.61872788592052, 'imgs/lugar-colocar.png');
    addInfoWindow(map, fatecDiadema, nome_fatec, './imgs/fzs.jpg', 19, '(11) 58518949', 'f217secacademica@cps.sp.gov.br');

=======



    // pegar todas as fatecs do banco e criar para cada uma delas a variavel abaixo
    fatecDiadema = createFatecMarker(map, -23.673520792926038, -46.61872788592052, 'imgs/lugar-colocar.png');
    addInfoWindow(map, fatecDiadema, nome_fatec, './imgs/fzs.jpg', 19, '(11) 58518949', 'f217secacademica@cps.sp.gov.br');

    // centro diadema = -23.68073183539147, -46.62785410163126




>>>>>>> backend-joao
    function createFatecMarker(map, lat, lng, icon) {
        return new google.maps.Marker({
            position: { lat, lng },
            map: map,
            icon: icon,
        });
    }

<<<<<<< HEAD
=======








>>>>>>> backend-joao
    function addUserLocationMarker(map, directionsService, directionsRenderer) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
    
                document.getElementById('origem').value = userLocation.lat + ',' + userLocation.lng;
    
                const userMarker = createFatecMarker(map, userLocation.lat, userLocation.lng, 'imgs/seu-local.png');
                calculateAndDisplayRoute(directionsService, directionsRenderer);
    
                return userMarker;
            });
        }
    }

<<<<<<< HEAD
=======

 //Adicionar informações do banco 
>>>>>>> backend-joao
    function addInfoWindow(map, marker, name, imageSrc, bookCount, phone, email) {
        const contentString = `
            <div id="content">
                <div id="notification"></div>
                <h1 id="firstHeading" class="firstHeading">${name} <br><img src='${imageSrc}' width=35%></h1>
                <div id="bodyContent">
                    <h3>Ver livros</h3>
                    <h3>Mais informações sobre a ${name}: </h3>
                    <h3>Estoque de Livros: ${bookCount}</h3>
                    <h3>Entre em contato</h3>
                    <h4>Telefone: <a href="tel:${phone}">${phone}</a> </h4>
                    <h4>E-mail: <a href="mailto:${email}">${email}</a></h4>
                </div>
            </div>
        `;
    }
<<<<<<< HEAD

=======
>>>>>>> backend-joao
    const infowindow = new google.maps.InfoWindow({
        content: contentString
    });

    
    marker.addListener('mouseout', function () {
        infowindow.open(map, marker);
    });


    marker.addListener('mousemove', function () {
        infowindow.close();
    });


let isMouseOverMarker = false;

fatecDiadema.addListener('mouseout', function() {
    isMouseOverMarker = false;
});




google.maps.event.addListener(map, 'mousemove', function(event) {
    if (!isMouseOverMarker) {
        infowindow.close();
    }
});
<<<<<<< HEAD

=======
>>>>>>> backend-joao
    function calculateAndDisplayRoute(directionsService, directionsRederer){
        const selectedMode = document.getElementById('mode').value;

    
<<<<<<< HEAD
        directionsService.route({
                origin: document.getElementById('origem').value,
                	destination: nome_fatec,
                travelMode: google.maps.TravelMode[selectedMode],
            })
=======
        directionsService
        .route({
            origin: document.getElementById('origem').value,
            destination: nome_fatec,
            travelMode: google.maps.TravelMode[selectedMode],
        })
>>>>>>> backend-joao
        .then((response)=>{
            directionsRederer.setDirections(response);
            const route = response.routes[0];
            const leg = route.legs[0]; 
            const duration = leg.duration.text; 

            document.getElementById('duration').textContent = 'Tempo de Percurso: ' + duration;
        }) 
        console.log(nome_fatec)
<<<<<<< HEAD
    }

//CLOSE func
}
=======
}

//CLOSE func
}


    //usar serviço do google para mostrar a rota

>>>>>>> backend-joao
    