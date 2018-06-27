**Displays live weather in the i3blocks status bar**

**Credits**: <a href="https://github.com/csparpa/pyowm">PyOWM</a><br><br>
**Requirements:** 
<li><a href="https://github.com/vivien/i3blocks">i3blocks</a></li>
<li>fonts-font-awesome (Ubuntu: sudo apt install fonts-font-awesome)</li>
<li>pyowm (Ubuntu: pip install pyowm)<br></li>
<li><a href="https://openweathermap.org/api">OpenWeatherMap API Key</a> (Free accounts work quite well)</li>

<br>

Feel free to customize this script to add more weather details.

**Usage within *i3blocks.conf*:**

[weather]<br>
command=/path/to/file/weather.py<br>
interval=180 #updates every 3 minutes <br>

_Example Output:_<br>
<img src="https://github.com/Bee-Mar/i3blocks_live_weather/blob/master/i3blocks_weather.png"/>
