from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


# -----------------------------
# DADOS DA FLORESTA
# -----------------------------

arvores = 100
biodiversidade = 100
agua = 100
solo = 100


# -----------------------------
# PÁGINA INICIAL
# -----------------------------

@app.route("/")
def inicio():
    return render_template("inicio.html")

def animais_da_floresta(arvores):

    animais = []

    if arvores >= 20:
        animais.append("🐒")

    if arvores >= 40:
        animais.append("🦜")

    if arvores >= 60:
        animais.append("🦥")

    if arvores >= 80:
        animais.append("🐆")

    if arvores >= 90:
        animais.append("🐍")

    return animais

# -----------------------------
# PÁGINA DO DESMATAMENTO
# -----------------------------

@app.route("/desmatamento")
def desmatamento():

    if arvores >= 75:
        mensagem = "🌳 A floresta está saudável!"

    elif arvores >= 50:
        mensagem = "⚠️ A floresta está começando a sofrer impactos."

    elif arvores >= 25:
        mensagem = "🚨 Grande parte da floresta foi perdida!"

    else:
        mensagem = "🛑 A floresta está severamente degradada!"


    animais = animais_da_floresta(arvores)


    return render_template(
        "desmatamento.html",

        arvores=arvores,
        biodiversidade=biodiversidade,
        agua=agua,
        solo=solo,
        mensagem=mensagem,
        animais=animais
    )
 
@app.route("/curiosidades")
def curiosidades():

    curiosidades = [
        {
            "titulo": "🌳 As florestas são essenciais",
            "texto": "As florestas fornecem habitat para muitas espécies e participam de processos importantes dos ecossistemas."
        },

        {
            "titulo": "🐾 Animais dependem das florestas",
            "texto": "Quando uma floresta é destruída, muitos animais podem perder seus locais de alimentação, abrigo e reprodução."
        },

        {
            "titulo": "💧 Florestas e água",
            "texto": "A vegetação participa do ciclo da água e ajuda na proteção do solo e dos recursos hídricos."
        },

        {
            "titulo": "🌱 Reflorestamento",
            "texto": "A recuperação de áreas degradadas pode ajudar a restaurar habitats e funções importantes dos ecossistemas."
        },

        {
            "titulo": "🌎 Florestas e clima",
            "texto": "As florestas armazenam carbono e fazem parte do sistema climático do planeta."
        },

        {
            "titulo": "🦥 Perda de habitat",
            "texto": "A fragmentação e a perda de habitats podem dificultar a sobrevivência de diversas espécies."
        }
    ]

    return render_template(
        "curiosidades.html",
        curiosidades=curiosidades
    )

@app.route("/ecoia", methods=["GET", "POST"])
def ecoia():

    resposta = ""

    if request.method == "POST":

        pergunta = request.form["pergunta"].lower()


        if "o que é desmatamento" in pergunta or "que é desmatamento" in pergunta:

            resposta = (
                "O desmatamento é a remoção ou destruição da vegetação "
                "de uma área de floresta. Ele pode acontecer por motivos "
                "como agricultura, pecuária, exploração de madeira e "
                "construção de áreas urbanas."
            )


        elif "por que" in pergunta and "desmatamento" in pergunta:

            resposta = (
                "O desmatamento pode causar perda de habitats, redução "
                "da biodiversidade, degradação do solo e alterações no "
                "ciclo da água e no clima."
            )


        elif "animal" in pergunta or "animais" in pergunta:

            resposta = (
                "O desmatamento pode destruir ou fragmentar os habitats "
                "dos animais. Com menos espaço e recursos, algumas "
                "espécies podem ter mais dificuldade para sobreviver."
            )


        elif "água" in pergunta:

            resposta = (
                "As florestas participam do ciclo da água e ajudam a "
                "proteger o solo e os recursos hídricos. A remoção da "
                "vegetação pode prejudicar esses processos."
            )


        elif "reflorestamento" in pergunta or "reflorestar" in pergunta:

            resposta = (
                "Reflorestamento é o processo de recuperar áreas onde "
                "a vegetação foi perdida. Ele pode ajudar na recuperação "
                "de habitats, do solo e de funções importantes dos "
                "ecossistemas."
            )


        elif "combater" in pergunta or "evitar" in pergunta:

            resposta = (
                "Podemos combater o desmatamento protegendo florestas, "
                "combatendo atividades ilegais, utilizando áreas já "
                "desmatadas de forma responsável e apoiando projetos "
                "de conservação e recuperação ambiental."
            )


        elif "importante" in pergunta and "floresta" in pergunta:

            resposta = (
                "As florestas são importantes porque abrigam grande "
                "diversidade de espécies, participam do ciclo da água, "
                "protegem o solo e armazenam carbono."
            )


        else:

            resposta = (
                "🤔 Ainda não sei responder essa pergunta. "
                "Tente perguntar sobre desmatamento, animais, água, "
                "florestas ou reflorestamento."
            )


    return render_template(
        "ecoia.html",
        resposta=resposta
    )

# -----------------------------
# DERRUBAR UMA ÁRVORE
# -----------------------------

@app.route("/derrubar")
def derrubar():

    global arvores
    global biodiversidade
    global agua
    global solo

    if arvores > 0:

        arvores -= 1

        biodiversidade = max(0, biodiversidade - 1)

        agua = max(0, agua - 1)

        solo = max(0, solo - 1)


    return redirect(url_for("desmatamento"))


# -----------------------------
# REPLANTAR UMA ÁRVORE
# -----------------------------

@app.route("/replantar")
def replantar():

    global arvores
    global biodiversidade
    global agua
    global solo

    if arvores < 100:

        arvores += 1

        biodiversidade = min(100, biodiversidade + 1)

        agua = min(100, agua + 1)

        solo = min(100, solo + 1)


    return redirect(url_for("desmatamento"))


# -----------------------------
# SERVIDOR
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)
