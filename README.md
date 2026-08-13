# Portfólio Pessoal

Site de portfólio construído em Streamlit, para apresentar projectos, percurso profissional e formas de contacto.

## Estrutura do projecto

```
portfolio/
├── app.py                  # Ponto de entrada (página Home)
├── pages/
│   ├── 1_Projectos.py      # Página com a lista de projectos
│   └── 2_Contacto.py       # Formulário de contacto
├── services/
│   ├── content_loader.py   # Lê e prepara os dados de data/
│   └── email_service.py    # Envio de mensagens do formulário de contacto
├── data/
│   ├── perfil.yaml         # Dados pessoais / biografia
│   └── projectos.yaml      # Lista de projectos do portfólio
├── assets/
│   ├── css/style.css       # Estilos personalizados
│   └── img/                # Imagens, foto de perfil, etc.
├── requirements.txt
└── README.md
```

## Arquitectura

O projecto segue uma separação em três camadas:

- **Apresentação** (`app.py`, `pages/`): apenas interface Streamlit, sem lógica de negócio.
- **Serviços** (`services/`): lógica pura em Python (carregamento de conteúdo, envio de emails), sem chamadas a `st.*`.
- **Dados** (`data/`): conteúdo do portfólio em YAML, editável sem tocar no código.

## Como correr o projecto

1. Criar e activar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

2. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Correr a aplicação:
   ```bash
   streamlit run app.py
   ```

## Próximos passos

- [ ] Preencher `data/perfil.yaml` com os dados pessoais
- [ ] Preencher `data/projectos.yaml` com a lista de projectos
- [ ] Implementar `services/content_loader.py`
- [ ] Implementar `services/email_service.py`
- [ ] Construir as páginas em `pages/`
- [ ] Estilizar com `assets/css/style.css`
