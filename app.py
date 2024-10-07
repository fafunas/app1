import folium

#Coordinates SN
map=folium.Map(location=(-33.3372385,-60.2167618),
               zoom_start=13,
               tiles="OpenStreetMap")

#Add coordinates with name, and the coordinates in a Tuple
coordinates =[
    {"name": "Estadio San Nicolas","coord":(-33.34390,-60.26441),"link":"https://www.estadiosannicolas.com.ar/"},
    {"name": "Autodromo San Nicolas","coord":(-33.39559,-60.20145),"link":"http://www.autodromosannicolas.com.ar/"},
    {"name": "Santuario","coord":(-33.32245,-60.22381),"link":"https://www.virgendesannicolas.org/"}

]

html="""
<h1>%s</h1>
<br>
<p><a href="%s" target="_blank">Visit this link</a></p

"""

for item in coordinates:
    iframe= folium.IFrame(html=html % (item["name"],item["link"]),width=400,height=400)
    map.add_child(folium.Marker(location=(item["coord"]),
                            popup=folium.Popup(iframe),
                            icon=folium.Icon(color="green")))
map.save("index.html")