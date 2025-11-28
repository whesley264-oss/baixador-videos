import os
import yt_dlp

def baixar_video(link, pasta_destino):
    opcoes = {
        'format': 'best',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([link])

def main():
    pasta_videos = '/storage/emulated/0/Videos'

    # 1. Verifica e cria a pasta se não existir
    if not os.path.exists(pasta_videos):
        os.makedirs(pasta_videos)
        print(f"Pasta criada em: {pasta_videos}")
    
    # 2. Interface de usuário
    print("--- Baixador de Vídeos ---")
    print("Escolha a plataforma:")
    print("1. YouTube")
    print("2. TikTok")
    print("3. Instagram")
    print("4. Kwai")
    
    plataforma = input("Digite o número da opção desejada: ")
    
    link_video = input("Cole o link do vídeo aqui: ")
    
    # 3. Baixa o vídeo
    try:
        baixar_video(link_video, pasta_videos)
        print("\nDownload concluído com sucesso!")
        print(f"Vídeo salvo em: {pasta_videos}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
