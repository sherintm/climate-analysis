# sqlalchemy-challenge
This project mainly contains 3 parts. 
<ul>
<li>Climate Analysis and Exploration</li>
<li>Climate App</li>
<li>Temperature analysis</li>
</ul>
## Climate Analysis and Exploration
A notebook named climate_starter.ipynb contains the precipitation analysis and station analysis by connecting to the sqlite database provided in the Resources folder.
### Precipitation Analysis
A plot is added to depict the precipitation data for the last 12 months.
### Station Analysis
This shows the different stations available and a histogram of last 12 months' temperature observations data of most active station.
##Climate App
The app is added in App.py. It shows available routes in the home page.<br>
Each route and the data displayed by them are as following.<br>
<ul>
<li>/api/v1.0/precipitation - displays the dates and precipitation values for the last 12 months</li>
<li>/api/v1.0/stations - displays the different stations available</li>
<li>/api/v1.0/tobs - displays the dates and temperature observations of the most active station for the last year of data.</li>
<li>/api/v1.0/start - displays the minimum temperature, the average temperature, and the max temperature for all dates greater than and equal to the start date.<br/>or 
<li>/api/v1.0/start/end - displays the minimum temperature, the average temperature, and the max temperature for dates between the start and end date inclusive</li>
## Temperature analysis
The Bonus parts are added in  temp_analysis_bonus_1_starter.ipynb and temp_analysis_bonus_1_starter.<br><br>
It identifies the average temperature for June and December across available years.<br>
Also a t-test is added to determine whether the difference in the means, if any, is statistically significant. The analysis is added at the end of temp_analysis_bonus_1_starter.ipynb.<br><br>
The second part of temperature analysis identifies the average temperature and total rainfall for a given timeframe.<br>
It also plots the daily temperature normals(minimum, maximum, and average) for the given timeframe.<br>
