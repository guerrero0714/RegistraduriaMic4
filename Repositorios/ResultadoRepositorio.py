from Repositorios.InterfazRepositorio import InterfazRepositorio
from Modelos.Resultados import Resultado
from bson import ObjectId

class ResultadoRepositorio(InterfazRepositorio[Resultado]):
    #da las votaciones por Mesa
    def getListadoCandidatosInscritos(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    #da las votaciones por candidato
    def getListadoMesaCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    #Numero mayor de una cedula
    def getNumeroCedulaMayorCandidato(self):
        query = {
            "$group":{
                "_id": "$candidato",
                "max":{
                    "$max":"$cedula"
                },
                "doc":{
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
