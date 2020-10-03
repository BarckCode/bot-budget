# !/bin/bash
# Description: Check Status App
# Autor: Barckcode

# Start App
python3 main.py &
sleep 5s

# Look for the application process
PID=$(ps -v | grep python3 | egrep -v grep | awk '{print $1}')

# Check if it keeps running
if [[ $PID -gt 0 ]]
then
    echo "El proceso de la app ha levantado con PID: $PID"
    echo "El proceso morirá en 10s. Prueba la app desde Telegram"
    sleep 5s
    echo "El proceso morirá en 5s..."
    sleep 5s
    echo "Se va a matar la app con PID: $PID"
    pkill python3
    echo "*************************************"
    echo "Status Test OK"
    echo "*************************************"
else
    echo "*************************************"
    echo "La app no ha levantado correctamente."
    ps -v | grep python3 | egrep -v grep
    echo $?
    echo "*************************************"
    sleep 5s
    pkill python3
fi
