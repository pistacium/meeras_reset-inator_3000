# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['meeras_reset-inator_3000.py'],
             pathex=['C:\\Users\\pistacium\\Documents\\SRC Stuff\\meeras_reset-inator_3000v1.1'],
             binaries=[],
             datas=[('macrosettings.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='meeras_reset-inator_3000',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='kitty.ico')
