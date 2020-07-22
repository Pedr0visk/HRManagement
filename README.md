# Sistema de gerenciamento de recursos humanos (SaaS)

- Multi-Tenant
    - Software vendido como serviço
    - Multiplas empresas utilizam a plataforma

- Multi-Database
    - A aplicação se comunica com mais de um banco ao mesmo tempo
    - Comunicação com aplicações legadas
        - Comunicação com bancos de dados existentes
        - Criação de Models do Django para mapear tabelas de bancos de dados de outros sistemas

- Multi-Idioma
- Multi-Location
    - Moedas
    - Formato de dadas
    - Fuso-horarios

- Celery para tarefas assíncronas
    - Geração de relatórios
        - PDF
        - Excel
        - CSV
    - Uso de HTTP Stream para geração de relatórios em tempo real

## Modelos

- Departamentos
- Empregados
- Usuários
- Documentos
- Empresas
- Registro de Hora Extra

## Tecnologias empregadas

### ----- RF (Requisitos Funcionais)

### ----- RNF (Requisitos não Funcionais)

### ----- RN (Regras de Negócio)


# Snippets

> pmm - python manage.py makemigrations
> pm - python manage.py migrate
> prs - python manage.py runserver
