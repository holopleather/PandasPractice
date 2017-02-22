import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print('Head:')
print(movies.head())
print()

print('Columns: ')
print(movies.columns)
print()

print('Shape: ')
print (movies.shape)
print()

# Output:
# Head:
#    star_rating                     title content_rating   genre  duration  \
# 0          9.3  The Shawshank Redemption              R   Crime       142
# 1          9.2             The Godfather              R   Crime       175
# 2          9.1    The Godfather: Part II              R   Crime       200
# 3          9.0           The Dark Knight          PG-13  Action       152
# 4          8.9              Pulp Fiction              R   Crime       154
#
#                                          actors_list
# 0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...
# 1    [u'Marlon Brando', u'Al Pacino', u'James Caan']
# 2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...
# 3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...
# 4  [u'John Travolta', u'Uma Thurman', u'Samuel L....
#
# Columns:
# Index(['star_rating', 'title', 'content_rating', 'genre', 'duration',
#        'actors_list'],
#       dtype='object')
#
# Shape:
# (979, 6)

# Example 1
print('Example 1: ')
print('Sorting Series')
print('Alphabetical Ascending (Default)')
print(movies.title.sort_values())
#OR movies['title'].sort_values()
print()
print('Alphabetical Descending: ')
print(movies.title.sort_values(ascending=False))
print()

# Output:
# Example 1:
# Alphabetical Ascending (Default)
# 542                   (500) Days of Summer
# 5                             12 Angry Men
# 201                       12 Years a Slave
# 698                              127 Hours
# 110                  2001: A Space Odyssey
# 910                                   2046
# 596                               21 Grams
# 624                              25th Hour
# 708                       28 Days Later...
# 60                                3 Idiots
# 225                                 3-Iron
# 570                                    300
# 555                           3:10 to Yuma
# 427           4 Months, 3 Weeks and 2 Days
# 824                                     42
# 597                                  50/50
# 203                                  8 1/2
# 170                       A Beautiful Mind
# 941                       A Bridge Too Far
# 571                           A Bronx Tale
# 266                      A Christmas Story
# 86                      A Clockwork Orange
# 716                         A Few Good Men
# 750                    A Fish Called Wanda
# 276                   A Fistful of Dollars
# 612                     A Hard Day's Night
# 883                  A History of Violence
# 869              A Nightmare on Elm Street
# 865                        A Perfect World
# 426                              A Prophet
#                       ...
# 207       What Ever Happened to Baby Jane?
# 562            What's Eating Gilbert Grape
# 719                When Harry Met Sally...
# 649                      Where Eagles Dare
# 33                                Whiplash
# 669                Who Framed Roger Rabbit
# 219        Who's Afraid of Virginia Woolf?
# 127                      Wild Strawberries
# 497    Willy Wonka & the Chocolate Factory
# 270                        Wings of Desire
# 483                           Withnail & I
# 920                                Witness
# 65             Witness for the Prosecution
# 970                            Wonder Boys
# 518                         Wreck-It Ralph
# 954                                  X-Men
# 248             X-Men: Days of Future Past
# 532                     X-Men: First Class
# 871                                     X2
# 695                      Y Tu Mama Tambien
# 403                             Ying xiong
# 235                                Yip Man
# 96                                 Yojimbo
# 280                     Young Frankenstein
# 535                                  Zelig
# 955                       Zero Dark Thirty
# 677                                 Zodiac
# 615                             Zombieland
# 526                                   Zulu
# 864                                  [Rec]
# Name: title, dtype: object

# Alphabetical Descending:
# 864                                  [Rec]
# 526                                   Zulu
# 615                             Zombieland
# 677                                 Zodiac
# 955                       Zero Dark Thirty
# 535                                  Zelig
# 280                     Young Frankenstein
# 96                                 Yojimbo
# 235                                Yip Man
# 403                             Ying xiong
# 695                      Y Tu Mama Tambien
# 871                                     X2
# 532                     X-Men: First Class
# 248             X-Men: Days of Future Past
# 954                                  X-Men
# 518                         Wreck-It Ralph
# 970                            Wonder Boys
# 65             Witness for the Prosecution
# 920                                Witness
# 483                           Withnail & I
# 270                        Wings of Desire
# 497    Willy Wonka & the Chocolate Factory
# 127                      Wild Strawberries
# 219        Who's Afraid of Virginia Woolf?
# 669                Who Framed Roger Rabbit
# 33                                Whiplash
# 649                      Where Eagles Dare
# 719                When Harry Met Sally...
# 562            What's Eating Gilbert Grape
# 207       What Ever Happened to Baby Jane?
#                       ...
# 426                              A Prophet
# 865                        A Perfect World
# 869              A Nightmare on Elm Street
# 883                  A History of Violence
# 612                     A Hard Day's Night
# 276                   A Fistful of Dollars
# 750                    A Fish Called Wanda
# 716                         A Few Good Men
# 86                      A Clockwork Orange
# 266                      A Christmas Story
# 571                           A Bronx Tale
# 941                       A Bridge Too Far
# 170                       A Beautiful Mind
# 203                                  8 1/2
# 597                                  50/50
# 824                                     42
# 427           4 Months, 3 Weeks and 2 Days
# 555                           3:10 to Yuma
# 570                                    300
# 225                                 3-Iron
# 60                                3 Idiots
# 708                       28 Days Later...
# 624                              25th Hour
# 596                               21 Grams
# 910                                   2046
# 110                  2001: A Space Odyssey
# 698                              127 Hours
# 201                       12 Years a Slave
# 5                             12 Angry Men
# 542                   (500) Days of Summer
# Name: title, dtype: object

# Example 2
print('Example 2')
print('Sorting DataFrame by Series')
print('Movies by Title (Alphabetical Ascending):')
print(movies.sort_values('title').head())
print()
print('Movies by Duration (Ascending):')
print(movies.sort_values('duration').head())
print()
print('Movies by Duration (Descending):')
print(movies.sort_values('duration', ascending=False).head())
print()
print('Movies by Content Rating and Duration:')
print(movies.sort_values(['content_rating', 'duration']).head())

# Output:
# Example 2
# Sorting DataFrame by Series
# Movies by Title (Alphabetical Ascending):
#      star_rating                  title content_rating      genre  duration  \
# 542          7.8   (500) Days of Summer          PG-13     Comedy        95
# 5            8.9           12 Angry Men      NOT RATED      Drama        96
# 201          8.1       12 Years a Slave              R  Biography       134
# 698          7.6              127 Hours              R  Adventure        94
# 110          8.3  2001: A Space Odyssey              G    Mystery       160
#
#                                            actors_list
# 542  [u'Zooey Deschanel', u'Joseph Gordon-Levitt', ...
# 5    [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...
# 201  [u'Chiwetel Ejiofor', u'Michael Kenneth Willia...
# 698  [u'James Franco', u'Amber Tamblyn', u'Kate Mara']
# 110  [u'Keir Dullea', u'Gary Lockwood', u'William S...
#
# Movies by Duration (Ascending):
#      star_rating                        title content_rating    genre  \
# 389          8.0                       Freaks        UNRATED    Drama
# 338          8.0          Battleship Potemkin        UNRATED  History
# 258          8.1  The Cabinet of Dr. Caligari        UNRATED    Crime
# 293          8.1                    Duck Soup         PASSED   Comedy
# 88           8.4                      The Kid      NOT RATED   Comedy
#
#      duration                                        actors_list
# 389        64  [u'Wallace Ford', u'Leila Hyams', u'Olga Bacla...
# 338        66  [u'Aleksandr Antonov', u'Vladimir Barsky', u'G...
# 258        67  [u'Werner Krauss', u'Conrad Veidt', u'Friedric...
# 293        68    [u'Groucho Marx', u'Harpo Marx', u'Chico Marx']
# 88         68  [u'Charles Chaplin', u'Edna Purviance', u'Jack...
#
# Movies by Duration (Descending):
#      star_rating                              title content_rating      genre  \
# 476          7.8                             Hamlet          PG-13      Drama
# 157          8.2                 Gone with the Wind              G      Drama
# 78           8.4        Once Upon a Time in America              R      Crime
# 142          8.3  Lagaan: Once Upon a Time in India             PG  Adventure
# 445          7.9               The Ten Commandments       APPROVED  Adventure
#
#      duration                                        actors_list
# 476       242  [u'Kenneth Branagh', u'Julie Christie', u'Dere...
# 157       238  [u'Clark Gable', u'Vivien Leigh', u'Thomas Mit...
# 78        229  [u'Robert De Niro', u'James Woods', u'Elizabet...
# 142       224  [u'Aamir Khan', u'Gracy Singh', u'Rachel Shell...
# 445       220  [u'Charlton Heston', u'Yul Brynner', u'Anne Ba...
#
# Movies by Content Rating and Duration:
#      star_rating                           title content_rating      genre  \
# 713          7.6                 The Jungle Book       APPROVED  Animation
# 513          7.8  Invasion of the Body Snatchers       APPROVED     Horror
# 272          8.1                     The Killing       APPROVED      Crime
# 703          7.6                         Dracula       APPROVED     Horror
# 612          7.7              A Hard Day's Night       APPROVED     Comedy
#
#      duration                                        actors_list
# 713        78  [u'Phil Harris', u'Sebastian Cabot', u'Louis P...
# 513        80  [u'Kevin McCarthy', u'Dana Wynter', u'Larry Ga...
# 272        85  [u'Sterling Hayden', u'Coleen Gray', u'Vince E...
# 703        85  [u'Bela Lugosi', u'Helen Chandler', u'David Ma...
# 612        87  [u'John Lennon', u'Paul McCartney', u'George H...