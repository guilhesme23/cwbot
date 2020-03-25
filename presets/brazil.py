from territory import Territory
from graph.graph import Graph

acre = Territory(1, "acre", color="#FF0A0A")
alagoas = Territory(2, "alagoas", color="#CC0A44")
amapa = Territory(3, "amapa", color="#FF0A0A")
amazonas = Territory(4, "amazonas", color="#FF0A0A")
bahia = Territory(5, "bahia", color="#FF0A0A")
ceara = Territory(6, "ceara", color="#FF0A0A")
df = Territory(7, "df", color="#FF0A0A")
espirito_santo = Territory(8, "espirito_santo", color="#FF0A0A")
goias = Territory(9, "goias", color="#FF0A0A")
maranhao = Territory(10, "maranhao", color="#FF0A0A")
mato_grosso = Territory(11, "mato_grosso", color="#FF0A0A")
mato_grosso_sul = Territory(12, "mato_grosso_sul", color="#FF0A0A")
minas_gerais = Territory(13, "minas_gerais", color="#FF0A0A")
para = Territory(14, "para", color="#FF0A0A")
paraiba = Territory(15, "paraiba", color="#FF0A0A")
parana = Territory(16, "parana", color="#FF0A0A")
pernambuco = Territory(17, "pernambuco", color="#FF0A0A")
piaui = Territory(18, "piaui", color="#FF0A0A")
rio = Territory(19, "rio", color="#FF0A0A")
rio_grande_norte = Territory(20, "rio_grande_norte", color="#FF0A0A")
rio_grande_sul = Territory(21, "rio_grande_sul", color="#FF0A0A")
rondonia = Territory(22, "rondonia", color="#FF0A0A")
roraima = Territory(23, "roraima", color="#FF0A0A")
santa_catarina = Territory(24, "santa_catarina", color="#FF0A0A")
sao_paulo = Territory(25, "sao_paulo", color="#FF0A0A")
sergipe = Territory(26, "sergipe", color="#FF0A0A")
tocantins = Territory(27, "tocantins", color="#FF0A0A")

g = Graph()

g.add_node(acre, [amazonas])
g.add_node(alagoas, [sergipe, pernambuco, bahia])
g.add_node(amapa, [para])
g.add_node(amazonas, [acre, rondonia, mato_grosso, para, roraima])
g.add_node(bahia, [minas_gerais, goias, tocantins, piaui, pernambuco, alagoas, sergipe, espirito_santo])
g.add_node(ceara, [piaui, pernambuco, paraiba, rio_grande_norte])
g.add_node(df, [goias])
g.add_node(espirito_santo, [rio, minas_gerais, bahia])
g.add_node(goias, [minas_gerais, mato_grosso_sul, mato_grosso, tocantins, bahia, df])
g.add_node(maranhao, [tocantins, para, piaui])
g.add_node(mato_grosso, [para, amazonas, rondonia, tocantins, goias, mato_grosso_sul])
g.add_node(mato_grosso_sul, [mato_grosso, goias, minas_gerais, sao_paulo, parana])
g.add_node(minas_gerais, [espirito_santo, rio, sao_paulo, goias, bahia, mato_grosso_sul])
g.add_node(para, [maranhao, tocantins, mato_grosso, amazonas, amapa, roraima])
g.add_node(paraiba, [rio_grande_norte, ceara, pernambuco])
g.add_node(parana, [mato_grosso_sul, sao_paulo, santa_catarina])
g.add_node(pernambuco, [alagoas, bahia, piaui, ceara, paraiba])
g.add_node(piaui, [maranhao, ceara, pernambuco, bahia, tocantins])
g.add_node(rio, [espirito_santo, minas_gerais, sao_paulo])
g.add_node(rio_grande_norte, [ceara, paraiba])
g.add_node(rio_grande_sul, [santa_catarina])
g.add_node(rondonia, [mato_grosso, amazonas, acre])
g.add_node(roraima, [para, amazonas])
g.add_node(santa_catarina, [parana, rio_grande_sul])
g.add_node(sao_paulo, [parana, mato_grosso_sul, minas_gerais, rio])
g.add_node(sergipe, [bahia, alagoas])
g.add_node(tocantins, [goias, mato_grosso, para, maranhao, piaui, bahia])