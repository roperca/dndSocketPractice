#import socket module
from socket import *
import sys # In order to terminate the program
"""
Web Server by Camryn Roper
this code is intended to be a very simple webserver. the goal is to understand how
webservers and tcp protocalls work.
Important Variables
serverSocket - the socket connected to the server
connectionSocket - the socket connected to the client
outputData - used to store the contents of the HTML file
other variables are self explanitory
"""
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
serverSocket.bind(('0.0.0.0', 6789)) #binds server to a particular host and any IP address
#TODO get ip address for this server and the helloworld.html webpage
serverSocket.listen(1) #listen for incoming connections
#number indicates queue size
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...\n')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    #above is a function that waits for a client to connect
    try:
        message = connectionSocket.recv(1024).decode('utf-8') #Fill in start #Fill in end
        # .recv prepares 1kb of memory for client to use(we can get more memory later if we need it)
        # .decode turns data human readable using utf-8 protocol

        #print(f"Received request: {message}") # Debug print to see the request

        filename = message.split()[1]

        #print(f"Requested file: {filename}") # Debug print to see the filename

        f = open(filename[1:])
        outputdata = f.read().encode('utf-8') # Read file contents and encode

        #print(f"File contents: {outputdata}") # Debug print to see the file content
        f.close()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        #assignment wasnt clear what version so i used http1.1
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode()) # End of header section
        #I grabed this from ChatGPT4o because that seemed the best way
        #to make sure i got the header lines and protocals right
        #Fill in end
        #Send the content of the requested file to the client

        connectionSocket.send(outputdata)#i replaced the loop with this bc i was having some issues
        #edit was made at recomendation from chatGPT
        connectionSocket.send("\r\n".encode())#blank line indicates end of content
        connectionSocket.close()#close connection

    except IOError:
        #Send response message for file not found
        #Fill in start

        #print("File not found, sending 404...") # Debug print

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        #grabbed header protocal from ChatGPT4o
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
    #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data