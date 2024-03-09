import flet as ft

def main(pagina): #criar função principal
    texto = ft.Text("Bem Vindo Ao Chat")
    
    chat = ft.Column()
    
    def enviarMensagemTunel(mensagem):
        print(mensagem)
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()
        
    pagina.pubsub.subscribe(enviarMensagemTunel)
    
    def enviar_mensagem(evento):
        print("enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {CampoMensagem.value}")
        CampoMensagem.value = " "
        pagina.update()
      
    CampoMensagem = ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click = enviar_mensagem)
    linha_enviar = ft.Row([CampoMensagem,botao_enviar])
    
    def entrar_chat(evento):
        print("Entrar no Chat")
        #fechar popup
        popup.open = False
        #tirar o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(chat)
        pagina
        texto_entrada = ft.Text(f"{nome_usuario.value} Entrou no chat")
        chat.controls.append(texto_entrada)
        pagina.add(linha_enviar)
        pagina.update()
        
    titulo_popup = ft.Text("Bem Vindo ao Chat")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click = abrir_popup)   #(oque vai estar escrito,funçao)
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main,view=ft.WEB_BROWSER) #criar o app chamando a função principal