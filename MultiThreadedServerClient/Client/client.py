# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:16:42 2019

@author: xwc981
"""
import socket
import tkinter as tk
import os
from tkinter import filedialog
class ClientConnection:
    def __init__(self):
        root = tk.Tk() 
        root.geometry("600x300") # size of windows
        root.resizable(False, False)
        root.title("UTRGV: Networking in Action CSCI: 4345")
        root.iconbitmap(r'logo.ico')
        root.geometry("+500+300") # distance from left and top
        label=tk.Label(root, text = "Select File to transfer")
        button = tk.Button(root, text="Select", command=self.select_file)
        label.grid(row = 1, column = 0)
        button.grid(row = 1, column = 1)
        
        # Server to Connect to 
        self.serverName = 'localhost'
        self.serverPort = 10000
        self.filename=''
        
        ''' Create Client Socket '''
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:   
            self.clientSocket.connect((self.serverName,self.serverPort))
        except:
            print("Unexpected error: Please check the server")
            root.withdraw()
            root.destroy()
            root.quit()
        
        root.mainloop()

        
    def select_file(self):
        # pick file to transfer
        self.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpeg files","*.jpg"),("xml files","*.xml"),("all files","*.*")))
        if(self.filename):
            self.sendfile()
    
    def sendfile(self):
        try:
            print(f"file to send {self.filename}")
            file_size = os.path.getsize(self.filename)
            file_to_send= os.path.basename(self.filename) 
            
            # Send metadata first
            line = file_to_send + ' '
            line += str(file_size)
            line += '\r\n'
            print(f"Metaddata line is:>>>{line}")
            metadata = line.encode()
            self.clientSocket.sendall(metadata)
            
            # Send data
            with open(file_to_send,"rb") as f:
                print(f'starting connection to server with file: {file_to_send}')
                data = f.read()
                self.clientSocket.sendall(data)
        finally:
            print('wait for confirmation from server...')
            text = self.clientSocket.recv(1024)
            print ('From Server: ', text.decode())
            print('closing socket after sendin data...')
            self.clientSocket.close()
    
ClientConnection()

