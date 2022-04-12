# 02 Requests
In the previous example, we created our first FastAPI application. We also went ahead and ran it with `uvicorn`. In this post, we are going to look at how requests are made and how a response is returned.  

Each time we create a route like below, we create a function that handles a request to a given URL, this function is invoked when we visit a URL.

```python
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
def greet_optional_name(name:Optional[str]="World"):

    return {"message": f"Helo {name}"}
```  
We have created two URLs one is `/{name}` and this takes in a path parameter. The second one is `/greet` and this should take in an optional query parameter `name` that defaults to `"World"`.  


### Let us change something.
For the previous examples, we have been using our web Browser to make requests to our URLs. We are going to change to [Insomnia](https://insomnia.rest/). This is an open-source API client that allow us to easily and quickly send [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [SOAP](https://en.wikipedia.org/wiki/SOAP) and [GRPC](https://en.wikipedia.org/wiki/GRPC) requests.  

I know that has been a lot. But basically `Insomnia` will really help us to make requests to our REST API easily.  

### Steps to Use Insomnia
1. Download one for your operating system [here](https://insomnia.rest/download) and Install it.  

2. Open it and you will see the following home screen.  

![Insomnia home](../images/insomnia-home.png)  

3. Create a request collection  

![request collection](../images/request-collection.png)  

4. Give the collection a name  

![request collection name](../images/request-name.png)

5. Then you will go to this UI  
![request home](../images/request-home.png)

6. Create a request and make a request  
![create a request](../images/make%20a%20request.png)  


### Note
I will be using Insomnia in this course, please feel free to use other API clients. Ok, so let use try accessing the other URLS on our API at this point. 

## Path Parameters
We shall begin with the `/{name}` endpoint which is going to take in a path parameter.  


![Path parameters](../images/path%20parameters.png)  

In this example we have passed a name `jona` within our URL and then made a `GET` request to the `/{name}` endpoint. This allows us to return the JSON response of `{"name": "Hello jona"}`.

Our path parameter is the name `"jona"` which is a string. This name is taken in by our request handler function that will return response as we see above. Our function takes in the `name` which is a string and in this case we are using type hints to specify that we shall have our name as a function.  
```python
def greet_name(name:str):
    
    return {"name":f"Hello {name}"}

```  

FastAPI heavily relies on type hints to determine what request handlers take and also to validate the data that we pass to our API as we shall see later when sending  `POST` and `PUT` requests.  

## Query parameters
Now let us make a request to our `/greet` URL and see what happens.


