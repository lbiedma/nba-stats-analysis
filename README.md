# nba-api-examples
Notebooks with Examples of how to use a [Python wrapper for the NBA API](https://github.com/swar/nba_api), for learning and testing purposes.

## PageRank to get NBA "Power Rankings"
[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/PageRankNBA.ipynb) gets into downloading regular season game results and using them to estimate each team's Page Rank, from downloading the data to creating the matrix for which we will apply the Power Method to obtain the dominant eigenvalue and its eigenvector (the final pagerank scores).

## Change in Pace in the NBA
[This notebook](https://github.com/lbiedma/nba-api-examples/blob/main/AvgPossessionsOverTime.ipynb) downloads teams' advanced data for the last 20 regular seasons and provides a couple of plots (using Plotly) to show how the pace of the game has elevated. This also includes scraping teams' primary and secondary colors and adding them to the plots. Scraping algorithm and CSV file provided in this repo.
