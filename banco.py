perguntas = [
    {"enunciado": "Qual é a capital do Brasil?",
     "opcoes": ["São Paulo", "Brasília", "Rio", "Salvador"],
     "correta": 1,
     "categoria": "Geografia",
     "dificuldade": "facil"},

    {"enunciado": "Qual é o maior planeta do sistema solar?",
     "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"],
     "correta": 2,
     "categoria": "Ciência",
     "dificuldade": "facil"},

    {"enunciado": "Quem escreveu Dom Casmurro?",
     "opcoes": ["Machado de Assis", "Clarice Lispector", "Drummond", "Alencar"],
     "correta": 0,
     "categoria": "Literatura",
     "dificuldade": "facil"},

    {"enunciado": "Qual é o oceano mais extenso?",
     "opcoes": ["Atlântico", "Índico", "Pacífico", "Ártico"],
     "correta": 2,
     "categoria": "Geografia",
     "dificuldade": "facil"},

    {"enunciado": "Qual a fórmula da água?",
     "opcoes": ["H2O", "CO2", "O2", "NaCl"],
     "correta": 0,
     "categoria": "Ciência",
     "dificuldade": "facil"},

    {"enunciado": "Quantos continentes existem?",
     "opcoes": ["5", "6", "7", "8"],
     "correta": 2,
     "categoria": "Geografia",
     "dificuldade": "facil"},

    {"enunciado": "Quem pintou a Mona Lisa?",
     "opcoes": ["Van Gogh", "Da Vinci", "Picasso", "Michelangelo"],
     "correta": 1,
     "categoria": "Arte",
     "dificuldade": "facil"},

    {"enunciado": "Qual o maior animal terrestre?",
     "opcoes": ["Elefante", "Leão", "Girafa", "Urso"],
     "correta": 0,
     "categoria": "Ciência",
     "dificuldade": "facil"},

    {"enunciado": "Qual idioma se fala na Argentina?",
     "opcoes": ["Português", "Espanhol", "Inglês", "Francês"],
     "correta": 1,
     "categoria": "Geografia",
     "dificuldade": "facil"},

    {"enunciado": "Quanto é 9 x 7?",
     "opcoes": ["63", "56", "72", "49"],
     "correta": 0,
     "categoria": "Matemática",
     "dificuldade": "facil"}
]
outras = [
    ("Menor país do mundo?", ["Mônaco","Vaticano","Malta","Andorra"],1,"Geografia","medio"),
    ("Maior deserto?", ["Saara","Gobi","Antártida","Atacama"],2,"Geografia","medio"),
    ("Autor de Harry Potter?", ["Rowling","Tolkien","King","Brown"],0,"Literatura","facil"),
    ("100/10?", ["5","10","20","50"],1,"Matemática","facil"),
    ("Estado mais populoso do Brasil?", ["RJ","MG","SP","BA"],2,"Geografia","medio"),
    ("Cor do céu?", ["Verde","Azul","Vermelho","Roxo"],1,"Geral","facil"),
    ("Maior rio?", ["Amazonas","Nilo","Yangtzé","Mississippi"],0,"Geografia","medio"),
    ("Metal do símbolo Fe?", ["Ferro","Flúor","Frâncio","Irídio"],0,"Ciência","facil"),
    ("Capital da Itália?", ["Roma","Milão","Napoli","Turim"],0,"Geografia","facil"),
    ("5^2?", ["10","20","25","15"],2,"Matemática","facil"),
    ("Velocidade da luz é?", ["Rápida","Lenta","Constante","Variável"],2,"Ciência","dificil"),
    ("Brasil fica em?", ["Europa","Ásia","América","África"],2,"Geografia","facil"),
    ("Cor mistura azul+amarelo?", ["Verde","Roxo","Preto","Laranja"],0,"Arte","facil"),
    ("Governo do Brasil?", ["Monarquia","República","Império","Ditadura"],1,"História","facil"),
    ("Órgão maior corpo?", ["Coração","Pele","Pulmão","Fígado"],1,"Ciência","medio"),
    ("Ano tem quantos meses?", ["10","11","12","13"],2,"Geral","facil"),
    ("Planeta mais próximo do Sol?", ["Vênus","Mercúrio","Terra","Marte"],1,"Ciência","medio"),
    ("Capital da Espanha?", ["Madri","Barcelona","Lisboa","Sevilha"],0,"Geografia","facil"),
    ("Autor 'O Pequeno Príncipe'?", ["Exupéry","Machado","Pessoa","Orwell"],0,"Literatura","medio"),
    ("Animal voa?", ["Cavalo","Águia","Tigre","Cobra"],1,"Geral","facil"),
    ("Continente África fica?", ["Sul","Norte","Centro","Global"],1,"Geografia","facil"),
    ("7x6?", ["42","36","48","40"],0,"Matemática","facil"),
    ("Presidente lidera?", ["Monarquia","República","Império","Tribo"],1,"História","facil"),
    ("Qual mar é salgado?", ["Todos","Nenhum","Alguns","Não"],0,"Ciência","facil"),
    ("Maior continente?", ["África","Ásia","Europa","América"],1,"Geografia","medio"),
    ("Animal doméstico comum?", ["Leão","Gato","Urso","Lobo"],1,"Geral","facil"),
    ("10+15?", ["20","25","30","35"],1,"Matemática","facil"),
    ("Planeta com anéis?", ["Terra","Saturno","Marte","Vênus"],1,"Ciência","facil"),
    ("Cor do sangue?", ["Azul","Verde","Vermelho","Preto"],2,"Geral","facil"),
    ("Capital de Portugal?", ["Lisboa","Porto","Faro","Coimbra"],0,"Geografia","facil")
]

for q in outras:
    perguntas.append({
        "enunciado": q[0],
        "opcoes": q[1],
        "correta": q[2],
        "categoria": q[3],
        "dificuldade": q[4]
    })

# pegar categorias únicas
categorias = list({p["categoria"] for p in perguntas})

print("Escolha uma categoria:")
for i, cat in enumerate(categorias):
    print(f"{i+1} - {cat}")

escolha = int(input("Digite o número: ")) - 1
categoria_escolhida = categorias[escolha]

resposta = int(input("Sua resposta: ")) - 1
