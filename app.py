from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/can_pass', methods=['GET', 'POST'])



def green_glass(word):
    can_pass = False
    for index in range(0, len(word)-1): # subtract 1 because word[index+1] would be out of bounds once word[i] is at the last character
        if word[index].lower() == word[index+1].lower():
            # return True
            can_pass = True
    if can_pass:
        print("You can pass the green glass door")
    else:
        print("Noooooo")
        
green_glass("GoOgle")
green_glass("Dog")
green_glass("BalL")
green_glass("Llama")

if __name__ == '__main__':
    app.run(debug=True)