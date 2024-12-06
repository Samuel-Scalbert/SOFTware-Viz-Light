from app.app import app, db
from flask import render_template
from Utils.software import software_all_mentions, dataset_creator

@app.route('/<software>')
def software_mentions(software):
    data = software_all_mentions(software,db)
    return render_template('pages/software_mentions.html',data = data)
