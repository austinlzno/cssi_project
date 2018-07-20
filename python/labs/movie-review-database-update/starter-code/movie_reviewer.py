#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
interstellar_movie = {
    "title": "Interstellar",
    "id": "tt0816692",
    "year_released": 2014,
    "rating": "PG",
    "score": 8.6,
    "out_of": 10,
    "reviews": 1191327
}

print ""

the_imitation_game_movie = {
    "title": "The Imitation Game",
    "id": "tt2084970",
    "year_released": 2014,
    "rating": "PG-13",
    "score": 8,
    "out_of": 10,
    "reviews": 580771
}

print ""

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

print ""

# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/

inside_movie ["year_released" ] =  2015
inside_movie ["score"] = 8.2
inside_movie ["reviews"] = 489496


for x,y in interstellar_movie.items():
    print(' {k} : {v} '.format(k=x, v=y))

    print ""

for x,y in the_imitation_game_movie.items():
    print(' {k} : {v} '.format(k=x, v=y))

    print ""

for x,y in inside_movie.items():
    print(' {k} : {v} '.format(k=x, v=y))

    print ""
