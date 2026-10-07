(() => {
  const toggle = document.querySelector('.nav-toggle');
  const navigation = document.querySelector('#mobile-nav');
  const setMenuOpen = (open) => {
    if (!toggle || !navigation) return;
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Zavřít navigaci' : 'Otevřít navigaci');
    navigation.hidden = !open;
    document.body.classList.toggle('modal-open', open);
  };
  toggle?.addEventListener('click', () => setMenuOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  navigation?.addEventListener('click', (event) => { if (event.target.closest('a')) setMenuOpen(false); });
  navigation?.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') return;
    const links = [...navigation.querySelectorAll('a')];
    if (!event.shiftKey && event.target === links.at(-1)) { event.preventDefault(); toggle.focus(); }
    if (event.shiftKey && event.target === links[0]) { event.preventDefault(); toggle.focus(); }
  });
  toggle?.addEventListener('keydown', (event) => {
    if (toggle.getAttribute('aria-expanded') !== 'true' || event.key !== 'Tab') return;
    event.preventDefault();
    (event.shiftKey ? navigation.querySelector('a:last-child') : navigation.querySelector('a')).focus();
  });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') { setMenuOpen(false); toggle.focus(); } });
  window.matchMedia('(min-width: 701px)').addEventListener('change', (event) => { if (event.matches) setMenuOpen(false); });
  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const gallery = document.querySelector('.gallery-strip');
  document.querySelectorAll('[data-gallery-step]').forEach((button) => button.addEventListener('click', () => {
    if (gallery) gallery.scrollBy({ left: Number(button.dataset.galleryStep) * Math.min(gallery.clientWidth * .72, 750), behavior: reducedMotion.matches ? 'instant' : 'smooth' });
  }));
  const photos = [...document.querySelectorAll('[data-photo]')];
  const viewer = document.querySelector('.photo-dialog');
  let photoIndex = 0;
  const showPhoto = (index) => {
    if (!viewer || !photos.length) return;
    photoIndex = (index + photos.length) % photos.length;
    const source = photos[photoIndex];
    const image = viewer.querySelector('.viewer-photo');
    image.src = source.dataset.photo;
    image.alt = source.dataset.caption;
    viewer.querySelector('#viewer-caption').textContent = source.dataset.caption;
    viewer.querySelector('.viewer-count').textContent = `${photoIndex + 1} / ${photos.length}`;
  };
  photos.forEach((button, index) => button.addEventListener('click', () => {
    if (!viewer?.showModal) { window.open(button.dataset.photo, '_blank', 'noopener'); return; }
    showPhoto(index); viewer.showModal(); document.body.classList.add('modal-open');
  }));
  document.querySelectorAll('[data-viewer-step]').forEach((button) => button.addEventListener('click', () => showPhoto(photoIndex + Number(button.dataset.viewerStep))));
  viewer?.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') showPhoto(photoIndex + 1);
    if (event.key === 'ArrowLeft') showPhoto(photoIndex - 1);
  });
  const videoDialog = document.querySelector('.video-dialog');
  document.querySelector('[data-video]')?.addEventListener('click', () => {
    if (!videoDialog?.showModal) { window.open('https://www.facebook.com/reel/1451673733369815/', '_blank', 'noopener'); return; }
    const iframe = document.createElement('iframe');
    iframe.src = 'https://www.facebook.com/plugins/video.php?href=' + encodeURIComponent('https://www.facebook.com/reel/1451673733369815/') + '&show_text=false&autoplay=false';
    iframe.title = 'Video čerstvých jarních závitků Restaurace ASIA';
    iframe.allow = 'fullscreen; picture-in-picture'; iframe.allowFullscreen = true;
    videoDialog.querySelector('.video-embed').replaceChildren(iframe);
    videoDialog.showModal(); document.body.classList.add('modal-open');
  });
  document.querySelectorAll('dialog').forEach((dialog) => {
    dialog.querySelector('.dialog-close')?.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
      const rect = dialog.getBoundingClientRect();
      if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('modal-open');
      if (dialog === videoDialog) videoDialog.querySelector('.video-embed').replaceChildren();
    });
  });
})();
