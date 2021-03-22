# rasa_general_bot
- To train a bot 
    $ rasa train --data data  -c config.yml -d domain.yml
- To run bot as an API
    $ rasa run --model models --debug --enable-api
- To hit the API
    $ curl -X POST http://0.0.0.0:6666/chat -d '{"sender": "user1", "message": "how are u"}' -H "Content-Type: application/json"   