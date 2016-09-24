from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import NameForm

#def archive (request)
def inicio(request):	
	return render(request, 'inicio.html')

#def grafo(request):
#	return render(request, 'grafo.html')
# Create your views here.
graph={"nodes":[], "edges":[]}

def findNodeId(nodeLabel):
	nodes = graph["nodes"]
	for n in nodes:
		if n["label"]==nodeLabel:
			return n["id"]
	return -1

def index(request):
	return render(request, "index.html", {})

def grafo(request):
    a = "hola"
    form = NameForm()
    return render(request, "grafo.html", {"formulario":form})


def mygraph(request):
	file = open("data.txt")
	print file

	

	node_id=1
	edge_id=1
	for line in file:
		line= line.replace("\n", "")
		values= line.split(",")
		 #INCIO DEL FILTRO PARA BUSCAR POR NOMBRE 
		 		
		 #FIN DEL FILTRO PARA BUSCAR POR NOMBRE

		fromLabel= values[0]
		toLabel= values[2]
		from_id=findNodeId(fromLabel)
		if toLabel==" Colombia" or toLabel=="France": #ESTE HACE EL FILTRO POR PAIS
		#if fromLabel== "Shakira" or fromLabel=="Pique" : # ESTE HACE EL FILTRO POR NOMBRE
			if from_id==-1:
				nodes= graph["nodes"]
				nodes.append({"id": node_id, "label": fromLabel})
				from_id=node_id
				node_id=node_id + 1
			
			to_id=findNodeId(toLabel)
			if to_id==-1:
				nodes= graph["nodes"]
				nodes.append({"id": node_id, "label": toLabel})
				to_id=node_id
				node_id=node_id + 1


			e= {"from": from_id, "to":to_id, "label": values[1]}
			graph["edges"].append(e)
			edge_id=edge_id+1


	return JsonResponse(graph)