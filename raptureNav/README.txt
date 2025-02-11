RAPTURENAV by Christian Dresen
Python file: raptureNav.py

DESC: This is a low-tech tool I made to help me visualize road trips, for an experimental roadtrip-centric TTRPG I was developing.
It visualizes the 50 states, allows you to set waypoints and their descriptions, and allows you to connect them if there is a straight path.
It's pretty clunky, and probably not that useful for anything other than my niche intended use case, but I'm uploading it so that anyone
who wants to can use it for free.

HOW TO USE:
Click anywhere on the map to create a waypoint. You will be prompted to enter a name and description (though you don't NEED to enter a description).
The first waypoint you set will have a green "home" icon. The map will show this waypoint as your current location (with the white bouncing box).
Consecutive waypoints will have a yellow "flag" icon.
You can travel between waypoints (changing your current location) if a straight line exists between two waypoints. (Oceans and Great Lakes obstruct this line, using a mask).
Click on the waypoint you want to travel to. If a green "Drive" icon is available (with a picture of a car), click on it to travel there. This will create a road, if one doesn't already exist.
You can also view, edit, and delete waypoints by clicking on them.

The program automatically saves your data when you close it.

To reset the data, go to SaveData\PinData and delete the entire contents of the folder.

Happy travels!
