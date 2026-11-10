const toggle = document.querySelector('.header__toggle');
const nav = document.querySelector('#navegacao');
function closeMenu() { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
toggle?.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
nav?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.querySelector('.contact__form')?.addEventListener('submit', event => {
 event.preventDefault(); const form = event.currentTarget; if (!form.reportValidity()) return;
 const values = new FormData(form); const message = `Olá! Meu nome é ${values.get('nome')}.\nE-mail: ${values.get('email')}\nTelefone: ${values.get('telefone')}\nServiço: ${values.get('servico')}\nAssunto: ${values.get('assunto')}\n\n${values.get('mensagem')}`;
 const target = `https://wa.me/5511960392977?text=${encodeURIComponent(message)}`;
 const status = form.querySelector('[role="status"]'); status.replaceChildren();
 const a = document.createElement('a'); a.href = target; a.textContent = 'Abrir WhatsApp para revisar e enviar'; a.className = 'text-link'; status.append('Mensagem preparada. ', a); a.focus();
});
