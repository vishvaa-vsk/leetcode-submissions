-- Last updated: 6/7/2026, 11:25:41 PM
# Write your MySQL query statement below
select tweet_id
from Tweets
where LENGTH(content) > 15;