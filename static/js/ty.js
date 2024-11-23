    // Dynamically load external confetti script
const script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js";
document.head.appendChild(script);

script.onload = () => {
    // Trigger confetti animation once the script has loaded
    const duration = 3 * 1000; // Confetti animation duration
    const animationEnd = Date.now() + duration;
    const colors = ['#bb0000', '#ffffff', '#7700bb', '#ff44ff', '#44ffdd', '#ff8844'];

    (function frame() {
        confetti({
            particleCount: 3,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: colors
        });
        confetti({
            particleCount: 3,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: colors
        });

        if (Date.now() < animationEnd) {
            requestAnimationFrame(frame);
        }
    })();
};