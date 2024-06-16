## HTTP WEB SERVER from Scratch

- Stores Processes and Delivers web pages to the users.
- Communication is done using Http

![alt text](images/image-1.png)

```
If we open any file in chrome or any other browser it will open and this is not a creation of a web browser this is just a reading and rendering of a file.
The text on the search bar begins with "File", which is good for simple websites, but this won't work on Server side Scripts, Databases, etc as they need http and web browser to process there requests.

```

1. **Intitialize a Socket** -
   Sockets are the endpoint in network communication system, they allow the data to be sent and receive over the network.
   Enabling the connection between the client and the server they can handle multiple clients simultaneously.

## Note - HTTP is data sent or received through the sockets.

    AdressFamily in socket refers to an IP (Internet Protocol - Rules for routing or sending packets over network between the devices)
    When data travels over the Internet or web it travels in small packets, IP addresses ensures that devices like computer servers route those data packets to the correct place.

    SOCK_STREAM - TCP Socket (Transmission Control Protocol)
    Establishes connection between the sender and the Receiver and ensures that the data once it arrives is complete in order and error free, this process is established usinf a handshake mechanism.

![alt text](images/image-1.png)
SYN - sequence number of data packets
SYN-ACK - Acknowledges the SYN Packet and includes server's own sequence number
ACK - Acknowledges the servers SYN Packet
Data exchange starts.

    SOCK_DGRAM - UDP Socket (User Datagram Protocol)
    Sends datagram to the recipient without checking whether the recipient is ready to recieve the datagram or not.

Note - TCP ensures reliable transfer through error checking, retransmission when the packets are corrupted, and congestion control to reduce the network traffic load. Therefore it is uses where reliability and data integrity is more like web browsing and emails.
UDP doesn't establish a connection or handshake before sending data. The benefit is UDP is faster than TCP, therefore UDP is used in broadcasting services, online gaming, streaming, etc.

    DNS - Domain Name System. -- Mapping proper strings to the IP addresses.
    HTTP - 80
    HTTPS - 443
    Ports 0-1023 are for OS use only we can't use this.

![alt text](images/image-2.png)
HTTP Request -
1st line is the request line /HTTP/1.1 its usually the url but it can be a path too.
1.1 is the HTTP version and the versions in HTTP depicts the structure of the request.

    Version 0.9
    Network layer : IP
    Transport layer : TCP
    Methods : GET

    Version 1.0
    (add) Request Header
    (add) Version Field
    (add) Status Codes
    (add) Content Type
    (add) Methods : POST, HEAD

    Cache Control, Pipelining, sending second request before the first one is completed.
    New TCP was created for each HTTP call in previous versions, this is inefficient.

    Version 1.1 Connection can be reused.
    (add) Host Header
    (add) Persistent Connections
    (add) Continue Status
    (add) Methods : PUT, PATCH, DELETE, CONNECT, TRACE, OPTIONS.

    Version 2.0
    (add) Request Multiplexing
    (add) Request Prioritizing
    (add) Automatic Compressing
    (add) Connection Reset
    (add) Server Push

    Version 3.0
    (change) Transport Layer : QUIC
    QUIC - Quick UDP Internet connection - Built on top of UDP provided the reliability and ordering of TCP but with reduced latency and improved performance.
    In this the connection is identified using connection ids rather than connection IPs so switching from wifi to mobile data or any network won't have any effect.

Note - We are getting HTTP/1.1 because we have created a basic server created on TCP hence HTTP/3.0 is not used whic requires QUIC.
For HTTP/2.0 we need to have features like multiplexing which is handling Multiple requests at once.

    2nd line Domain Name
    3rd Connection keep alive - The client wants to keep the connections open rather than closing it right after this connection is fulfilled. The connection is reused.

    CORS - Cross Origin Resource Sharing - Security Mechanisms implemented by users to protect them from certains cyber attacks like Cross Site Request Forgery.

Succesfully created the Web server running for all methods -
![alt text](images/image-3.png)

Changing the methods.
Received the HTML page on GET Request - 
![alt text](images/image-4.png)

Remaining Requests are not allowed - 
![alt text](images/image-5.png)

Defining the path - 
![alt text](images/image-6.png)