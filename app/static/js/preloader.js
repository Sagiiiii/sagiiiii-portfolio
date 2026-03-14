(function() {
    const preloader = document.getElementById('preloader');

    if (sessionStorage.getItem('visited')) {
        preloader.remove();
        return;
    }

    sessionStorage.setItem('visited', 'true');

    const startTime  = Date.now();
    const barFill    = document.getElementById('barFill');
    const statusText = document.getElementById('preloaderText');

    const messages = [
        'Iniciando...',
        'Cargando proyectos...',
        'Preparando portfolio...',
        'Casi listo...',
        '¡Bienvenido! 🦊',
    ];

    let progress = 0;
    let msgIndex = 0;

    const interval = setInterval(() => {
        const step = progress < 70 ? 2 : progress < 90 ? 1 : 0.5;
        progress = Math.min(progress + step, 99);
        barFill.style.width = progress + '%';

        const newIndex = Math.floor((progress / 100) * messages.length);
        if (newIndex !== msgIndex && newIndex < messages.length) {
            msgIndex = newIndex;
            statusText.style.opacity = '0';
            setTimeout(() => {
                statusText.textContent = messages[msgIndex];
                statusText.style.opacity = '1';
            }, 200);
        }
    }, 30);

    window.addEventListener('load', () => {
        clearInterval(interval);
        barFill.style.width = '100%';
        statusText.textContent = '¡Bienvenido! 🦊';

        const elapsed   = Date.now() - startTime;
        const remaining = Math.max(0, 3000 - elapsed);

        setTimeout(() => {
            preloader.classList.add('hidden');
            setTimeout(() => preloader.remove(), 700);
        }, remaining);
    });
})();