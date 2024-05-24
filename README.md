# Llm
## paso 1 DESCARGARLO
descargar
curl -fsSL https://ollama.com/install.sh | sh

### paso 2 abrir el server
ollama serve

### Ejecutarlo en bash
ollama pull tinyllama

### Para preguntar
ollama run tinyllama ....

### Modo Chat/Detener chat

ollama run tinyllama
detener: ctrl+D

### Los token
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Por qué el cielo es azul?",
  "stream": false
}'