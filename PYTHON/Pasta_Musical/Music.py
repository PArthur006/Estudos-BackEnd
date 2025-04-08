print('''[1] Eletrônica
[2] MPB
[3] HipHop
[4] Sertanejo''')
while True:
    usu = int(input('Qual deseja ouvir? '))
    while usu <= 0 or usu > 4:
        usu = int(input('Pasta não encontrada. Tente outra vez: '))
    if usu == 1:
        print('''Músicas
Faded
Happier
Together
Wake me Up''')
        mus = str(input('Escolha a música: ')).upper().strip()
        while mus != 'FADED' or 'HAPPIER' or 'TOGETHER' or 'WAKE ME UP':
            mus = str(input('Essa música não está no catálogo. Tente novamente: ')).upper().strip()
        if mus == 'FADED':
            import pygame
            print('Música: Faded')
            pygame.init()
            pygame.mixer.music.load('Faded.mp3')
            pygame.mixer.music.play()
            import time
            time.sleep(120)