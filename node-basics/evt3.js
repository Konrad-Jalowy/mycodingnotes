const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('zdarzenie', (data) => {
    console.log('Otrzymano dane:', data);
});

emitter.emit('zdarzenie', 'Hello, World!');