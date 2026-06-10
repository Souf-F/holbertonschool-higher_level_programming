# Task 0: Basics of HTTP/HTTPS

## Overview
HTTP (HyperText Transfer Protocol) and HTTPS (HTTP Secure) are the fundamental protocols used for data communication on the web. This document provides a comprehensive understanding of these protocols, their differences, structure, methods, and status codes.

---

## Part 1: Differentiating HTTP and HTTPS

### What is HTTP?
HTTP is an application-layer protocol that defines how messages are formatted and transmitted between web clients (browsers, applications) and web servers. It operates on port 80 by default.

### What is HTTPS?
HTTPS is the secure version of HTTP that uses SSL/TLS (Secure Sockets Layer/Transport Layer Security) encryption to protect data transmitted between client and server. It operates on port 443 by default.

### Key Differences

| Aspect | HTTP | HTTPS |
|--------|------|-------|
| **Port** | 80 | 443 |
| **Encryption** | None | SSL/TLS Encryption |
| **Security** | Data visible to eavesdroppers | Data encrypted and hidden |
| **URL Format** | `http://example.com` | `https://example.com` |
| **Data Integrity** | No verification | Verified with certificates |
| **Use Cases** | Public, non-sensitive content | Banking, emails, sensitive data |
| **Performance** | Slightly faster | Minimal overhead from encryption |
| **Browser Indicator** | No special indicator | Green padlock icon |

### Security Aspects

**HTTP Vulnerabilities:**
- Data transmitted in plain text
- Susceptible to man-in-the-middle attacks
- No authentication of server identity
- No data integrity verification

**HTTPS Protections:**
- Data encrypted using SSL/TLS
- Protects against eavesdropping
- Authenticates server identity via digital certificates
- Ensures data hasn't been tampered with
- Prevents man-in-the-middle attacks

**The "S" in HTTPS = Secure**

Modern web browsers display a green padlock icon for HTTPS connections, indicating a secure connection. Websites handling sensitive data (banking, healthcare, e-commerce) must use HTTPS.

---

## Part 2: Understanding HTTP Structure

### HTTP Request Structure

An HTTP request consists of:

```
METHOD /path/to/resource HTTP/1.1
Host: example.com
Header1: Value1
Header2: Value2
Content-Type: application/json

Body (optional)
```

**Components:**

1. **Request Line**
   - Method (GET, POST, PUT, DELETE, etc.)
   - Path (URI/URL of the resource)
   - HTTP Version (HTTP/1.1 or HTTP/2)
   - Example: `GET /api/users/1 HTTP/1.1`

2. **Headers**
   - Metadata about the request
   - Format: `Header-Name: Value`
   - Common headers:
     - `Host`: Target server domain
     - `User-Agent`: Client information
     - `Content-Type`: Type of data being sent
     - `Accept`: Expected response format
     - `Authorization`: Authentication credentials

3. **Body (Optional)**
   - Data sent with the request
   - Used in POST, PUT, PATCH requests
   - Not used in GET, DELETE requests

### HTTP Response Structure

A server responds with:

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1234
Server: Apache/2.4.1

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Components:**

1. **Status Line**
   - HTTP Version
   - Status Code (e.g., 200, 404, 500)
   - Status Message (e.g., OK, Not Found, Server Error)
   - Example: `HTTP/1.1 200 OK`

2. **Headers**
   - Metadata about the response
   - Common headers:
     - `Content-Type`: Format of response data
     - `Content-Length`: Size of response body
     - `Server`: Server software information
     - `Set-Cookie`: Session cookies

3. **Body**
   - The actual response data
   - Could be HTML, JSON, XML, etc.
   - Empty for some status codes (204, 304)

### Example Request-Response Cycle

```
CLIENT                          SERVER
  |                              |
  |--- GET /users HTTP/1.1 ---->|
  |                              |
  |    Host: api.example.com     |
  |    Accept: application/json  |
  |                              |
  |<---- HTTP/1.1 200 OK --------|
  |                              |
  |    Content-Type: app/json    |
  |    Content-Length: 256       |
  |                              |
  |    [JSON Response Body]      |
  |                              |
```

---

## Part 3: Common HTTP Methods

HTTP methods (also called verbs) define the type of action to be performed on a resource.

### The Main HTTP Methods

| Method | Purpose | Data Sent | Idempotent | Safe | Use Case |
|--------|---------|-----------|-----------|------|----------|
| **GET** | Retrieve data | No body | Yes | Yes | Fetching a web page, API data, images |
| **POST** | Create new data | In body | No | No | Submitting forms, creating new records |
| **PUT** | Replace entire resource | In body | Yes | No | Updating a complete user profile |
| **PATCH** | Partial update | In body | No | No | Updating specific user fields |
| **DELETE** | Remove resource | No body | Yes | No | Deleting a user account or record |
| **HEAD** | Like GET, no body | No body | Yes | Yes | Check resource without downloading |
| **OPTIONS** | Describe communication | No body | Yes | Yes | Check allowed methods for a resource |

### Detailed Explanations

**GET Method**
- Description: Retrieves data from a server without modifying it
- Body: No request body
- When to use: Fetching a web page, API data, images, documents
- Example: `GET /api/users/1 HTTP/1.1` → Returns user with ID 1

**POST Method**
- Description: Submits data to server to create a new resource
- Body: Contains the data to create
- When to use: Submitting forms, creating new records, uploading files
- Example: `POST /api/users HTTP/1.1` with JSON body creates a new user

**PUT Method**
- Description: Replaces an entire resource with new data
- Body: Contains complete replacement data
- When to use: Updating entire records, complete replacement
- Example: `PUT /api/users/1 HTTP/1.1` replaces user 1 completely

**PATCH Method**
- Description: Partially updates a resource
- Body: Contains only the fields to update
- When to use: Updating specific fields without replacing everything
- Example: `PATCH /api/users/1 HTTP/1.1` updates only specified fields

**DELETE Method**
- Description: Removes a resource from the server
- Body: No request body
- When to use: Deleting records, accounts, files
- Example: `DELETE /api/users/1 HTTP/1.1` deletes user with ID 1

---

## Part 4: Common HTTP Status Codes

HTTP status codes indicate the result of an HTTP request. They're grouped into five categories:

### Status Code Categories

- **1xx (Informational)**: Request received, processing continues
- **2xx (Success)**: Request succeeded
- **3xx (Redirection)**: Further action needed to complete request
- **4xx (Client Error)**: Request contains error or can't be fulfilled
- **5xx (Server Error)**: Server failed to fulfill valid request

### Five Most Common Status Codes

#### 1. Status Code: 200 OK
- **Category**: 2xx Success
- **Description**: Request succeeded. The response contains the requested data.
- **Meaning**: Everything worked as expected
- **Scenario Examples**:
  - User successfully logs in
  - API call returns requested data
  - Form submission processed successfully
  - Website loads successfully
- **Example Response**:
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json
  
  {"status": "success", "data": {...}}
  ```

#### 2. Status Code: 404 Not Found
- **Category**: 4xx Client Error
- **Description**: The requested resource could not be found on the server
- **Meaning**: The URL or resource doesn't exist
- **Scenario Examples**:
  - User visits a non-existent webpage
  - API call requests a user that doesn't exist
  - Accessing a deleted resource
  - Typo in URL path
- **Example Response**:
  ```
  HTTP/1.1 404 Not Found
  Content-Type: text/html
  
  <html>404 - Page Not Found</html>
  ```

#### 3. Status Code: 500 Internal Server Error
- **Category**: 5xx Server Error
- **Description**: The server encountered an unexpected condition that prevented it from fulfilling the request
- **Meaning**: Something went wrong on the server's side
- **Scenario Examples**:
  - Database connection fails
  - Code exception or crash
  - Server runs out of memory
  - Unhandled error in API endpoint
- **Example Response**:
  ```
  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json
  
  {"error": "An unexpected error occurred"}
  ```

#### 4. Status Code: 401 Unauthorized
- **Category**: 4xx Client Error
- **Description**: Authentication is required but missing or invalid
- **Meaning**: User credentials not provided or invalid
- **Scenario Examples**:
  - User tries to access protected content without login
  - API token is expired or invalid
  - Missing authentication header
  - Wrong password provided
- **Example Response**:
  ```
  HTTP/1.1 401 Unauthorized
  WWW-Authenticate: Bearer realm="api"
  
  {"error": "Authentication required"}
  ```

#### 5. Status Code: 201 Created
- **Category**: 2xx Success
- **Description**: The request succeeded and a new resource was created
- **Meaning**: POST request successfully created a new resource
- **Scenario Examples**:
  - New user account created successfully
  - API creates a new database record
  - New file uploaded successfully
  - New comment posted on a post
- **Example Response**:
  ```
  HTTP/1.1 201 Created
  Location: /api/users/123
  Content-Type: application/json
  
  {"id": 123, "username": "newuser", "email": "user@example.com"}
  ```

### Additional Common Status Codes

| Code | Name | Scenario |
|------|------|----------|
| 204 | No Content | Request succeeded but no content to return (DELETE) |
| 301 | Moved Permanently | Resource moved to new URL (permanent redirect) |
| 302 | Found | Resource temporarily at different URL (temporary redirect) |
| 400 | Bad Request | Malformed request (invalid syntax) |
| 403 | Forbidden | User authenticated but lacks permission |
| 502 | Bad Gateway | Invalid response from upstream server |
| 503 | Service Unavailable | Server temporarily unavailable (maintenance) |

---

## Summary: HTTP Status Code Classes

```
1xx: Informational
    Request received, continuing process

2xx: Success
    Action was successfully received, understood, and accepted
    - 200 OK: Standard successful response
    - 201 Created: Resource created
    - 204 No Content: Request succeeded, no content

3xx: Redirection
    Further action must be taken to complete the request
    - 301 Moved Permanently
    - 302 Found (temporary redirect)
    - 304 Not Modified

4xx: Client Error
    Request contains error or cannot be fulfilled
    - 400 Bad Request
    - 401 Unauthorized
    - 403 Forbidden
    - 404 Not Found

5xx: Server Error
    Server failed to fulfill valid request
    - 500 Internal Server Error
    - 502 Bad Gateway
    - 503 Service Unavailable
```

---

## Key Takeaways

### HTTP/HTTPS
- HTTPS is HTTP with encryption using SSL/TLS
- Always use HTTPS for sensitive data
- Encryption prevents eavesdropping and man-in-the-middle attacks

### HTTP Structure
- Requests consist of: Method, Headers, Body (optional)
- Responses consist of: Status Line, Headers, Body
- Headers provide metadata about request/response

### HTTP Methods
- GET: Retrieve data (safe, idempotent)
- POST: Create new resources
- PUT: Replace entire resources
- PATCH: Update specific fields
- DELETE: Remove resources

### Status Codes
- 2xx: Success
- 3xx: Redirection
- 4xx: Client errors (fix the request)
- 5xx: Server errors (fix the server)

---

## Practical Application

Understanding HTTP/HTTPS is essential for:
- Web development
- API creation and consumption
- Security implementation
- Debugging network issues
- Building scalable applications

This knowledge forms the foundation for working with RESTful APIs, building web services, and understanding modern web architecture.
