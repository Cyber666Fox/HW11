from flask import Flask, request, render_template
import utils


app = Flask (__name__)

@app.route ("/")
def page_index():
    items = utils.load_candidates_from_json()
    return render_template('list.html', items=items)

@app.route ("/candidate/<int:id>")
def page_card(id):
    item = utils.get_candidate(id)
    return render_template('card.html', item=item )

@app.route ("/search/<candidate_name>")
def page_name(candidate_name):
    items = utils.get_candidates_by_name(candidate_name)
    print(items)
    items_len = len(items)
    return render_template('search.html', items=items, items_сount=items_len)  

@app.route ("/skill/<skill_name>")
def page_skill(skill_name):
    items = utils.get_candidates_by_skill(skill_name)
    items_len = len(items)
    return render_template('skill.html', items=items, items_сount=items_len)   

app.run ()
