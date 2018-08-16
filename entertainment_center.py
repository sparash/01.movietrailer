import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to his life",
                        "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_QL50_SY1000_SX670_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_QL50_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

blackpanther = media.Movie("Black Panther",
                           "Black Panther is a 2018 American superhero film based on the Marvel Comics character of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the eighteenth film in the Marvel Cinematic Universe (MCU). The film is directed by Ryan Coogler, who co-wrote the screenplay with Joe Robert Cole, and stars Chadwick Boseman as T'Challa / Black Panther, alongside Michael B. Jordan, Lupita Nyong'o, Danai Gurira, Martin Freeman, Daniel Kaluuya, Letitia Wright, Winston Duke, Angela Bassett, Forest Whitaker, and Andy Serkis. In Black Panther, T'Challa is crowned king of Wakanda following his father's death, but his sovereignty is soon challenged by a new adversary who plans to abandon the country's isolationist policies and begin a global revolution.",
                           "https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=xjDjIWPwcPU")
#print(blackpanther.storyline)
#blackpanther.show_trailer()

infinitywar = media.Movie("Avengers: Infinity War",
                          "Avengers: Infinity War is a 2018 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. It is the sequel to 2012's The Avengers and 2015's Avengers: Age of Ultron, and the nineteenth film in the Marvel Cinematic Universe (MCU).",
                          "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=QwievZ1Tx-8")
#print(infinitywar.storyline)
#infinitywar.show_trailer()

dp2 = media.Movie("Deadpool 2",
                  "Deadpool 2 is a 2018 American superhero film based on the Marvel Comics character Deadpool, distributed by 20th Century Fox. It is the eleventh installment in the X-Men film series, and a direct sequel to the 2016 film Deadpool.",
                  "https://m.media-amazon.com/images/M/MV5BMjI3Njg3MzAxNF5BMl5BanBnXkFtZTgwNjI2OTY0NTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                  "https://www.youtube.com/watch?v=D86RtevtfrA")
#print(dp2.storyline)
#dp2.show_trailer()

thor = media.Movie("Thor: Ragnarok",
                   "Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. It is the sequel to 2011's Thor and 2013's Thor: The Dark World, and is the seventeenth film in the Marvel Cinematic Universe (MCU).",
                   "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")
#print(thor.storyline)
#thor.show_trailer()

movies = [toy_story, avatar, blackpanther, infinitywar, dp2, thor]
fresh_tomatoes.open_movies_page(movies)
