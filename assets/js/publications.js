(function () {
  'use strict';

  var toggles = Array.prototype.slice.call(document.querySelectorAll('[data-bibtex-toggle]'));
  if (!toggles.length) return;

  function close(toggle) {
    var panel = document.getElementById(toggle.getAttribute('aria-controls'));
    toggle.setAttribute('aria-expanded', 'false');
    if (panel) panel.hidden = true;
  }

  function closeAll(except) {
    toggles.forEach(function (toggle) {
      if (toggle !== except) close(toggle);
    });
  }

  toggles.forEach(function (toggle) {
    toggle.addEventListener('click', function () {
      var scrollLeft = window.pageXOffset;
      var scrollTop = window.pageYOffset;
      var panel = document.getElementById(toggle.getAttribute('aria-controls'));
      if (!panel) return;
      var willOpen = toggle.getAttribute('aria-expanded') !== 'true';
      closeAll(toggle);
      toggle.setAttribute('aria-expanded', String(willOpen));
      panel.hidden = !willOpen;

      // Expanding a panel changes the grid height. Preserve the viewport so the
      // sticky profile column does not appear to jump beside the publication.
      window.requestAnimationFrame(function () {
        window.scrollTo(scrollLeft, scrollTop);
        window.requestAnimationFrame(function () {
          window.scrollTo(scrollLeft, scrollTop);
        });
      });
    });
  });

  document.querySelectorAll('[data-bibtex-copy]').forEach(function (button) {
    button.addEventListener('click', function () {
      var panel = button.closest('[data-bibtex-panel]');
      var code = panel && panel.querySelector('code');
      if (!code) return;
      var text = code.textContent;
      var label = button.querySelector('[data-copy-label]');

      function showCopied() {
        if (label) label.textContent = '已复制';
        window.setTimeout(function () {
          if (label) label.textContent = '复制';
        }, 1600);
      }

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(showCopied);
        return;
      }

      var textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.setAttribute('readonly', '');
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      try {
        document.execCommand('copy');
        showCopied();
      } finally {
        document.body.removeChild(textarea);
      }
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeAll();
  });
}());
