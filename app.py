from flask import Flask

app = Flask('__main__')

@app.route('/')
def home():
    return 'welcome home'

if __name__ == '__main__': app.run()
