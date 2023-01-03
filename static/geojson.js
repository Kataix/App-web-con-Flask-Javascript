$(document).ready(function () {

    let boton = document.querySelector('#btn')

    let mymap = L.map('mapid').setView([-38.74039392086135, -72.59666919708252], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);

    boton.addEventListener('click', (e) => {
        e.preventDefault()

        let id = document.querySelector('#vehiculo').value
        let date = document.querySelector('#fecha').value
        let mapa = document.querySelector('#mapid').innerHtml = ''

        $.getJSON(`http://127.0.0.1:5000/gps_track/${id}/${date}`, function (data,) {

            let latitud = -38.7508;
            let longitud = -72.6063;;
            mymap.remove();
            // mymap.off();

            if (typeof data.datos[0] === 'undefined') {
                alert('No hay registros de ese día')
            } else {
                longitud = data.datos[0][0]
                latitud = data.datos[0][1]
            }
            console.log(latitud, longitud)
            //-38.7508/-72.6063

            mymap = L.map('mapid',{attributionControl: false}).setView([latitud, longitud], 13);

            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1
            }).addTo(mymap);

            var geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "LineString",
                            "coordinates": data.datos
                        }
                    }
                ]
            }

            L.geoJSON(geojson).addTo(mymap)


        });


       
    })
    $('.leaflet-control-attribution').hide()
});