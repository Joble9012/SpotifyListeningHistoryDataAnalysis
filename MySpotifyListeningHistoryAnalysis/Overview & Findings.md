Project Overview

This project analyzes a personal Spotify listening history dataset to uncover music listening patterns, preferences, and trends over time. Raw data was provided in multiple JSON files containing metadata about each played track, including timestamps, track and artist details, and play duration in milliseconds. The project begins by consolidating and cleaning this data into a single structured CSV file, removing unnecessary metadata such as platform details, IP addresses, and audiobook-related fields. The cleaning process also filters out irrelevant entries (e.g., "White Noise 3 Hour Long"), ensures consistent datetime formatting, converts listening duration to minutes, and retains only records from 2018 onward to focus on recent listening habits.

After cleaning, the dataset becomes a reliable foundation for analysis. Using pandas, the project performs exploratory data analysis to identify top artists, most played tracks, and overall listening time. Additional preprocessing steps include handling missing values, renaming columns for clarity, and filtering out entries with incomplete core metadata. By structuring the dataset in this way, the analysis becomes more interpretable and avoids noise from irrelevant or inconsistent entries.

The analysis phase applies descriptive statistics and visualization to extract insights. Metrics such as total listening hours, the most frequently played artists, and the tracks with the highest total listening time are calculated. These findings can reveal patterns in musical tastes, highlight shifts in genre preferences over the years, and quantify engagement with different artists. The cleaned dataset and resulting insights can also be used for further advanced analysis—such as seasonal listening trends, genre distribution, or correlations between time of day and listening choices—making the project a scalable foundation for deeper musical behavior exploration.

Findings:
 
