const root = document.documentElement;
    const selector = document.querySelector('.languages');
    const buttons = selector.querySelectorAll('button[data-language]');
    const translations = Array.from(document.querySelectorAll('[data-en], [data-en-label]'), element => ({
      element,
      polishText: element.dataset.en ? element.textContent : null,
      polishLabel: element.getAttribute('aria-label')
    }));
    const pageTitle = document.title;
    const pageLinks = [...document.querySelectorAll('a[data-page]')].map(link => [link, link.getAttribute('href')]);
    function setLanguage(language) {
      const english = language === 'en';
      for (const { element, polishText, polishLabel } of translations) {
        if (element.dataset.en) element.textContent = english ? element.dataset.en : polishText;
        if (element.dataset.enLabel) element.setAttribute('aria-label', english ? element.dataset.enLabel : polishLabel);
      }
      root.lang = language;
      document.title = english ? root.dataset.enTitle : pageTitle;
      for (const [link, original] of pageLinks) {
        const parts = original.split('#');
        link.setAttribute('href', parts[0] + (english ? '?lang=en' : '') + (parts[1] ? '#' + parts[1] : ''));
      }
      for (const button of buttons) {
        button.setAttribute('aria-pressed', String(button.dataset.language === language));
      }
    }
    for (const button of buttons) {
      button.addEventListener('click', () => {
        const url = new URL(window.location.href);
        if (button.dataset.language === 'en') url.searchParams.set('lang', 'en');
        else url.searchParams.delete('lang');
        window.history.replaceState(null, '', url);
        setLanguage(button.dataset.language);
      });
    }
    setLanguage(new URLSearchParams(window.location.search).get('lang') === 'en' ? 'en' : 'pl');
    selector.hidden = false;

    function revealLinkedDetails() {
      const target = document.getElementById(window.location.hash.slice(1));
      const detail = target?.closest('details');
      if (detail && !detail.open) {
        detail.open = true;
        target.scrollIntoView();
      }
    }
    window.addEventListener('hashchange', revealLinkedDetails);
    revealLinkedDetails();
