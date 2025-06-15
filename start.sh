#!/bin/bash

# Sanal ortam varsa aktif et
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
fi

# Uygulamayı başlat
python3 app.py
