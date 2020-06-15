M = 30 #Malta
L = 45 #Levadura

def phenotype (chromosome):
	return chromosome[0] * 4 + chromosome[1] * 7 + chromosome[2] * 3

def fitness (chromosome): # priorize ordered genes
    malta = chromosome[0] * 2 + chromosome[1] * 1 + chromosome[2] * 2
    levadura = chromosome[0] * 1 + chromosome[1] * 2 + chromosome[2] * 2
    if (malta > M) or (levadura > L): # No se puede pasar de ese limite.
        return 0
    beneficio = chromosome[0] * 4 + chromosome[1] * 7 + chromosome[2] * 3
    return beneficio

# El número meximo que puede haber es 22 rubias, de las otras como mucho habría 15.

parameters = { 'alphabet':list(range(23)), 'type':'classic', 'chromsize':3, 'target': 160 } # Target ponemos 160 porque es el máximo posible con estos recursos.