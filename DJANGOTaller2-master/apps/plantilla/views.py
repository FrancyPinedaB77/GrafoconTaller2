from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import os
#HACIENDO UN SUBPROCESO
archivo_cluster=os.system ("scp cluster_bigdata:lasalida/cluster* /home/estudiante/GrafoconTaller2/DJANGOTaller2-master")
print archivo_cluster
#TERMINANDO EL SUBPROCESO



#def archive (request)
def inicio(request):
    return render(request, 'inicio.html')

def findNodeId(nodeLabel,graph):
    #graph = {"nodes": [], "edges": []}
    nodes = graph["nodes"]
    for n in nodes:
        if n["label"]==nodeLabel:
            return n["id"]
    return -1

def index(request):
    return render(request, "index.html", {})

def grafo(request):

    return render(request, "grafo.html")

def mygraph(request):
    graph = {"nodes": [], "edges": []}
    file = open("data.txt")
    a=request.GET['country']
    b=request.GET['name']
    f_inicio=request.GET['fecha_inicio']
    f_fin=request.GET['fecha_fin']
    node_id=1
    edge_id=1
    for line in file:
        line= line.replace("\n", "")
        line2=line.replace("|","/")
        values= line2.split(",")
         #INCIO DEL FILTRO PARA BUSCAR POR NOMBRE
         #FIN DEL FILTRO PARA BUSCAR POR NOMBRE
        fromLabel= values[0]
        toLabel= values[2]
        fecha=values[1]
        from_id=findNodeId(fromLabel, graph)
        if (fromLabel==b or toLabel==a and (f_inicio <= fecha <= f_fin)): #ESTE HACE EL FILTRO POR PAIS
        #if fromLabel== "Shakira" : # ESTE HACE EL FILTRO POR NOMBRE
            if from_id==-1:
                nodes= graph["nodes"]
                nodes.append({"id": node_id, "label": fromLabel})
                from_id=node_id
                node_id=node_id + 1

            to_id=findNodeId(toLabel, graph)
            if to_id==-1:
                nodes= graph["nodes"]
                nodes.append({"id": node_id, "label": toLabel})
                to_id=node_id
                node_id=node_id + 1


            e= {"from": from_id, "to":to_id, "label": values[1]}
            graph["edges"].append(e)
            edge_id=edge_id+1
    return JsonResponse(graph)
