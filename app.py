from flask import Flask, render_template
import string
import random
from password import PasswordGenerator


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


app = Flask(__name__)

app.config["SECRET_KEY"] = "Praveen@10"


@app.route("/", methods=["GET", "POST"])
def password():

    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    form = PasswordGenerator()

    new_password = ""
    strg = ""

    if form.validate_on_submit():

        length = form.password.data

        # Character pool
        characters = []

        if form.uppercase.data:
            characters += upper

        if form.lowercase.data:
            characters += lower

        if form.numbers.data:
            characters += numbers

        if form.symbols.data:
            characters += symbols

        # Generate password
        if characters:

            password_list = []

            for i in range(length):
                password_list.append(random.choice(characters))

            random.shuffle(password_list)

            new_password = "".join(password_list)

            # Check password strength
            strg = password_strength(new_password)

    return render_template(
        "pass.html",
        form=form,
        new=new_password,
        strg=strg
    )


if __name__ == "__main__":
    app.run(debug=True)