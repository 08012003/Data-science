# APIs (Application Programming Interfaces)

## What is an API?
- An API is a set of rules that allow one software application to interact with another.
- It acts like a bridge that helps different applications communicate with each other.
- APIs can be used for retrieving data from a server, sending data, or interacting with other services.

**Example:**
- If you want to get weather data for a city, you can use a weather API. 
- For example, you could send a request to `https://api.weather.com/v1/current?city=London` to get weather data.

## What is a RESTful API?
- REST stands for Representational State Transfer.
- It is a type of API that follows certain rules to provide a simple way to access resources.
- RESTful APIs use HTTP methods (GET, POST, PUT, DELETE) to perform operations.
- They are stateless, meaning each request is independent and does not rely on previous ones.

**Example of RESTful API Request:**
- **GET** `/users/123` would retrieve information for user with ID 123.
- **POST** `/users` would create a new user.
- **PUT** `/users/123` would update user 123's information.
- **DELETE** `/users/123` would delete user 123.

## Difference Between Web API and API
- **API**: General term for any kind of interface that allows software to communicate.
- **Web API**: A specific type of API that works over the web, typically using HTTP. It is often used for web services and allows interaction with servers via the internet.

**Example:**
- A **Web API** could be an API provided by a website to interact with its services, like an API for fetching movie data from an online database.
- A **general API** might be used to interact with a local application or service that doesn’t necessarily involve the internet.

## REST and SOAP Architecture

### REST Architecture
- **Stateless**: Each request from a client contains all the necessary information.
- **Uniform Interface**: A consistent interface for interaction (like using URLs to represent resources).
- **Cacheable**: Responses can be cached for performance improvement.
- **Client-Server**: The client and server are separate, allowing for more flexibility.
- **Layered System**: APIs can be structured in layers for scalability.

**Example of a RESTful API Endpoint:**
- `https://api.example.com/users/123` to get information about the user with ID 123.
- `https://api.example.com/products` to get a list of products.

### SOAP Architecture
- **Protocol-based**: SOAP uses a strict set of rules for communication (XML-based).
- **Stateful**: SOAP can maintain state, making it more complex.
- **Message-driven**: SOAP focuses on the message format and can be more secure and reliable than REST.
- **Transport Protocol**: SOAP can work over different protocols like HTTP, SMTP, and more.

**Example of a SOAP Request:**
- A SOAP request might look like this:
  ```xml
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                    xmlns:web="http://www.example.com/webservice">
      <soapenv:Header/>
      <soapenv:Body>
         <web:GetUserDetails>
            <userID>123</userID>
         </web:GetUserDetails>
      </soapenv:Body>
  </soapenv:Envelope>
