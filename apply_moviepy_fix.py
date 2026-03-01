# coding: utf-8
"""
Script para aplicar os patches do MoviePy (fix/VideoClip.py e fix/CompositeVideoClip.py)
no pacote moviepy instalado. Funciona em Windows e Linux.
"""
import os
import shutil
import sys
from pathlib import Path


def get_project_root() -> Path:
    """Raiz do projeto (pasta que contém fix/ e apply_moviepy_fix.py)."""
    return Path(__file__).resolve().parent


def get_moviepy_path() -> Path:
    """Caminho da pasta do pacote moviepy instalado."""
    try:
        import moviepy
        return Path(moviepy.__path__[0]).resolve()
    except ImportError:
        print("Erro: moviepy não está instalado. Instale com: pip install -r requirements.txt")
        sys.exit(1)


def apply_fix() -> bool:
    root = get_project_root()
    fix_dir = root / "fix"
    video_clip_src = fix_dir / "VideoClip.py"
    composite_src = fix_dir / "CompositeVideoClip.py"

    if not video_clip_src.is_file():
        print(f"Erro: não encontrado {video_clip_src}")
        return False
    if not composite_src.is_file():
        print(f"Erro: não encontrado {composite_src}")
        return False

    moviepy_base = get_moviepy_path()
    video_dir = moviepy_base / "video"
    compositing_dir = video_dir / "compositing"
    video_clip_dst = video_dir / "VideoClip.py"
    composite_dst = compositing_dir / "CompositeVideoClip.py"

    if not video_dir.is_dir():
        print(f"Erro: pasta do moviepy não encontrada: {video_dir}")
        return False
    if not compositing_dir.is_dir():
        print(f"Erro: pasta compositing não encontrada: {compositing_dir}")
        return False

    try:
        shutil.copy2(video_clip_src, video_clip_dst)
        print(f"OK: {video_clip_src.name} -> {video_clip_dst}")
        shutil.copy2(composite_src, composite_dst)
        print(f"OK: {composite_src.name} -> {composite_dst}")
        return True
    except OSError as e:
        print(f"Erro ao copiar arquivos: {e}")
        if os.name == "nt":
            print("Dica no Windows: execute o terminal como Administrador ou feche programas que usem o moviepy.")
        return False


def main():
    print("Aplicando correções do MoviePy (fix/ -> site-packages/moviepy)...")
    if apply_fix():
        print("Concluído. As alterações do fix/ foram aplicadas ao moviepy instalado.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
