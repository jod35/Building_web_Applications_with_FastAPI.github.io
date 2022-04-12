# 02 Requests
In the previous example, we created our first FastAPI application. We also went ahead and ran it with `uvicorn`. In this post, we are going to look at how requests are made and how a response is returned.  

Each time we create a route like below, we create a function that handles a request to a given URL, this function is invoked when we visit a URL.

```
@app.get("/")
def index():
    return {"message": "Helo World"}

```  
In this example, we are making a request to the `/` URL and are getting a JSON response of `{"message": "Helo World"}`.  

The route decorator specified includes an HTTP method that is used when making a request. In our example, this is the `GET` request. Now let us create more routes by adding this code.

```python
@app.get('/{name}')
def greet_name(name:str):
    
    return {"name":f"Hello {name}"}


@app.get("/greet")
def greet_otional_name(name:Optional[str]="World"):

    return {"message": f"Helo {name}"}
```