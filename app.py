from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def green_glass(word):
    #can_pass = False
    for index in range(0, len(word)-1): # subtract 1 because word[index+1] would be out of bounds once word[i] is at the last character
        if word[index].lower() == word[index+1].lower():
            return True
    return False
            #can_pass = True
    #if can_pass:
        #print("You can pass the green glass door")
    #else:
        #print("Noooooo")
        
@app.route('/door-result', methods=['GET', 'POST'])
def door_result():
    user_guess = request.form['guess']
    if request.method == 'POST':
        does_pass = green_glass(user_guess)
        if does_pass == True:
            return render_template('can_pass.html', original_guess = user_guess)
        else: 
            return render_template('cannot_pass.html', original_guess = user_guess)
    else:
        return "<h1>Oops, something went wrong!</h1>"

@app.route('/palindrome-form')
def load_palindrome_checker():
    return render_template('palindrome_form.html')

def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

@app.route('/palindrome-result', methods=['GET', 'POST'])
def palindrome_result():
    input = request.form['palindrome-input']
    if request.method == 'POST':
        if is_palindrome(input) == True:
            return render_template('is_palindrome.html', original_input = input)
        else:
            return render_template('not_palindrome.html', original_input = input)
    else:
        return "<h1>Oops, something went wrong!</h1>"
# Test cases: 
#green_glass("GoOgle")
#green_glass("Dog")
#green_glass("BalL")
#green_glass("Llama")

if __name__ == '__main__':
    app.run(debug=True)