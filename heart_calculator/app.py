from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    # if request.method == "POST":
    #     print(request.form["name"])
    #     print(request.form["email"])

    age_list = ['<20', '20><35', '35><60', '60<']
    gender_list = ['Male', 'Female']
    profession_list = ['Desk Job', 'Field Job', 'Standing Job/Physical Activity',
                    'Exaercise Daily', 'Exercise once a week', 'Never']
    how_often_list = ['Once a Week', 'Once a Month', 'Twice or More in a Week']
    family_history_list = ['Yes', 'No']

    return render_template('home.html', age_list=age_list, gender_list=gender_list,
                            profession_list=profession_list,
                            how_often_list=how_often_list, family_history_list=family_history_list)

if __name__ == "__main__":
    app.run()
