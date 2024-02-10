# import required packages
import webbrowser
import folium
import os
import json

# generate a map with or without opening
def generateMap(open_map: bool = True):
    # get settings
    with open('settings.json') as f:
        settings = json.load(f)
        f.close()

    # create map
    m = folium.Map(location=[settings["start_location"][0],
                             settings["start_location"][1]],
                   zoom_start=settings["start_zoom"])
    m.add_child(folium.LatLngPopup())

    # add tag for office
    folium.Marker(
            location=[settings["home_address"][0], settings["home_address"][1]],
            popup=settings["home_tag"],
            icon=folium.Icon(color=settings["home_color"], icon='house-flag', prefix='fa')
        ).add_to(m)

    # get all markers
    with open('markers.json') as f:
        file_tags = json.load(f)
        f.close()

    # get all files
    r = []
    for root, dirs, files in os.walk('files'):
        for name in files:
            r.append(os.path.join(root, name))

    # put file tags on map
    for item in file_tags["markers"]:
        # attempt to find file
        file_path = "null"
        for filename in r:
            base = os.path.basename(filename)
            name = os.path.splitext(base)[0]
            if name == item[0]:
                file_path = filename

        # add marker
        if file_path == "null":
            folium.Marker(
                location=[item[1], item[2]],
                popup=item[0],
                icon=folium.Icon(color=settings["tag_color"], icon='clipboard-question', prefix='fa')
            ).add_to(m)
        else:
            file_path = file_path.replace("\\", "/")  # swap slashes
            folium.Marker(
                location=[item[1], item[2]],
                popup="<a href=" + file_path + ">" + item[0] + "</a>",
                icon=folium.Icon(color=settings["tag_color"], icon='clipboard-user', prefix='fa')
            ).add_to(m)

    # save and open map
    html_path = os.path.abspath(os.getcwd()) + "/DataMapper.html"
    m.save(html_path)
    if open_map:
        webbrowser.open('file://' + html_path)
