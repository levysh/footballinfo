### FOOTBALL INFO
Запросы лежат в src/app/queries. Что бы запустить локально используй 

    cd src
    ./run.sh
    
Пример запроса в src/app/routes/queries/queries.py 

    @bp.route("/players", methods=["GET", "POST"])
    def players():
        ...
        
Что бы добавить свой запрос:
* добавь запрос в папку src/app/queries
* напиши форму в src/app/forms.py
* напиши эндпоинт в src/app/routes/queries/queries.py по примеру с /players
* добейся работоспособности