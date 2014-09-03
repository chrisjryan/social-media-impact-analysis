# What is the typical content of high, medium, and low impact tweets?

Here, the post history is analyzed for Twitter profiles that are maintained to promote two recent documentary films: [The Square](http://en.wikipedia.org/wiki/The_Square_%282013_film%29) and [How to Survive a Plague](http://en.wikipedia.org/wiki/How_to_Survive_a_Plague). The former depicts the ongoing Egyptian Revolution of 2011 from its roots in Tahrir Square. The latter describes the early years of the AIDS epidemic, and the efforts & struggles of activist groups.

The films have both significant similarities and differences. Both tell the stories of grassroots activist movements and consist of 'fly on the wall' footage covering a small set of leaders. Both films were released during similar times, and both were recognized with Academy Award nominations. However, while one ('Plague') is a historical struggle during the 80s and 90s and has something of a resolution, the other ('Square') covers a recent and ongoing movement. For this latter film, social media outreach is thus not only a means of recognizing import and heroic efforts, but of promoting a cause for which the filmmakers want to gather global support. 

Modern tools of social media provide a great opportunity for filmmakers to advance their work and keep followers updated with news. However, it can be challenging to know how to best manage these tools. To this end, the brief analysis shown below looks at a dataset of past tweets and begins to examine at how their content correlates with impact.

Note: Since the data set for the "The Square" contains many more tweets than that for "How to Survive a Plague" (3156 instead of 1309) and is over a much shorter time span (2 months instead of 2+ years), <strong>the analysis here focuses on "The Square"</strong>. Corresponding plots for "How to Survive a Plague" are found in the Appendix.


## Measuring impact: beyond retweets

For a given tweet, a particularly helpful proxy measurement of impact is the number of times it has been retweeted. This number can be acquired straightforwardly via the usual methods for harvesting batches of recent Twitter posts (a.k.a. "status updates", a.k.a. "tweets"). The charts below break down the contents of tweets (i.e., whether they contain photos, hashtags, url links to some article, or combination of these) from [the Twitter account promoting The Square](https://twitter.com/TheSquareFilm). All the tweets posted from January 2014 to March 2014 were broken into 3 categories based on whether they were retweeted 0 times, 1 to 5 times, or >5 times.

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Contents of tweets for 'The Square' 

<p align="center">
  <img src="https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/sq_pie_0retweets.png"  width=215/>
  <img src="https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/sq_pie_1to5retweets.png" width=250/>
  <img src="https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/sq_pie_morethan5retweets.png" width=250/>
</p>

The above plots show that the lowest impact tweets typically contain no links, hashtags, or photos. Tweets with a few retweets more often contain hashtags sometimes combined with links. Both make good sense -- hashtags allow tweets to arise when users sort feeds using them, and links may be to articles that elaborate on an important issue or news item. The tweets with the highest numbers of rewteets have hashtags that are sometimes combined with photographs. Though there are certainly more details worth considering, this begins to suggest how to better get people's attention on Twitter. Looking at the highly-retweeted tweets in particular, hashtags alone seem about as useful as useful as hashtags combined with photos. <strong>But let's look closer at this subset of data...</strong>

Tweets that reach many users of social media are not just retweeted, but are retweeted by users with a large following. To examine this, additional information was gathered from the Twitter API for each tweet that was retweeted more than 5 times. This information provided a follower count for each retweeter of each tweet. Thus, <strong>for each tweet in the ">5 retweets" subset, a sum of all the followers of each retweeter was calculated</strong>. As a shorthand, we can refer to this number as a <strong>summed followers count</strong> for each tweet in our set of interest. (Using terms from the theory social networks, this is the sum of the [degree centrality](http://en.wikipedia.org/wiki/Centrality#Degree_centrality) of each retweeter for a given tweet -- specifically the indegree centrality, since our network is a directed graph and it is the users' follower counts that are being added. But this is getting a bit beyond the scope here.)

The values of the summed followers count for this data set ranged from 304 to 2052877; for 52 tweets this was on the order of 10<sup>6</sup> and for 6 tweets this was on the order of 10<sup>7</sup> (histograms can be viewed [here](https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/summed_followers_hist.png) ). These data were then segmented into quantiles -- the top 10 tweets were contained in the tenth quantile, the 20th to 11th highest values were in the next highest set, and so on. Finally, the content of these ten sets were analyzed in the same manner as the pie charts above.

<p align="center">
  <img src="https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/sq_stackedbar_morethan5retweets_quantiles.png"  width=400/>
</p>

This breakdown provides a closer look at the data contained in the ">5 retweets" pie chart. In particular, it can now be seen that the very highest-impact tweets tend to contain both photos & hashtags (green) when compared to hashtags only (yellow), which are found in the lower quantile. In the pie chart, all these data were aggregated together and the usefulness of a photo in addition to a hashtag was not clear.


## Discussion

This analysis sheds some light on how tweet content relates to impact, however the results here merit careful thought and some scrutiny:

- It is currently inconsistent to use present-day data about the followers-count for each retweeter when the retweeting may have occurred a long time ago. A Twitter user's follower count could double over a few months, or this growth could be punctuated by certain events. Since all data here is from two months in 2014 this effect isn't so significant, but when computing these plots for data across a long timescale, the data set could be broken into batches of 'equally old' tweets (and even this should be considered thoughtfully).
- A subset of tweets posted by an account will also be retweets of other accounts' tweets. How to optimize this for impact could be another interesting issue.
- The follower count for each retweeter was summed for each tweet, however this is not generally a sum of unique users. Users may follow more than 1 of the retweeters.
- A subset of the ">5 retweet" data was not used for stacked bar plot, since these results required some extra handling.


Future work might consider:

- Tweet frequency. Is more tweeting always better, or does this dilute the most important messages?
- Twitter activity for films is highly affected by certain events -- especially theater/Netflix release dates and award ceremonies. Analysis of these events should be complex and might consider data outside of a tweet set, such as release locations and ticket sales.
- What time of day is best for posting updates?
- How should anything learned for a film/account of a given size be applied to larger or smaller films?
- Other than tweet content, users have control over how their profile is designed. How can this be optimized?
- How do any discovered patterns in Twitter vary by location and native language?

__________________________

### Appendix
<p></p>

#### Tweet content plots for "How to Survive a Plague"
<p></p>

- [pie plot, tweets with 0 retweets](https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/pl_pie_0retweets.png)

- [pie plot, tweets with 1 to 5 retweets](https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/pl_pie_1to5retweets.png)

- [pie plot, tweets with >5 retweets](https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/pl_pie_morethan5retweets.png)

- [stacked bar plot with 10-quantile breakdown for tweets with >5 retweets](https://raw.githubusercontent.com/christopherjamesryan/social-media-impact-analysis/master/pl_stackedbar_morethan5retweets_quantiles.png)