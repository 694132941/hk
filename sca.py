#!/usr/bin/python
#coding=UTF-8
#
import optparse
import socket

def connScan(tgtHost,tgtPort):
    try:
	connSkt = socket.socket(socket.AF_INEF,socket.SOCKET_STREAM)
	connSkt.connect((tgtHost,tgtPort))
	connSkt.send('ViolentPython\r\n')
	results = connSkt.recv(100)
	print('[+]%d/tcp open' % tgtPort)
	print('[+]' + str(results))
	connSkt.close()
    except:
	print('[-]%d/tcp closed' % tgtPort)
def portScan(tgtHost, tgtPorts):
    try:
	tgtIP = socket.gethostbyname(tgtHost)
    except:
	print "[-] Cannot resolve '%s': Unknown host" %tgtHost
	return
    try:
	tgtName = socket.gethostbyaddr(tgtIP)
	 
