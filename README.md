# party-rank-video-generator
Gera os video de party rank

Usar no Google Colab

Criar Pastas:
```bash
%mkdir videos_party_rank
%mkdir output_party_rank
%mkdir images_party_rank
```

Executar:
```bash
!pip uninstall pillow
!pip install pillow==9.1.0
!pip uninstall moviepy
!pip install moviepy
!python3 /content/party-rank-video-generator/main.py
```

Lembrar de trocar o bitrate do video calculando em:
https://www.citizeninsomniac.com/WMV/WMVBitCalc.html
