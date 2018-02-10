console.log("App firing up...");

const $ = require('jquery');
const mapboxgl = require('mapbox-gl');
mapboxgl.accessToken = 'pk.eyJ1IjoiZHVuY2FucmFnZXIiLCJhIjoidlN6TWZTQSJ9.wRF8gxx6x679fF8ZsMxMQg';

const currentIndex = 6;
let index = currentIndex;
const locations = {
  1: [-77.0369, 38.9072],
  2: [-84.4472, 39.0751],
  3: [-94.5786, 39.0997],
  4: [-104.9903, 39.7392],
  5: [-111.8910, 40.7608],
  6: [-122.1661, 37.4241]
};

const backTrack = require('./backTrack.json');
const forwardTrack = require('./forwardTrack.json');
const destinations = require('./destinations.json');

const backtrackLayer = {
    "id": "backTrack",
    "type": "line",
    "source": {
        "type": "geojson",
        "data": backTrack
    },
    "layout": {
        "line-join": "round",
        "line-cap": "round"
    },
    "paint": {
        "line-color": "#4B0082",
        "line-width": 5
    }
}

const forwardtrackLayer = {
    "id": "forwardTrack",
    "type": "line",
    "source": {
        "type": "geojson",
        "data": forwardTrack
    },
    "layout": {
        "line-join": "round",
        "line-cap": "round"
    },
    "paint": {
        "line-color": "#888",
        "line-width": 2
    }
}

const destinationLayer = {
    "id": "destinations",
    "type": "circle",
    "source": {
        "type": "geojson",
        "data": destinations,
    },
    "paint": {
        "circle-radius": {
            "property": "status",
            "type": "categorical",
            "stops": [
                ["past", 10],
                ["current", 14],
                ["future", 7]
            ]
        },
        "circle-color": {
            "property": "status",
            "type": "categorical",
            "stops": [
                ["past", "#4B0082"],
                ["current", "#008000"],
                ["future", "#888"]
            ]
        }
    }
}

const destinationLabels = {
    "id": "destination-labels",
    "type": "symbol",
    "source": {
        "type": "geojson",
        "data": destinations,
    },
    "layout": {
        "text-field": "{eta}",
        "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
        "text-offset": [0, 1],
        "text-anchor": "top"
    },
    "paint": {
        "text-color": "#202",
        "text-halo-color": "#fff",
        "text-halo-width": 3
    }
}



const map = new mapboxgl.Map({
    container: 'map-div',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: locations[currentIndex],
    zoom: 6
});

map.on('load', () => {
    map.addLayer(backtrackLayer);
    map.addLayer(forwardtrackLayer);
    map.addLayer(destinationLayer);
    map.addLayer(destinationLabels);
})

$('#forward-button').on('click', () => {
    index += 1;
    index = index > 6 ? 6 : index;
    map.flyTo({
        center: locations[index],
        zoom: 6
    });
});

$('#current-button').on('click', () => {
    index = currentIndex;
    map.flyTo({center: locations[currentIndex]});
});

$('#backward-button').on('click', () => {
    index -= 1;
    index = index < 1 ? 1 : index;
    map.flyTo({
        center: locations[index],
        zoom: 6
    });
});