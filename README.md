# Team 3
<h3>Dallin Gordon, Sonu Kumar, Rakin Munim, Leo Zhang </h3>



All Pull Requests must follow the Pull Request Template, with a title formatted like such `[Project Name]: <Descriptive Title>`

1. <h4>What is the project focus/overall goal?</h4> 
To get a better idea about the distribution of landlords not enrolled in different affordable housing programs. Important features to be considered: number of units, geographic location, and the demographic profile of the census block group. We will also look into the percentage of housing stock that is owned by the owner occupied and the small landlords, and at % affordable.
2. <h4>What type of data will you collect or be analyzing?
</h4> The two main data sources are the current affordable housing listings database, and the 
current owner occupied units database.  The main request will rely on these.  Further analysis will benefit from Census or demographic data.  

3. <h4>What are potential limitations of the project?
</h4>We are hoping that we can find a cleaner way to join the two primary databases.  If not,  the join will be on address and likely involve lower integrity.  Linking up demographic data will likely have similar challenges.  We want to look at generation of citizenship, and some other demographics that may require additional data sources.  

4. <h4>Why is this project important or Why did you choose this project?
</h4>We have chosen this assignment since many students opt to live in Boston after college for work. Since housing discrimination can have large implicit biases and have consequences for years, we wish to understand how Boston is meeting affordable housing for different demographics. 
5. <h4>What is your team’s next steps? (include action items/tasks)
</h4>Our next steps are to wait for Tom to get back to us about whether or not he can join the 2 datasets we have been provided. From here either we can move forward with the joined data or we will have to join the data ourselves. Following this we will have to clean the data. From then on we can begin processing the data. Some demographics we will explore are income, race, gender, neighborhood. Also we wish to see general affordability information about Boston’s neighborhoods. 


<i>Meeting times scheduled for after class on Wednesdays.</i>


<h1>Deliverable 1 </h1>

<h1> Notebooks for datasets </h1>
We have explored different datasets in different notebooks. If we need to mix different datasets then we will use our a new notebook and provide a decription of what datasets(and derivatives) are used in that notebook. This section contains notebooks and their descriptions. 


<h2> landPDExploration.ipynb </h2>
<h3> Databases </h3>

https://datacommon.mapc.org/browser/datasets/360

Goals of this notebook: 

Pull all residential properties from parcel database for Boston & Identify which are owner occupied and how many units for each property

<h3> Dervived Data Files </h3>
bostonParcelsData.csv

<h2>Post Analysis of Dataset</h2>
This dataset is not very well suited for our analysis, since it doesn't offer information about whether or not a housing unit is owner occupied or affordable. It does contain a great breadth of all units in Boston, however the main issue with the data is that the row identfiers for any given property don't seem to have a match with other datasets. Thus it will be very hard to use this dataset with the other datasets we have been provided. If the PM or someone from City Council could fill us in on this dataset's dictionary we could have some use for it in the future for the extended project. 

----------
<h2> data_explore.ipynb </h2>
<h3> Databases </h3>

Dataset with all Boston units:
https://data.boston.gov/dataset/property-assessment/resource/4b99718b-d064-471b-9b24-517ae5effecc

Dataset with Boston affordable housing stock:
http://www.bostonplans.org/housing/finding-housing/property-listings


Goals of this notebook: 

1. Obtain distribution of affordable housing stock across 
Boston.
2. Analyze all Boston Housing Units and distribution
3. See how we can mix data from Boston Housing Units and Affordable Housing Stock


<h2>Post Analysis of Datasets</h2>
In this notebook we were able to anaylze the distribution of Boston's affordable housing stock with respect to location. We also made attempts to read up on and understand the complete boston housing dataset. However we notice various issues when it came to mixing the affordable housing stock and all housing units dataset since the affordable housing stock had no specific information about the units at each location, made it hard to compare to the total housing dataset. For our next deliverable we need to cover this point. 




----------
<h2> incomeRestricted.ipynb </h2>
<h3> Databases </h3>

Dataset with income restricted units:
https://data.boston.gov/dataset/income-restricted-housing

Goals of this notebook: 

1. Obtain distribution of income restricted housing
Boston.
3. See how we can mix data with Boston Affordable Housing Stock and Complete Boston Housing


<h2>Post Analysis of Datasets</h2>
This notebook, while insightful with respect to understand where income restricted housing falls, is not going to be easy to join with the other datasets. This is due to the fact that the entries do not contain addresses or IDs, rather contain project name and neighborhood. While we can obtain information from the neighbohood sections we can't match income restricted housing projects to addresses. 


----------
<h2> Questions Answered for Deliverable 1</h2>

Refer to this Google doc:
https://docs.google.com/document/d/1WrUQUFYNWBPBuU7wWQBt6Q8ffXdFRXdMxk6GdVyaEiE/edit#



<h2>Updated Project Proposal </h2>

1. <h4>What is the project focus/overall goal?</h4> 
To get a better idea about the distribution of landlords not enrolled in different affordable housing programs. Important features to be considered: number of units, geographic location, and the demographic profile of the census block group. We will also look into the percentage of housing stock that is owned by the owner occupied and the small landlords, and at % affordable.
2. <h4>What type of data will you collect or be analyzing?
</h4> The 3 main data sources are the current affordable housing listings database, the current owner occupied units database and income restricted dataset.  The main request will rely on these .  Further analysis will benefit from Census or demographic data.  

3. <h4>What are potential limitations of the project?
</h4>Joining data across datasets will nearly impossible for income restricted dataset since no addresses are included only projects. Additionally the dataset for all Boston housing units has alot of garbage and unfilled in numbers, or numbers are just wrong. So quesitons that rely on these values will not be answerable since the data is incomplete.  Linking up demographic data will likely have similar challenges although we can use statiscal methods to estimate. 

4. <h4>Why is this project important or Why did you choose this project?
</h4>We have chosen this assignment since many students opt to live in Boston after college for work. Since housing discrimination can have large implicit biases and have consequences for years, we wish to understand how Boston is meeting affordable housing for different demographics.
5. <h4>What is your team’s next steps? (include action items/tasks)
</h4>Our next steps are to to clean the data furthermore so we can obtain more simple metrics and information about the data. Afterwords we can obtain data about demographics and census. This will then be included in the next deliverable. 

<h1>End of Deliverable 1</h1>