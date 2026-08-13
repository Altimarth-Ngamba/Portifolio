import streamlit as st

st.set_page_config(layout="wide")

nome = "Altimarth Ngamba"

col1, col2 = st.columns(2)
with col1:
    saudacao = st.subheader(f"Olá, Eu sou {nome}")
    texto_apresentacao = st.write("Sou um estudante de programação e desenvolvedor freelancer."
            " Meu objetivo é criar aplicações web envolventes e visualmente impressionantes, através de código cuidadosamente elaborado e design centrado no usuário.",
            " Estou sempre em busca de novos desafios e oportunidades para aprimorar minhas habilidades e contribuir para projetos inovadores.",
            " Se você está procurando um desenvolvedor apaixonado e dedicado para transformar suas ideias em realidade")

with col2:
    imagem_1 = st.image("assets/img/port.png", width=300)



col3, col4 = st.columns(2)
with col3:
    imagem = st.image("assets/img/port.png", width=500,)

with col4:
    st.title("Sou desenvolvedor profissional de experiência do usuário.")
    st.write("Eu desenvolvo serviços para clientes especializados na criação de websites modernos", 
             " e elegantes, serviços web e lojas online. Minha paixão é desenvolver experiências digitais para o usuário.")

    st.write("Eu desenvolvo serviços para clientes especializados na criação de sites e serviços web modernos e elegantes.")

    col5, col6, col7, col8, = st.columns(4)
    with col5:
        if st.button("Meus Projetos", key="projects_button"):
            st.switch_page("pages/1_Projectos.py")
        
    with col6:
        botao_baixar_cv = st.button("Baixar CV", key="download_cv_button")
        
    with col7:
        botao_contactos = st.button("Contactos")
        if botao_contactos:
                st.switch_page("pages/2_Contacto.py")

    with col8:
        pass
    
    
with st.form("Projectos"):
    st.subheader("Projectos",)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        foto = st.image("assets/img/port.png")
        st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        
    with col2:
        foto = st.image("assets/img/port.png")
        st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
    with col3:
        foto = st.image("assets/img/port.png")
        st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
            
    a1, a2, a3, a4, a5 = st.columns(5)
    with a1:
        pass
    
    with a2:
        pass
        
    with a3:
        if st.form_submit_button("Ver mais Projectos"):
                               
            st.switch_page("pages/1_Projectos.py",)
    
    with a4:
        pass
    
    with a5:
        pass
    


    
with st.form("Outros"):  
    
    col1, col2, col3 = st.columns(3)
        
    with col1:
            foto = st.image("assets/img/port.png")
            st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            
    with col2:
            foto = st.image("assets/img/port.png")
            st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        
    with col3:
            foto = st.image("assets/img/port.png")
            st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      
    a1, a2, a3, a4, a5 = st.columns(5)      
    with a1:
            pass
        
    with a2:
            pass
            
    with a3:
            if st.form_submit_button("Ver mais Projectos"):
                                   
                st.switch_page("pages/1_Projectos.py",)
        
    with a4:
            pass
        
    with a5:
            pass