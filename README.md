# rasa_general_bot
- To train a bot 
    $ rasa train --data data  -c config.yml -d domain.yml
- To run bot as an API
    $ rasa run --model models --debug --enable-api
- To hit the API
    $ curl -X POST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "user1", "message": "hi"}'    