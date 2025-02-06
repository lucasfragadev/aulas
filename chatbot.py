import sys
import time
import random
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def digitar(texto, cor=Fore.WHITE, delay=0.05):
    """
    Simula a digitação da mensagem, imprimindo caractere por caractere.
    """
    for char in texto:
        sys.stdout.write(cor + char)
        sys.stdout.flush()
        time.sleep(random.uniform(delay * 0.2, delay * 0.3))
    print()  # Pula a linha ao final

def verificar_palavras_chave(pergunta):
    """
    Verifica se a mensagem contém palavras-chave e retorna uma resposta específica.
    São consideradas dois grupos:
      1. Tecnologias e temas gerais (python, sql, js, etc.).
      2. Setores para contato (coordenador, professor, monitor, direção, financeiro, academico, portal).
    """
    respostas_chave = {
        "python": "Python é uma linguagem de programação versátil, muito usada para desenvolvimento web, análise de dados e inteligência artificial.",
        "sql": "SQL é essencial para manipulação e consulta em bancos de dados relacionais, fundamental para data analytics e desenvolvimento de sistemas.",
        "js": "JavaScript é a principal linguagem para desenvolvimento web, permitindo a criação de interfaces interativas e dinâmicas.",
        "django": "Django é um framework Python robusto para desenvolvimento web, facilitando a criação de aplicações seguras e escaláveis.",
        "flask": "Flask é um microframework Python que possibilita o desenvolvimento rápido de aplicações web de forma simples e flexível.",
        "java": "Java é uma linguagem amplamente utilizada, conhecida por sua portabilidade e robustez em aplicações corporativas.",
        "html": "HTML é a linguagem padrão para estruturar páginas na web.",
        "css": "CSS é usado para definir estilos e layouts em páginas web, deixando os sites mais atraentes visualmente.",
        "ganhar em dolar": "Trabalhar com tecnologia ou serviços online é uma excelente estratégia para ganhar em dólar, aproveitando a globalização dos mercados.",
        "trabalhar para gringa": "Muitos profissionais buscam oportunidades internacionais; isso geralmente exige fluência em inglês e atualização constante em tecnologias atuais.",
        "falar ingles": "Falar inglês é fundamental para acessar melhores oportunidades no mercado de trabalho, especialmente em empresas multinacionais."
    }
    
    contatos = {
        "coordenador": ("Para assuntos relacionados à coordenação, entre em contato com o coordenador pelo e-mail "
                         "coordenacao@infinityschool.com ou pelo telefone 0800-141-7000. A equipe de coordenação é essencial "
                         "para orientar questões acadêmicas e pedagógicas."),
        "professor": ("Se você tiver dúvidas sobre aulas, conteúdos ou suporte pedagógico, entre em contato com os professores pelo "
                      "e-mail professores@infinityschool.com ou ligue para 0800-141-7000. Eles estão sempre prontos para ajudar."),
        "monitor": ("Para suporte relacionado às atividades monitoradas, entre em contato com o monitor da sua turma pelo "
                    "e-mail monitor@infinityschool.com ou pelo telefone 0800-141-7000. Eles auxiliam no esclarecimento de dúvidas "
                    "e no acompanhamento do seu progresso."),
        "direção": ("Caso sua dúvida envolva a direção da escola, entre em contato com o setor de direção pelo e-mail "
                    "direcao@infinityschool.com ou pelo telefone 0800-141-7000. O setor de direção é responsável por decisões "
                    "estratégicas e pelo suporte institucional."),
        "financeiro": ("Para questões financeiras, como mensalidades, pagamentos ou dúvidas sobre bolsas, entre em contato com o "
                       "setor financeiro pelo e-mail financeiro@infinityschool.com ou telefone 0800-141-7000. Eles podem te ajudar "
                       "a encontrar a melhor solução para sua situação."),
        "academico": ("Para assuntos acadêmicos, como matrículas, desempenho e informações sobre cursos, entre em contato com o "
                      "setor acadêmico pelo e-mail academico@infinityschool.com ou pelo telefone 0800-141-7000. Eles são fundamentais "
                      "para garantir que sua experiência educacional seja a melhor possível."),
        "portal": ("Se você precisar de suporte para acessar o Portal do Aluno, entre em contato com o suporte pelo e-mail "
                   "suporteportal@infinityschool.com. Manter o acesso ao portal é importante para acompanhar seu desempenho e acessar "
                   "conteúdos exclusivos.")
    }
    
    # Primeiro, verifica se alguma palavra-chave de tecnologia/temas gerais está na mensagem.
    for chave, resposta in respostas_chave.items():
        if chave in pergunta:
            return resposta
    
    # Em seguida, verifica se alguma palavra relacionada aos contatos está presente.
    for chave, contato in contatos.items():
        if chave in pergunta:
            return contato
    
    return None

def iniciar_conversa():
    respostas_basicas = {
        "oi": "Olá! Como posso te ajudar?",
        "olá": "Oi! Tudo bem?",
        "qual seu nome?": "Eu sou o Infinitão, seu assistente virtual!",
        "como você está?": "Eu sou um chatbot, então estou sempre bem!",
        "o que você faz?": "Eu respondo perguntas simples e também posso te ajudar com informações sobre a Infinity School.",
        "tchau": "Até mais! Se precisar, estou por aqui."
    }

    digitar("\nInfinitão: Olá! Digite 'sair' para encerrar a conversa.", Fore.CYAN)
    while True:
        pergunta = input(Fore.YELLOW + "Você: ").strip().lower()
        if pergunta == "sair":
            digitar("Infinitão: Até logo!", Fore.CYAN)
            break

        # Verifica se há alguma palavra-chave e direciona para a resposta específica.
        resposta_kw = verificar_palavras_chave(pergunta)
        if resposta_kw:
            digitar(f"Infinitão: {resposta_kw}", Fore.CYAN)
            continue

        # Se não houver palavra-chave, verifica se há uma resposta básica.
        resposta = respostas_basicas.get(pergunta, "Desculpe, não entendi. Pode reformular?")
        digitar(f"Infinitão: {resposta}", Fore.CYAN)

def faq():
    faqs = {
        "O que é a Infinity School?":
            "A Infinity School é uma escola 100% presencial com metodologia americana, voltada para capacitar profissionais nas áreas de inovação e criatividade. "
            "Oferece cursos práticos e completos para atender às demandas do mercado atual.",
        "Quais cursos a Infinity School oferece?":
            "A escola oferece diversos cursos, como Programação Full Stack IA, Marketing Digital IA, Design Full Stack IA, Film Design, Fotografia Design, "
            "Data Science e Kids, entre outros, sempre com uma abordagem prática e atualizada.",
        "Qual é a metodologia da Infinity School?":
            "A metodologia é 100% presencial e prática, inspirada no modelo americano, permitindo experiências reais e dinâmicas de aprendizado.",
        "Quais são os diferenciais da Infinity School?":
            "Entre os diferenciais, destacam-se parcerias com Adobe, Microsoft e Google, aulas de reforço, módulos avançados, reserva de estúdio, "
            "gamificação, computadores individuais, cursos moduláveis, certificado internacional e aulas de reposição presencial.",
        "Como posso me inscrever?":
            "Você pode se inscrever diretamente pelo site clicando em 'Faça sua inscrição' ou entrando em contato pelo telefone 0800-141-7000 via WhatsApp.",
        "Onde estão localizadas as unidades?":
            "A Infinity School possui unidades em diversas cidades, incluindo Salvador, Fortaleza, Belo Horizonte, Recife e São Paulo. "
            "Confira os endereços completos no site oficial.",
        "Como funciona o Infinity App e o Portal do aluno?":
            "Através do Infinity App e do Portal do aluno, você pode acompanhar seu desempenho, acessar conteúdos exclusivos e interagir com a comunidade, "
            "tornando a experiência de aprendizado ainda mais integrada.",
        "Quais workshops a escola oferece?":
            "A escola organiza workshops presenciais e gratuitos, abordando temas atuais e relevantes das áreas de inovação, criatividade e tecnologia."
    }

    while True:
        digitar("\n===== FAQ - Perguntas Frequentes =====", Fore.GREEN)
        for i, pergunta in enumerate(faqs, 1):
            digitar(f"{i}. {pergunta}", Fore.GREEN)
        digitar(f"{len(faqs)+1}. Voltar ao menu principal", Fore.GREEN)
        
        escolha = input(Fore.YELLOW + "Selecione o número da pergunta que deseja saber: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(faqs):
                pergunta = list(faqs.keys())[escolha-1]
                resposta = faqs[pergunta]
                digitar(f"\nPergunta: {pergunta}", Fore.MAGENTA)
                digitar(f"Resposta: {resposta}\n", Fore.MAGENTA)
            elif escolha == len(faqs) + 1:
                break
            else:
                digitar("Opção inválida! Tente novamente.", Fore.RED)
        else:
            digitar("Opção inválida! Tente novamente.", Fore.RED)

def sobre_infinity():
    info = (
        "A Infinity School é uma instituição de ensino inovadora, com cursos 100% presenciais e uma metodologia americana "
        "voltada para o desenvolvimento de habilidades nas áreas de tecnologia, marketing, design, filmagem, fotografia e muito mais. "
        "Além dos cursos, a escola oferece uma série de diferenciais que facilitam o aprendizado, como aulas de reforço, parcerias com grandes marcas "
        "(Adobe, Microsoft e Google), computadores individuais, e até mesmo a possibilidade de reservar estúdios para projetos pessoais ou comerciais.\n\n"
        "Para mais informações, visite o site oficial ou entre em contato pelo telefone 0800-141-7000."
    )
    digitar("\nInfinity School:", Fore.CYAN)
    digitar(info, Fore.CYAN)

def chatbot():
    while True:
        digitar("\n===== MENU PRINCIPAL =====", Fore.BLUE)
        digitar("1. Iniciar conversa", Fore.BLUE)
        digitar("2. FAQ - Perguntas Frequentes sobre a Infinity School", Fore.BLUE)
        digitar("3. Sobre a Infinity School", Fore.BLUE)
        digitar("4. Sair", Fore.BLUE)
        
        escolha = input(Fore.YELLOW + "Escolha uma opção: ").strip()

        if escolha == "1":
            iniciar_conversa()
        elif escolha == "2":
            faq()
        elif escolha == "3":
            sobre_infinity()
        elif escolha == "4":
            digitar("\nInfinitão: Obrigado por conversar conosco. Até a próxima!", Fore.CYAN)
            break
        else:
            digitar("Opção inválida! Por favor, escolha uma opção do menu.", Fore.RED)

# Iniciar o chatbot
chatbot()