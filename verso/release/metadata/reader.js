/* Reveal checked statements reached by a definition link or saved bookmark. */
(() => {
  function revealStatement() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); }
    catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    let opened = false;
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === "DETAILS" && !parent.open) {
        parent.open = true;
        opened = true;
      }
    }
    if (opened) requestAnimationFrame(() => target.scrollIntoView());
  }
  document.addEventListener("DOMContentLoaded", revealStatement);
  window.addEventListener("hashchange", revealStatement);
  // Wide original equations keep their mathematical layout. Make their
  // horizontal scroll region reachable by keyboard as well as touch.
  function markScrollableMath() {
    for (const formula of document.querySelectorAll('main .math.display')) {
      if (formula.scrollWidth > formula.clientWidth + 1) {
        formula.setAttribute('tabindex', '0');
        formula.setAttribute('role', 'region');
        formula.setAttribute('aria-label', 'Scrollable mathematical formula');
      } else {
        formula.removeAttribute('tabindex');
        formula.removeAttribute('role');
        formula.removeAttribute('aria-label');
      }
    }
  }
  window.addEventListener('load', markScrollableMath);
  window.addEventListener('resize', markScrollableMath);
})();
