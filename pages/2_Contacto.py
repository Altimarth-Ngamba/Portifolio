import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Contacto | Altimarth Ngamba",
    page_icon="📩",
    layout="wide"
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("📩 Contacto")

st.subheader(
    "Vamos conversar sobre uma ideia, projeto ou oportunidade?"
)

st.write(
    """
    Se quiseres conhecer melhor o meu trabalho, discutir um projeto,
    trocar ideias sobre tecnologia ou falar sobre uma oportunidade
    profissional, podes entrar em contacto comigo.
    """
)


st.divider()


# ============================================================
# INFORMAÇÕES DE CONTACTO
# ============================================================

st.header("Encontra-me")

col1, col2 = st.columns(2)


with col1:

    st.subheader("📧 Email")

    email = st.write(
        "altimarthngamba1@gmail.com"
    )


with col2:

    st.subheader("💻 GitHub")

    st.write(
        "https://github.com/Altimarth-Ngamba"
    )


st.divider()


# ============================================================
# REDES / PERFIS
# ============================================================

st.header("Perfis profissionais")

st.write(
    """
    Estes são os espaços onde pretendo apresentar o meu trabalho,
    projetos e evolução profissional.
    """
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("GitHub")

    st.write(
        "Projetos, código e experiências de desenvolvimento."
    )

    st.link_button(
        "🐙 Visitar GitHub",
        "https://github.com/Altimarth-Ngamba"
    )


with col2:

    st.subheader("LinkedIn")

    st.write(
        "Experiência profissional, formação e carreira."
    )

    st.link_button(
        "💼 Visitar LinkedIn",
        "https://www.linkedin.com/in/altimarth-ngamba"
    )


with col3:

    st.subheader("WhatsApp")
    
    st.write("Entrar em contacto via whatsApp")
    
    st.link_button(
            "Visitar WhatsApp",
            "https://wa.link/182zme"
        )

st.divider()


# ============================================================
# FORMULÁRIO
# ============================================================

st.header("Envie uma mensagem")

st.write(
    """
    Preenche o formulário abaixo. O formulário serve para recolher
    as informações necessárias para entrar em contacto contigo.
    """
)


with st.form("formulario_contacto"):

    nome = st.text_input(
        "Nome",
        placeholder="Digite o seu nome"
    )

    email = st.text_input(
        "Email",
        placeholder="Digite o seu email"
    )

    assunto = st.selectbox(
        "Assunto",
        [
            "Projeto",
            "Oportunidade profissional",
            "Colaboração",
            "Dúvida",
            "Outro"
        ]
    )

    mensagem = st.text_area(
        "Mensagem",
        placeholder="Escreva a sua mensagem...",
        height=180
    )

    enviar = st.form_submit_button(
        "Enviar mensagem",
        use_container_width=True
    )


# ============================================================
# PROCESSAMENTO DO FORMULÁRIO
# ============================================================

if enviar:

    if not nome:
        st.warning(
            "Por favor, informe o seu nome."
        )

    elif not email:
        st.warning(
            "Por favor, informe o seu email."
        )

    elif not mensagem:
        st.warning(
            "Por favor, escreva uma mensagem."
        )

    else:

        st.success(
            "Mensagem preenchida com sucesso!"
        )

        st.write(
            f"""
            **Nome:** {nome}

            **Email:** {email}

            **Assunto:** {assunto}

            **Mensagem:** {mensagem}
            """
        )

        st.info(
            """
            O envio real da mensagem ainda precisa ser configurado.
            """
        )


st.divider()


# ============================================================
# DISPONIBILIDADE
# ============================================================

st.header("Sobre oportunidades")

st.write(
    """
    Tenho interesse em oportunidades relacionadas com desenvolvimento
    de software, Python, Backend, aplicações, dados e áreas relacionadas
    com tecnologia.

    Também estou aberto a projetos que me permitam aplicar os meus
    conhecimentos, aprender novas tecnologias e desenvolver soluções
    para problemas reais.
    """
)


st.divider()


# ============================================================
# VOLTAR PARA HOME
# ============================================================

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
    "© 2026 Altimarth Ngamba · Contacto"
)