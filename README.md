# Data Analysis and Machine Learning with NBA Stats' API
Notebooks with Examples of how to use a [Python wrapper for the NBA API](https://github.com/swar/nba_api), for learning and testing purposes.

## Four Factors Analysis and Linear Model Adjustment for the Last 20 Seasons

![pic](https://github.com/lbiedma/nba-api-examples/blob/main/images/4factors.png)

[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/FourFactorsAnalysis.ipynb) tries to follow up on [Squared2020 Blog introducing the Four Factors](https://squared2020.com/2017/09/05/introduction-to-olivers-four-factors/), adjusting a linear model for the last 20 seasons and check how important each of these factors turned out to be.
## PageRank to get NBA "Power Rankings"

![pic](https://github.com/lbiedma/nba-api-examples/blob/main/images/pagerankscores.png)

[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/PageRankNBA.ipynb) gets into downloading regular season game results and using them to estimate each team's Page Rank, from downloading the data to creating the matrix for which we will apply the Power Method to obtain the dominant eigenvalue and its eigenvector (the final pagerank scores).

## Change in Pace in the NBA

![pic](https://github.com/lbiedma/nba-api-examples/blob/main/images/posspermin.png)

[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/AvgPossessionsOverTime.ipynb) downloads teams' advanced data for the last 20 regular seasons and provides a couple of plots (using Plotly) to show how the pace of the game has elevated. This also includes scraping teams' primary and secondary colors and adding them to the plots. Scraping algorithm and CSV file provided in this repo.

## Computing the Offensive Rating of all NBA Players

![pic](https://github.com/lbiedma/nba-api-examples/blob/main/images/ortg.png)

[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/OffensiveRatings.ipynb) shows the computation of the Offensive Rating for each player in a specific regular season, following the formulae created by Dean Oliver, which were published in his book: [Basketball on Paper](http://www.basketballonpaper.com/).
