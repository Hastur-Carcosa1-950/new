<!DOCTYPE html>
<html lang="pt-br">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>projeto_final_:3</title>

    <link rel="stylesheet"
          href="{{ url_for('static', filename='estilo.css') }}">

</head>


<body>

    <header>

        <h1>🌳 projeto_final_:3</h1>

        <nav>

            <a href="/">Início</a>

            <a href="/desmatamento">Desmatamento</a>

            <a href="/curiosidades">Curiosidades</a>

            <a href="/ecoia">EcoIA</a>

        </nav>

    </header>


    <main>

        <section class="hero">

            <h2>
                O que acontece quando uma floresta desaparece?
            </h2>

            <p>
                Descubra os impactos do desmatamento
                através de experiências interativas.
            </p>

            <a href="/desmatamento" class="botao">
                Começar experiência 🌱
            </a>

        </section>


        <section class="informacao">

            <h2>Por que isso importa?</h2>

            <p>
                As florestas são importantes para a biodiversidade,
                para o solo, para a água e para o equilíbrio dos
                ecossistemas.
            </p>

        </section>

    </main>


    <footer>

        <p>
            projeto_final_:3 — Projeto de conscientização ambiental
        </p>

    </footer>

</body>

</html>
