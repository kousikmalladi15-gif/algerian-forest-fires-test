---
title: Algerian Forest Fires Prediction
emoji: 🔥
colorFrom: red
colorTo: yellow
sdk: docker
app_port: 7860
---
Algerian Forest Fire Dataset: Data Strategy & Preprocessing:
When we set out to build this prediction model, the primary goal was to take the raw Algerian Forest Fire data and turn it into a streamlined tool for estimating the Fire Weather Index (FWI). To get there, we had to make some specific calls on what data to keep, what to throw away, and how to reshape the categorical variables so the math actually works.

Why We Kept Certain Features:
In the world of forest fires, not all weather data is created equal. We focused on the parameters that have a physical "cause and effect" relationship with how the wood and leaves burn.

The Basics (Temp, RH, Wind, Rain):
These are the non-negotiables. Temperature and Humidity determine how dry the fuel is, Wind Speed dictates how much oxygen the fire gets and how fast it travels, and Rain is the only natural "reset" button for fire risk.

The Moisture Codes (FFMC & DMC):
We kept these because they track different layers of the forest floor. The FFMC tells us about the dry needles and twigs on top (which start fires), while the DMC tells us about the deeper organic layers (which keep fires burning).

The Rate of Spread (ISI):
This value is crucial because it combines wind speed and fuel moisture to tell us how fast a fire would move if it started right now.

Why We Removed Certain Data:
A lot of the raw dataset was "noise" that would have actually confused the model rather than helped it.

Date and Time Columns:
While fires happen in "seasons," the specific day of the month doesn't cause a fire—the weather on that day does. By removing dates, we forced the model to look at the actual environmental conditions instead of just memorizing that "August is hot."

Incomplete Records:
We took a hard line on missing data. If a row was missing a humidity or rain reading, we removed it entirely. In machine learning, guessing a missing value (imputation) can sometimes introduce bias, and we wanted this model to be as clean as possible.

Statistical Outliers:
We filtered out extreme anomalies that looked like recording errors. If the data showed a weather pattern that was physically impossible for that region, it was tossed to ensure the model stayed grounded in reality.

The Logic Behind Binary Conversions:
linear models aren't great at understanding the textual feature value of a place name like "Bejaia" or a status like "Fire." They only speak numbers.

Region Mapping: We decided to treat the two regions (Bejaia and Sidi-Bel Abbes) as a binary switch (0 and 1). This allows the model to account for the unique geographic differences between the two areas without needing complex text processing.

Class Mapping:
Similarly, for "Fire Status," we converted the labels to 0 (No Fire) and 1 (Fire). This turns a descriptive label into a mathematical weight that the ElasticNet model can use to adjust its final FWI prediction.

The User Experience:
Even though the model sees 0s and 1s, we built the interface with dropdown menus. This way, the end user can select a region by name, and the code handles the "translation" into math behind the scenes using the concepts of hashmaps a.k.a. dictionaries.

Technical Note on Scaling:
Finally, we applied a StandardScaler to the input features. Because Relative Humidity is measured in percentages (0-100) while the Rain is measured in millimeters (often 0-5), because the model might think that th e Humidity is "more important" just because the size of numbers differ a lot from one feature to another. Scaling levels the playing field so every feature gets a fair say in the final result.