import streamlit as st


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Projetos | Altimarth Ngamba",
    page_icon="🚀",
    layout="wide"
)


# ============================================================
# TÍTULO DA PÁGINA
# ============================================================

st.title("🚀 Meus Projetos")

st.subheader(
    "Projetos que transformam conhecimento em aplicações reais."
)

st.write(
    """
    Esta página reúne projetos que desenvolvi ou estou a desenvolver
    durante a minha formação em Python, Desenvolvimento de Software
    e Dados.

    Mais do que apresentar apenas o resultado final, procuro mostrar
    os problemas que cada projeto pretende resolver, as tecnologias
    utilizadas e aquilo que aprendi durante o desenvolvimento.
    """
)


st.divider()


# ============================================================
# FILTROS
# ============================================================

st.subheader("Explorar projetos")

filtro = st.selectbox(
    "Filtrar por área",
    [
        "Todos",
        "Python",
        "Backend",
        "Software",
        "Dados",
        "Desktop",
        "PDF"
    ]
)


st.divider()


# ============================================================
# PROJETO 1
# ============================================================

if filtro in ["Todos", "Python", "Backend", "Software"]:

    st.header("01 — Assistente Virtual")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Assistente Virtual")

        st.write(
            """
            Um projeto voltado para a criação de um assistente
            capaz de interagir com o utilizador e executar diferentes
            tarefas.

            A ideia é explorar como Python pode ser utilizado para
            criar uma aplicação capaz de receber comandos, processar
            informações e responder de acordo com o contexto.
            """
        )

        st.write("**Área:** Desenvolvimento de Software")

        st.write("**Tecnologias:**")

        st.code(
            "Python",
            language="text"
        )

        st.write("**Objetivos do projeto:**")

        st.markdown(
            """
            - Criar uma interface de interação com o utilizador
            - Processar comandos
            - Organizar diferentes funcionalidades
            - Trabalhar com funções e estruturas de dados
            - Evoluir o projeto conforme novos conhecimentos
            """
        )


    st.divider()


# ============================================================
# PROJETO 2
# ============================================================

if filtro in ["Todos", "Python", "Backend", "Software"]:

    st.header("02 — Sistema de Gestão Processual")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Sistema de Gestão Processual")

        st.write(
            """
            Aplicação desenvolvida para organizar e gerir informações
            relacionadas a processos.

            O sistema pretende permitir o registo, consulta, pesquisa,
            alteração de estados e organização dos processos, além da
            geração de informações úteis para acompanhamento e análise.
            """
        )

        st.write("**Área:** Desenvolvimento de Software")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "Streamlit\n"
            "SQL",
            language="text"
        )

        st.write("**Funcionalidades previstas:**")

        st.markdown(
            """
            - Autenticação de utilizadores
            - Registo de processos
            - Pesquisa de processos
            - Alteração do estado dos processos
            - Organização por número e data
            - Estatísticas
            - Relatórios
            - Mapas de processos
            """
        )


    st.divider()


# ============================================================
# PROJETO 3
# ============================================================

if filtro in ["Todos", "Python", "Software", "PDF"]:

    st.header("03 — Sistema de Assinaturas Eletrónicas")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Assinaturas Eletrónicas em PDF")

        st.write(
            """
            Projeto direcionado para o trabalho com documentos PDF,
            com foco na autenticação e utilização de assinaturas
            eletrónicas.

            O objetivo é explorar como aplicações Python podem ser
            utilizadas para trabalhar com documentos digitais e
            processos de assinatura.
            """
        )

        st.write("**Área:** Desenvolvimento de Software")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "PDF",
            language="text"
        )

        st.write("**Objetivos:**")

        st.markdown(
            """
            - Trabalhar com documentos PDF
            - Criar processos de assinatura
            - Validar informações dos documentos
            - Estudar mecanismos de autenticação
            - Explorar segurança aplicada a documentos digitais
            """
        )


    st.divider()


# ============================================================
# PROJETO 4
# ============================================================

if filtro in ["Todos", "Python", "Dados"]:

    st.header("04 — Sistema de Comparação de Dados")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Comparador")

        st.write(
            """
            Projeto destinado à comparação de informações para
            identificar diferenças, correspondências e alterações
            entre conjuntos de dados.

            A proposta é desenvolver uma ferramenta capaz de facilitar
            a análise de grandes quantidades de informação.
            """
        )

        st.write("**Área:** Dados / Desenvolvimento de Software")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "Pandas\n"
            "Streamlit",
            language="text"
        )

        st.write("**Objetivos:**")

        st.markdown(
            """
            - Importar dados
            - Comparar informações
            - Identificar diferenças
            - Filtrar resultados
            - Apresentar os resultados de forma clara
            """
        )


    st.divider()


# ============================================================
# PROJETO 5
# ============================================================

if filtro in ["Todos", "Python", "Dados"]:

    st.header("05 — Análise de Dados")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Projeto de Análise de Dados")

        st.write(
            """
            Projeto destinado à exploração do processo de análise
            de dados utilizando Python.

            O objetivo é trabalhar desde a preparação dos dados até
            à produção de informações que possam ajudar na tomada
            de decisões.
            """
        )

        st.write("**Área:** Análise de Dados")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "Pandas\n"
            "SQL",
            language="text"
        )

        st.write("**Etapas:**")

        st.markdown(
            """
            - Recolha dos dados
            - Limpeza
            - Tratamento
            - Transformação
            - Análise
            - Consultas SQL
            - Apresentação dos resultados
            """
        )


    st.divider()


# ============================================================
# PROJETO 6
# ============================================================

if filtro in ["Todos", "Python", "Software", "Desktop"]:

    st.header("06 — Aplicação Desktop")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Aplicação Desktop com Python")

        st.write(
            """
            Projeto destinado ao desenvolvimento de aplicações
            desktop utilizando Python e interfaces gráficas.

            O objetivo é explorar a criação de software para
            computadores utilizando uma interface gráfica completa.
            """
        )

        st.write("**Área:** Desenvolvimento de Software")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "PyQt5",
            language="text"
        )

        st.write("**Objetivos:**")

        st.markdown(
            """
            - Criar interfaces gráficas
            - Trabalhar com eventos
            - Criar formulários
            - Organizar diferentes telas
            - Trabalhar com bases de dados
            - Desenvolver aplicações desktop completas
            """
        )


    st.divider()


# ============================================================
# PROJETO 7 — ETL
# ============================================================

if filtro in ["Todos", "Python", "Dados"]:

    st.header("07 — Pipeline de Dados / ETL")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "assets/img/port.png",
            use_container_width=True
        )

    with col2:

        st.subheader("Processamento de Dados — ETL")

        st.write(
            """
            Projeto focado no processo de Extração, Transformação
            e Carregamento de dados.

            A proposta é construir um fluxo capaz de receber dados
            de uma fonte, processá-los e disponibilizar os dados
            transformados para utilização posterior.
            """
        )

        st.write("**Área:** Dados / ETL")

        st.write("**Tecnologias:**")

        st.code(
            "Python\n"
            "Pandas\n"
            "SQL",
            language="text"
        )

        st.write("**Etapas:**")

        st.markdown(
            """
            - Extract — Extração dos dados
            - Transform — Limpeza e transformação
            - Load — Carregamento dos dados
            - Validação dos resultados
            """
        )


    st.divider()


# ============================================================
# TECNOLOGIAS
# ============================================================

st.header("Tecnologias utilizadas")

st.write(
    "Principais tecnologias presentes nos projetos deste portfólio."
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("Python")

    st.write(
        """
        Linguagem principal utilizada nos projetos.
        """
    )


with col2:

    st.subheader("Streamlit")

    st.write(
        """
        Utilizado na criação de aplicações e interfaces interativas.
        """
    )


with col3:

    st.subheader("PyQt5")

    st.write(
        """
        Utilizado para desenvolvimento de aplicações desktop.
        """
    )


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("Pandas")

    st.write(
        """
        Utilizado para tratamento, transformação e análise de dados.
        """
    )


with col2:

    st.subheader("SQL")

    st.write(
        """
        Utilizado para trabalhar com bases de dados e consultas.
        """
    )


with col3:

    st.subheader("ETL")

    st.write(
        """
        Utilizado para estruturar processos de extração,
        transformação e carregamento de dados.
        """
    )


st.divider()


# ============================================================
# ESTADO ATUAL
# ============================================================

st.header("Em desenvolvimento")

st.write(
    """
    O portfólio está em constante evolução. Alguns projetos estão
    em desenvolvimento e serão atualizados à medida que novas
    funcionalidades forem implementadas.
    """
)

st.info(
    "Novos projetos e versões serão adicionados regularmente."
)


# ============================================================
# CONTACTO
# ============================================================

st.header("Gostaste de algum projeto?")

st.write(
    """
    Se quiseres conhecer melhor algum dos projetos ou conversar
    sobre desenvolvimento de software, podes entrar em contacto.
    """
)


if st.button(
    "📩 Entrar em contacto",
    use_container_width=True
):
    st.switch_page("pages/2_Contacto.py")


# ============================================================
# VOLTAR PARA HOME
# ============================================================

st.write("")

if st.button(
    "← Voltar para a página inicial",
    use_container_width=True
):
    st.switch_page("app.py")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "© 2026 Altimarth Ngamba · Projetos"
)