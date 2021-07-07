const net = require('net');

const client = new net.Socket();
const stind = process.openStdin();

client.connect(2708, '127.0.0.1', () => {
  stind.addListener('data', (text) => {
    const message = text.toString().trim();
    client.write(message);
  });
});

client.on('data', (data) => {
  console.log(' ' + data + ' ')
});