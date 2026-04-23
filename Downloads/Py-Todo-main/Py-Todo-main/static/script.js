// Theme toggle, clock, and AJAX handlers for Smart To-Do Manager Pro
document.addEventListener('DOMContentLoaded', () => {
  // Theme
  const root = document.documentElement;
  const stored = localStorage.getItem('theme');
  if (stored) root.setAttribute('data-theme', stored);
  const toggle = document.getElementById('theme-toggle');
  if (toggle) toggle.addEventListener('click', () => {
    const cur = root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    const next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    toggle.textContent = next === 'dark' ? '🌙' : '☀️';
  });

  // Clock
  const clock = document.getElementById('clock');
  function updateClock(){
    const now = new Date();
    const opts = {weekday:'short', month:'short', day:'numeric'};
    const date = now.toLocaleDateString(undefined, opts);
    const time = now.toLocaleTimeString(undefined, {hour:'2-digit', minute:'2-digit'});
    if(clock) clock.textContent = `${date} • ${time}`;
  }
  updateClock(); setInterval(updateClock, 1000);

  // AJAX helpers for done/delete so we can animate
  function ajaxPost(url, data){
    return fetch(url, {method:'POST', headers:{'X-Requested-With':'XMLHttpRequest'}, body:data});
  }

  // handle done buttons
  document.body.addEventListener('click', async (e)=>{
    const doneBtn = e.target.closest('.done-btn');
    if(doneBtn){
      const id = doneBtn.dataset.id;
      const r = await ajaxPost(`/done/${id}`, null);
      if(r.ok){
        const card = document.querySelector(`.task-card[data-id='${id}']`);
        if(card){ card.classList.add('done'); }
      }
    }
    const delBtn = e.target.closest('.del-btn');
    if(delBtn){
      const id = delBtn.dataset.id;
      const card = document.querySelector(`.task-card[data-id='${id}']`);
      if(card){
        card.classList.add('del-anim');
        setTimeout(async ()=>{
          const r = await ajaxPost(`/delete/${id}`, null);
          if(r.ok){ card.remove(); } else { card.classList.remove('del-anim'); }
        }, 300);
      }
    }
  });

  // smooth add: when add form submits, let server render new page; keep progressive enhancement minimal
  const addForm = document.getElementById('addForm');
  if(addForm){
    addForm.addEventListener('submit', ()=>{
      // small visual feedback
      const btn = addForm.querySelector('button[type=submit]');
      if(btn){ btn.disabled = true; btn.textContent = 'Adding…'; }
    });
  }

  // --- Reminders & Notifications ---
  function requestNotificationPermission(){
    if('Notification' in window && Notification.permission === 'default'){
      Notification.requestPermission();
    }
  }

  function showNotification(title, body){
    if('Notification' in window && Notification.permission === 'granted'){
      try{ new Notification(title, { body }); }catch(e){}
    }
  }
  // Play a short notification tone using WebAudio
  function playTone(){
    try{
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const o = ctx.createOscillator();
      const g = ctx.createGain();
      o.type = 'sine';
      o.frequency.value = 880; // A5 tone
      g.gain.setValueAtTime(0, ctx.currentTime);
      g.gain.linearRampToValueAtTime(0.12, ctx.currentTime + 0.01);
      g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
      o.connect(g); g.connect(ctx.destination);
      o.start();
      setTimeout(()=>{ try{ o.stop(); ctx.close(); }catch(e){} }, 700);
    }catch(e){
      // fallback: short beep via audio tag not available
      console.warn('Audio not available', e);
    }
  }

  // Centered modal popup
  function showModal(title, message){
    // overlay
    const overlay = document.createElement('div');
    overlay.className = 'reminder-overlay';
    // modal
    const modal = document.createElement('div');
    modal.className = 'reminder-modal';
    const h = document.createElement('div'); h.className='title'; h.textContent = title;
    const b = document.createElement('div'); b.className='body'; b.textContent = message;
    const actions = document.createElement('div'); actions.className='actions';
    const ok = document.createElement('button'); ok.className='btn'; ok.textContent='OK';
    ok.addEventListener('click', ()=>{ overlay.classList.remove('show'); modal.classList.remove('show'); setTimeout(()=>{ overlay.remove(); modal.remove(); },300); });
    actions.appendChild(ok);
    modal.appendChild(h); modal.appendChild(b); modal.appendChild(actions);
    document.body.appendChild(overlay); document.body.appendChild(modal);
    // animate in
    requestAnimationFrame(()=>{ overlay.classList.add('show'); modal.classList.add('show'); });
    playTone();
    // auto-dismiss after 6 seconds
    setTimeout(()=>{ try{ overlay.classList.remove('show'); modal.classList.remove('show'); setTimeout(()=>{ overlay.remove(); modal.remove(); },300);}catch(e){} }, 6000);
  }

  function parseDueString(s){
    if(!s) return null;
    // expect 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD '
    const trimmed = s.trim();
    if(!trimmed) return null;
    const iso = trimmed.replace(' ', 'T'); // make ISO-like
    const d = new Date(iso);
    if(isNaN(d)) return null;
    return d;
  }

  function checkReminders(){
    const cards = document.querySelectorAll('.task-card');
    const now = new Date();
    cards.forEach(card =>{
      const id = card.dataset.id;
      if(!id) return;
      if(card.classList.contains('done')) return; // ignore done
      const dueStr = card.dataset.due;
      const due = parseDueString(dueStr);
      if(!due) return;
      // If now past due and not alerted before
      const alertedKey = `alerted:${id}`;
      const alerted = localStorage.getItem(alertedKey);
      if(now >= due && !alerted){
        const title = 'Task Reminder';
        const body = `${card.querySelector('.title')?.textContent || 'Task'} is due now.`;
        showModal(title, body);
        showNotification(title, body);
        localStorage.setItem(alertedKey, new Date().toISOString());
      }
    });
  }

  // request permission and start periodic check
  requestNotificationPermission();
  // check every 30 seconds
  setInterval(checkReminders, 30000);
  // also run once on load
  setTimeout(checkReminders, 1500);
});
