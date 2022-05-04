from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',)
def page_index():

    page_content = """ 
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Моя страничка</title>
        <link rel="stylesheet" type="text/css" href="/static/styles/style.css" />
    </head>
    <body>
        <h1>Куприянов Александр Андреевич</h1>
        <br>
        <img src="/static/images/my_foto.png" width="300" alt="Моё фото" />
        <br>
        <div>
        <p>Привет я житель <strong>Российской Федерации </strong>.<em>Проживаю на берегу красивейшего пресного озера "Байкал"</em> в городе Иркутск.</p>
        <a href = "https://vk.com/cyber666fox"> Я в соцсетях.</a>
        <br>
        <p>На этой странице буду <del>публиковать всякую дичь</del> свой код и ссылки на GitHub </p>
        <a href = "https://github.com/Cyber666Fox"> Я в GitHub.</a>
        <br>
        <p>Код мой выглядит сейчас так себе <mark>,потому что я только учусь.</mark></p>
        </div>
    </body>
    </html>
    """
    return page_content


app.run()