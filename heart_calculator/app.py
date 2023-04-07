from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    age_list = ['<20', '20><35', '35><60', '60<']
    gender_list = ['Male', 'Female']
    profession_list = ['Desk Job', 'Field Job', 'Standing Job']
    physical_act_list = ['Exercise Daily', 'Exercise once a week', 'Never']
    how_often_list = ['Once a Week', 'Once a Month', 'Twice or More in a Week']
    family_history_list = ['Yes', 'No']

    if request.method == "POST":
        age = request.form.get('age')
        gender = request.form.get('gender')
        pro = request.form.get('profession')
        physical = request.form.get('physical')
        often = request.form.get('how_often')
        history =request.form.get('family_history')
        return  "Your age is: " + age + "<br>Gender is: " + gender + "<br>Profession is: " + pro + "<br>Physical Activities: " + physical + "<br>You eat fried foods: " + often + "<br>Family history: " + history

    return render_template('index.html', age_list=age_list, gender_list=gender_list,
                            physical_act_list=physical_act_list, profession_list=profession_list,
                            how_often_list=how_often_list, family_history_list=family_history_list)

if __name__ == "__main__":
    app.run()
