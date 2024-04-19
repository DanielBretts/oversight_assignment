import folium
map_test = folium.Map(location=(50, 0), zoom_start=8)#location - the center of the map, zoom_start - the resolution
map_test.save("map.html")
map_test