/* tacoshermanos.com  ·  nav, sticky header, scroll reveal */
(function () {
  'use strict';

  /* ---- mobile nav ---- */
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---- sticky header hairline ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- scroll reveal ---- */
  var items = document.querySelectorAll('.reveal');
  if (!items.length) return;

  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    items.forEach(function (el) { el.classList.add('in'); });
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  items.forEach(function (el) { io.observe(el); });
})();

/* ---- video cards: nothing loads until someone actually asks for it ---- */
(function () {
  'use strict';
  document.querySelectorAll('.video-card[data-video]').forEach(function (card) {
    var btn = card.querySelector('.video-card__play');
    if (!btn) return;
    btn.addEventListener('click', function () {
      if (card.querySelector('video')) return;
      var v = document.createElement('video');
      v.src = card.dataset.video;
      v.playsInline = true;
      v.controls = true;
      v.preload = 'auto';
      card.appendChild(v);
      card.classList.add('is-playing');
      v.play().catch(function () { /* leave the controls for the user */ });
    });
  });
})();
