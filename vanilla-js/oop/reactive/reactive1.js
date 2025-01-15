// Reactive System
function reactive(target) {
    const listeners = new Map(); // Mapa przechowująca efekty dla poszczególnych kluczy
  
    const notify = (key) => {
      const effects = listeners.get(key);
      if (effects) {
        effects.forEach(effect => effect());
      }
    };
  
    const track = (key, effect) => {
      if (!listeners.has(key)) {
        listeners.set(key, new Set());
      }
      listeners.get(key).add(effect);
    };
  
    return new Proxy(target, {
      get(target, key) {
        // Automatyczne śledzenie zależności, jeśli w trakcie wywoływana jest funkcja efektu
        if (currentEffect) {
          track(key, currentEffect);
        }
        return target[key];
      },
      set(target, key, value) {
        target[key] = value; // Zaktualizuj wartość
        notify(key); // Powiadom efekty
        return true;
      }
    });
  }
  
  // Przechowuje bieżący efekt (dla trackowania)
  let currentEffect = null;
  
  // Funkcja do rejestrowania efektów
  function effect(callback) {
    currentEffect = callback;
    callback(); // Wywołaj efekt natychmiast, aby zainicjalizować stan
    currentEffect = null;
  }

  
  const state = reactive({ message: 'Hello, World!' });

    // Aktualizuj widok, gdy zmienia się stan
    effect(() => {
      document.getElementById('output').textContent = state.message;
    });

    // Obsługa wiązania dwukierunkowego
    const input = document.getElementById('message');
    input.value = state.message;
    input.addEventListener('input', (e) => {
      state.message = e.target.value; // Aktualizuj stan na podstawie wpisanego tekstu
    });