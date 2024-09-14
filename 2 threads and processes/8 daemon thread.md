# Daemon (Background) thread
- It's a thread that has become detached from the parent thread
- Does not prevent the process from terminating
- The entire Python program exits when no alive non-daemon threads are left
- By default new threads are spawned as non-daemon threads
- If the main thread of the process terminate, the process too
  and with it, all it's child threads.

Note:
- If you spawn daemon threads, be careful that they
  will not have negative effects if terminated abruptly.


# GPT

En Python, los threads (hilos) pueden ser de dos tipos: daemon y non-daemon (a veces llamados "normal threads" o simplemente "threads"). La principal diferencia entre estos tipos de threads es cómo afectan la vida útil del programa completo:

- **Daemon Threads**: Son considerados threads de "segundo plano". Estos threads corren en el fondo y no impiden que el programa principal finalice. Una vez que todos los threads no-daemon del programa han terminado, el programa finalizará, cerrando también todos los threads daemon que aún estén ejecutándose, independientemente de si han terminado su tarea o no.

- **Non-Daemon Threads**: Son los threads "principales" del programa. El programa seguirá ejecutándose mientras al menos uno de estos threads siga vivo. Solo cuando el último thread no-daemon haya finalizado, el programa en su conjunto podrá terminar.

### Resumen:
El programa completo de Python finaliza cuando no quedan threads no-daemon vivos. Esto significa que, independientemente de cuantos threads daemon estén corriendo, el programa se cerrará cuando todos los threads no-daemon hayan terminado su ejecución. Los threads daemon no pueden mantener el programa en ejecución por sí solos; están destinados a tareas de fondo que no necesitan impedir que el programa finalice.