from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import store

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
        <h1> y  rrrrrrrrr luciana hijita  test 2  3/<h1>
    """

@app.get('/name')
def run():
    store.print(range)

if __name__ == '__main__':
    run()