## Overview

This project is a simple Twitter application.

This project uses Django Framework and Redis In Memory key-Value store.

## Requirements
Python 3.6,
Redis : https://redis.io,
##Note: This code assumes Redis running on local setup. This can be easily extended to the Redis Cluster or larger Redis and Persistent environments.

## Usage
To run the server, please execute the following from the root directory:
pip3 install -r requirements.txt

python3 manage.py runserver

and open your browser to here:

http://localhost:8000/feed

For just JSON output use:

http://localhost:8000/feed?format=json

Query Paramters::
count:number of tweets, default:20
since_id:from tweet id, default:None
userid:User id, default:1
format:html/json, default:json



