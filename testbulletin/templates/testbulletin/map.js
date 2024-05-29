console.log("yyyyyyyyyyyyyyyyyyyy")
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
// const map = L.map('map')
const url =  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const osm = L.tileLayer(url, { attribution: copy });
// .addTo(map);
map.fitWorld();
const map = L.map("map",
    { layers: [osm], minZoom: 3 });
// map.locate()
//     .on("locationfound", (e) => map.setView(e.latlng, 8))
//     .on("locationerror", () => map.setView([60, 30], 5));
const queryset = JSON.parse(document.getElementById("queryset-data").textContent);
const features = L.geoJSON(queryset).bindPopup(layer => layer.feature.properties.name);

map.addLayer(features).fitBounds(features.getBounds());