from flask import Flask, render_template, redirect, url_for
import time

app = Flask(__name__)

class CookieClicker:
    def __init__(self):
        self.cookies = 0
        self.cps = 0
        self.upgrades = 0

    def click(self):
        self.cookies += 1

    def buy_upgrade(self):
        upgrade_cost = 10 * (self.upgrades + 1)
        if self.cookies >= upgrade_cost:
            self.cookies -= upgrade_cost
            self.upgrades += 1
            self.cps += 1

    def auto_collect(self):
        self.cookies += self.cps

# Initialize the game object
game = CookieClicker()

@app.route('/')
def index():
    return render_template('index.html', cookies=game.cookies, cps=game.cps, upgrades=game.upgrades)

@app.route('/click')
def click():
    game.click()
    game.auto_collect()
    return redirect(url_for('index'))

@app.route('/buy_upgrade')
def buy_upgrade():
    game.buy_upgrade()
    game.auto_collect()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
