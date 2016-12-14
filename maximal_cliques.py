#!/usr/bin/python
# coding: utf-8

from bronker_bosch2 import bronker_bosch2
from data import *
from reporter import Reporter
from time import time


TAM = len(NEIGHBORS) - 1

def writeFile(fTime):
	archivo = open("datos.txt", "r+")
	contenido = archivo.read()
	final_de_archivo = archivo.tell()	 
	archivo.write(fTime+" "+str(TAM)+"\n")
	archivo.seek(final_de_archivo)
	archivo.close()
 
 
if __name__ == '__main__':
    funcs = [bronker_bosch2]

    for func in funcs:
        report = Reporter('## %s' % func.func_doc)
        init_time = time()
        func([], set(NODES), set(), report)
        final_time = time()
        e_time = final_time - init_time
        str_time = str("%.20f" % e_time)
        writeFile(str_time)
        report.print_report()
