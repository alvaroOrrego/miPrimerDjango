let tl = gsap.timeline({ repeat: 0, yoyo: false });
tl.from('#logo', {
    duration: 1,
    rotate: 360
});

tl.from('.text-center', {
    duration: 0.5,
    scale: 0,
    stagger: 0,
});
