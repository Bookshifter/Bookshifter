let fatecDiadema;


function initMap(){
    const mapDiv = document.getElementById('map');
    mapDiv.removeAttribute('hidden', '');
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();
    const valorSelecionado = document.getElementById("form-fatec");
    const nome_fatec = valorSelecionado.options[valorSelecionado.selectedIndex].text
    
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: -23.68677960423178, lng: -46.628339988195634}
    });
  
    document.getElementById('btn-rota').addEventListener('click', () => {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    });

    directionsRenderer.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsRenderer);
    
    const userMarker = addUserLocationMarker(map, directionsService, directionsRenderer);
    
    fatecDiadema = createFatecMarker(map, -23.673520792926038, -46.61872788592052, 'imgs/lugar-colocar.png');
    addInfoWindow(map, fatecDiadema, nome_fatec, './imgs/fzs.jpg', 19, '(11) 58518949', 'f217secacademica@cps.sp.gov.br');

    function createFatecMarker(map, lat, lng, icon) {
        return new google.maps.Marker({
            position: { lat, lng },
            map: map,
            icon: icon,
        });
    }

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

    function calculateAndDisplayRoute(directionsService, directionsRederer){
        const selectedMode = document.getElementById('mode').value;

    
        directionsService.route({
                origin: document.getElementById('origem').value,
                	destination: nome_fatec,
                travelMode: google.maps.TravelMode[selectedMode],
            })
        .then((response)=>{
            directionsRederer.setDirections(response);
            const route = response.routes[0];
            const leg = route.legs[0]; 
            const duration = leg.duration.text; 

            document.getElementById('duration').textContent = 'Tempo de Percurso: ' + duration;
        }) 
        console.log(nome_fatec)
    }

//CLOSE func
}
    