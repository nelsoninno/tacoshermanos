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

/* ---- deep links: land on the right card, fully visible ---------------- */
(function () {
  'use strict';
  function jumpToHash() {
    if (!location.hash) return;
    var el;
    try { el = document.querySelector(location.hash); } catch (e) { return; }
    if (!el) return;
    // Arriving at a specific card means the scroll-reveal above it is irrelevant,
    // and leaving it unresolved both hides the target and shifts the layout.
    document.querySelectorAll('.reveal').forEach(function (n) { n.classList.add('in'); });
    // Instant, never smooth: a smooth scroll from another page animates for a
    // second or more, so anyone who touches the wheel on arrival fights it.
    try { el.scrollIntoView({ block: 'start', behavior: 'instant' }); }
    catch (e) { el.scrollIntoView(true); }
  }
  // run after images and fonts have settled, so the position is final
  if (document.readyState === 'complete') setTimeout(jumpToHash, 50);
  else window.addEventListener('load', function () { setTimeout(jumpToHash, 50); });
  window.addEventListener('hashchange', jumpToHash);
})();
