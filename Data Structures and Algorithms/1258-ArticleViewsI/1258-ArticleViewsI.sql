-- Last updated: 6/7/2026, 11:25:40 PM
# Write your MySQL query statement below
SELECT DISTINCT(author_id) as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;