i# Task 1: Consume Data from an API Using Command Line Tools (curl)

## Overview

`curl` (Client URL) is a command-line tool that allows you to transfer data using URLs. It's essential for testing APIs, debugging, and interacting with web services directly from the command line.

---

## Part 1: Installing and Using curl

### What is curl?

`curl` is a free tool that makes HTTP requests from the command line. It supports:
- HTTP/HTTPS protocols
- Custom headers
- Different HTTP methods (GET, POST, PUT, DELETE, etc.)
- File uploads/downloads
- Authentication

### Installation

**On Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install curl
```

**On macOS:**
```bash
brew install curl
```

**On Windows:**
Use WSL (Windows Subsystem for Linux) or download from: https://curl.se/download.html

### Verify Installation

```bash
curl --version
```

**Expected Output:**
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0 OpenSSL/1.1.1
Release-Date: 2020-01-08
Protocols: file ftp ftps http https imap imaps ldap ldaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: AsynchDNS IPv6 Largefile GSS-API Kerberos SPNEGO NTLM NTLM_WB SSL libz UnixSockets
```

---

## Part 2: Basic curl Usage

### Simple GET Request

**Fetch a webpage:**
```bash
curl http://example.com
```

Returns the HTML content of the website.

### Fetch Data from JSONPlaceholder API

JSONPlaceholder is a fake REST API for testing and prototyping.

**Get all posts:**
```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Output (first few posts):**
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae..."
  }
]
```

**Get a specific post:**
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
}
```

---

## Part 3: Working with Headers

### View Only Headers

Use the `-I` flag to fetch only response headers without the body.

**Syntax:**
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Output:**
```
HTTP/1.1 200 OK
Date: Wed, 10 Jun 2026 10:30:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 27645
Connection: keep-alive
Server: cloudflare
Cache-Control: public, max-age=14400
ETag: W/"6bed-3WrwjWZIOpxvB5MV+llo4GV6M58"
Vary: Origin
```

### Add Custom Headers

Use the `-H` flag to add headers to your request.

**Syntax:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/data
```

**Example:**
```bash
curl -H "User-Agent: MyApp/1.0" https://jsonplaceholder.typicode.com/posts/1
```

### View Response Headers and Body

Use `-i` flag to see both headers and body:

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

---

## Part 4: HTTP Methods with curl

### GET Request (Default)

Retrieve data from the server:

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

Or explicitly:
```bash
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

---

### POST Request (Create)

Create new data on the server.

**Syntax:**
```bash
curl -X POST -d "param1=value1&param2=value2" https://api.example.com/endpoint
```

**JSONPlaceholder Example:**
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Output:**
```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

**With JSON data:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"foo","body":"bar","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

---

### PUT Request (Replace)

Replace an entire resource.

**Syntax:**
```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"title":"updated","body":"updated body","userId":1}' \
  https://jsonplaceholder.typicode.com/posts/1
```

**Output:**
```json
{
  "title": "updated",
  "body": "updated body",
  "userId": 1,
  "id": 1
}
```

---

### PATCH Request (Partial Update)

Update only specific fields.

**Syntax:**
```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"title":"new title"}' \
  https://jsonplaceholder.typicode.com/posts/1
```

**Output:**
```json
{
  "userId": 1,
  "id": 1,
  "title": "new title",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum"
}
```

---

### DELETE Request (Remove)

Delete a resource.

**Syntax:**
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Output:**
```json
{}
```

---

## Part 5: Useful curl Flags

### Common Flags

| Flag | Description | Example |
|------|-------------|---------|
| `-X` | Specify HTTP method | `curl -X POST` |
| `-d` | Send data in body | `curl -d "key=value"` |
| `-H` | Add header | `curl -H "Authorization: Bearer token"` |
| `-I` | Show headers only | `curl -I https://...` |
| `-i` | Show headers + body | `curl -i https://...` |
| `-o` | Save to file | `curl -o file.json https://...` |
| `-O` | Save with original name | `curl -O https://...` |
| `-L` | Follow redirects | `curl -L https://...` |
| `-v` | Verbose (debug info) | `curl -v https://...` |
| `-u` | Basic auth | `curl -u user:pass https://...` |

### Examples

**Save response to file:**
```bash
curl https://jsonplaceholder.typicode.com/posts > posts.json
```

**Verbose output (see all details):**
```bash
curl -v https://jsonplaceholder.typicode.com/posts/1
```

**Follow redirects:**
```bash
curl -L https://example.com
```

**Basic authentication:**
```bash
curl -u username:password https://api.example.com/data
```

---

## Part 6: Formatting JSON Output with jq

When API responses are large, use `jq` to format JSON nicely.

### Install jq

```bash
sudo apt install jq
```

### Usage

**Pretty print JSON:**
```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.'
```

**Select specific fields:**
```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[].title'
```

**Output:**
```
"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
"qui est esse"
"ea molestias quasi exercitationem repellat qui ipsa sit aut"
...
```

**Filter by condition:**
```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[] | select(.userId == 1)'
```

---

## Part 7: Practical Examples

### Example 1: Get all users and count them

```bash
curl https://jsonplaceholder.typicode.com/users | jq 'length'
```

**Output:** `10`

---

### Example 2: Get user 1 data

```bash
curl https://jsonplaceholder.typicode.com/users/1 | jq '.'
```

**Output:**
```json
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough"
  }
}
```

---

### Example 3: Create a post and view response

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Post","body":"This is awesome!","userId":1}' \
  https://jsonplaceholder.typicode.com/posts | jq '.'
```

**Output:**
```json
{
  "title": "My First Post",
  "body": "This is awesome!",
  "userId": 1,
  "id": 101
}
```

---

### Example 4: Get comments for post 1

```bash
curl https://jsonplaceholder.typicode.com/posts/1/comments | jq '.'
```

---

## Part 8: Cheat Sheet

### Quick Reference

**GET:**
```bash
curl https://api.example.com/endpoint
```

**POST (JSON):**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/endpoint
```

**POST (Form):**
```bash
curl -X POST -d "key=value&key2=value2" https://api.example.com/endpoint
```

**PUT:**
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/endpoint/1
```

**DELETE:**
```bash
curl -X DELETE https://api.example.com/endpoint/1
```

**View Headers Only:**
```bash
curl -I https://api.example.com/endpoint
```

**Authentication:**
```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com/endpoint
```

**Save Response:**
```bash
curl https://api.example.com/endpoint > response.json
```

**Pretty Print JSON:**
```bash
curl https://api.example.com/endpoint | jq '.'
```

---

## Summary

### What You Learned

✅ How to install and use `curl`  
✅ Making GET requests to fetch data  
✅ Making POST requests to create data  
✅ Making PUT requests to replace data  
✅ Making PATCH requests to update data  
✅ Making DELETE requests to remove data  
✅ Working with headers  
✅ Formatting JSON output with `jq`  

### Key Points

- `curl` is a powerful tool for API testing and debugging
- Use `-X` to specify HTTP method
- Use `-d` to send data in the request body
- Use `-H` to add custom headers
- Use `-I` to see only response headers
- Use `jq` to format and filter JSON responses
- Always use HTTPS for sensitive data

### API to Practice With

JSONPlaceholder: https://jsonplaceholder.typicode.com/

Available endpoints:
- `/posts` - Blog posts
- `/users` - User information
- `/comments` - Comments on posts
- `/albums` - Photo albums
- `/photos` - Photos
- `/todos` - To-do items

---

## Next Steps

1. Practice making different curl requests
2. Explore different endpoints on JSONPlaceholder
3. Combine curl with `jq` for powerful data processing
4. Learn Python requests library for more advanced API work
