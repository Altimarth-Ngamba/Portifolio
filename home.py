import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Altimarth Ngamba | Desenvolvedor Python",
    page_icon="🐍",
    layout="wide"
)


# ============================================================
# CABEÇALHO / HERO
# ============================================================

st.title("Altimarth Ngamba")

st.subheader(
    "Desenvolvedor Python | Backend • Software • Dados"
)

st.write(
    """
    Desenvolvedor Python em formação, com foco em Backend,
    Desenvolvimento de Software e Análise de Dados.

    Meu objetivo é transformar problemas reais em aplicações,
    sistemas e soluções baseadas em dados.
    """
)


# ============================================================
# BOTÕES PRINCIPAIS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "🚀 Meus Projetos",
        use_container_width=True
    ):
        st.switch_page("pages/1_Projectos.py")


with col2:
    if st.button(
        "📄 Baixar CV",
        use_container_width=True
    ):
        st.info("O CV será disponibilizado aqui.")


with col3:
    if st.button(
        "📩 Contacto",
        use_container_width=True
    ):
        st.switch_page("pages/2_Contacto.py")


st.divider()


# ============================================================
# APRESENTAÇÃO
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.header("Sobre mim")

    st.write(
        """
        Sou Altimarth Ngamba, estudante e desenvolvedor em formação,
        interessado em tecnologia e no desenvolvimento de software
        através da programação.

        Python é a principal linguagem que utilizo na minha formação.
        A partir dela, estou construindo conhecimentos em diferentes
        áreas, principalmente Backend, Desenvolvimento de Software,
        aplicações desktop e Análise de Dados.

        Gosto de aprender construindo projetos e procurando transformar
        conhecimentos teóricos em soluções que possam resolver problemas
        reais.
        """
    )


with col2:

    st.image(
        "assets/img/alth.png",
        width=400
    )


st.divider()


# ============================================================
# ÁREAS DE INTERESSE
# ============================================================

st.header("Áreas de interesse")

st.write(
    """
    Estas são as principais áreas em que estou construindo minha
    formação e que pretendo explorar profissionalmente.
    """
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("⚙️ Backend")

    st.write(
        """
        Desenvolvimento da lógica e estrutura por trás das aplicações,
        trabalhando com Python, bases de dados, APIs e sistemas.
        """
    )


with col2:

    st.subheader("💻 Desenvolvimento de Software")

    st.write(
        """
        Criação de aplicações e sistemas para desktop e web,
        procurando desenvolver soluções funcionais e organizadas.
        """
    )


with col3:

    st.subheader("📊 Dados")

    st.write(
        """
        Tratamento, organização e análise de dados utilizando
        ferramentas do ecossistema Python.
        """
    )


st.divider()


# ============================================================
# TECNOLOGIAS
# ============================================================

st.header("Tecnologias")

st.write(
    """
    Tecnologias que fazem parte da minha formação e do caminho
    profissional que estou construindo.
    """
)


# ------------------------------------------------------------
# PYTHON
# ------------------------------------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("🐍 Python")

    st.write(
        """
        Minha principal linguagem de programação, utilizada como
        base para meus estudos e projetos.
        """
    )


# ------------------------------------------------------------
# STREAMLIT
# ------------------------------------------------------------

with col2:

    st.subheader("🎈 Streamlit")

    st.write(
        """
        Desenvolvimento de aplicações interativas utilizando Python,
        especialmente para ferramentas, sistemas e aplicações
        orientadas a dados.
        """
    )


# ------------------------------------------------------------
# PYQT5
# ------------------------------------------------------------

with col3:

    st.subheader("🖥️ PyQt5")

    st.write(
        """
        Desenvolvimento de aplicações desktop com interfaces gráficas
        utilizando Python.
        """
    )


# ------------------------------------------------------------
# PANDAS
# ------------------------------------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("📊 Pandas")

    st.write(
        """
        Tratamento, organização, transformação e análise de dados
        utilizando Python.
        """
    )


# ------------------------------------------------------------
# SQL
# ------------------------------------------------------------

with col2:

    st.subheader("🗄️ SQL")

    st.write(
        """
        Trabalho com bases de dados, consultas, organização e
        manipulação de informações.
        """
    )


# ------------------------------------------------------------
# ETL
# ------------------------------------------------------------

with col3:

    st.subheader("🔄 ETL")

    st.write(
        """
        Processos de extração, transformação e carregamento de
        dados para preparação e utilização das informações.
        """
    )


st.divider()


# ============================================================
# PROJETOS
# ============================================================

st.header("Projetos em destaque")

st.write(
    """
    Alguns projetos que representam a minha evolução e os problemas
    que procuro resolver através da programação.
    """
)


col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# PROJETO 1
# ------------------------------------------------------------

with col1:

    st.image(
        "assets/img/port.png",
        use_container_width=True
    )

    st.subheader("Assistente Virtual")

    st.write(
        """
        Projeto focado na criação de um assistente capaz de
        interagir com o utilizador e executar diferentes tarefas.
        """
    )

    st.caption(
        "Python · Aplicações · Inteligência"
    )


# ------------------------------------------------------------
# PROJETO 2
# ------------------------------------------------------------

with col2:

    st.image(
        "assets/img/port.png",
        use_container_width=True
    )

    st.subheader("Sistema de Gestão Processual")

    st.write(
        """
        Sistema para organização e gestão de processos, permitindo
        registo, pesquisa, alteração de estados e acompanhamento
        das informações.
        """
    )

    st.caption(
        "Python · Streamlit · Gestão de Dados"
    )


# ------------------------------------------------------------
# PROJETO 3
# ------------------------------------------------------------

with col3:

    st.image(
        "assets/img/port.png",
        use_container_width=True
    )

    st.subheader("Assinaturas Eletrónicas")

    st.write(
        """
        Projeto direcionado à autenticação e utilização de
        assinaturas eletrónicas em documentos PDF.
        """
    )

    st.caption(
        "Python · PDF · Segurança"
    )


st.write("")


if st.button(
    "Ver todos os projetos →",
    use_container_width=True
):
    st.switch_page("pages/1_Projectos.py")


st.divider()


# ============================================================
# COMO EU DESENVOLVO
# ============================================================

st.header("Como eu desenvolvo")

st.write(
    """
    Acredito que aprender programação não deve significar apenas
    aprender sintaxe. Procuro utilizar cada conhecimento adquirido
    para construir alguma coisa.
    """
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("01 — Entender")

    st.write(
        """
        Primeiro procuro compreender o problema, os objetivos,
        os dados envolvidos e as necessidades do utilizador.
        """
    )


with col2:

    st.subheader("02 — Construir")

    st.write(
        """
        Divido o problema em partes menores e desenvolvo uma
        solução utilizando as ferramentas mais adequadas.
        """
    )


with col3:

    st.subheader("03 — Melhorar")

    st.write(
        """
        Testo a aplicação, identifico problemas e procuro melhorar
        continuamente o código, a estrutura e o resultado final.
        """
    )


st.divider()


# ============================================================
# OBJETIVO PROFISSIONAL
# ============================================================

st.header("O que estou construindo")

st.write(
    """
    Estou construindo uma formação sólida em Python para poder
    trabalhar profissionalmente com desenvolvimento de software,
    Backend e dados.

    Mais do que acumular tecnologias, o meu objetivo é desenvolver
    a capacidade de analisar problemas, projetar soluções e
    transformar essas soluções em software funcional.
    """
)


# ============================================================
# CONTACTO
# ============================================================

st.header("Vamos conversar?")

st.write(
    """
    Se quiseres conhecer melhor os meus projetos, trocar ideias
    ou conversar sobre uma oportunidade, podes entrar em contacto
    comigo.
    """
)


if st.button(
    "📩 Entrar em contacto",
    use_container_width=True
):
    st.switch_page("pages/2_Contacto.py")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "© 2026 Altimarth Ngamba · Desenvolvedor Python"
)
