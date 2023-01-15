### db作成
sqlite3 db-name

### create table
CREATE TABLE score_results(
  movie_name STRING,
  user STRING,
  parts STRING,
  timing_category STRING,
  time_from STRING,
  time_to STRING,
  results BOOLEAN,
  comment STRING,
  PRIMARY KEY(movie_name, user, parts)
);

### insert
INSERT INTO score_results VALUES('sample1.mov', '白井', '腕', '投げ始め', '00:02', '00:04', TRUE, '高さが十分で良い');

### select
SELECT * FROM score_results