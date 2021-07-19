# sqlalchemy-challenge
This project mainly contains 3 parts. 
<ul>
<li>Climate Analysis and Exploration</li>
<li>Climate App</li>
<li>Temperature analysis</li>
</ul>
<h2><strong>Climate Analysis and Exploration</strong></h2>
A notebook named climate_starter.ipynb contains the precipitation analysis and station analysis by connecting to the sqlite database provided in the Resources folder.
<h3><strong>Precipitation Analysis</strong></h3>
A plot is added to depict the precipitation data for the last 12 months.
<h3><strong>Station Analysis</strong></h3>
This shows the different stations available and a histogram of last 12 months' temperature observations data of most active station.
<h2><strong>Climate App</strong></h2>
The app is added in App.py. It shows available routes in the home page.<br>
Each route and the data displayed by them are as following.<br>
<ul>
<li>/api/v1.0/precipitation - displays the dates and precipitation values for the last 12 months.</li>
<li>/api/v1.0/stations - displays the different stations available.</li>
<li>/api/v1.0/tobs - displays the dates and temperature observations of the most active station for the last year of data.</li>
<li>/api/v1.0/start - displays the minimum temperature, the average temperature, and the maximum temperature for all dates greater than or equal to the start date.<br/>or 
<li>/api/v1.0/start/end - displays the minimum temperature, the average temperature, and the maximum temperature for dates between the start and end date inclusive.</li>
</ul>
<h2><strong>Temperature Analysis</strong></h2>
The Bonus parts are added in  temp_analysis_bonus_1_starter.ipynb and temp_analysis_bonus_1_starter.ipynb<br><br>
It identifies the average temperature for June and December across available years.<br>
Also a t-test is added to determine whether the difference in the means, if any, is statistically significant. The analysis is added at the end of temp_analysis_bonus_1_starter.ipynb.<br><br>
The second part of temperature analysis identifies the average temperature and total rainfall for a given timeframe.<br>
It also plots the daily temperature normals(minimum, maximum, and average) for the given timeframe.<br>
