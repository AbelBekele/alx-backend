/* eslint-disable */
const redis = require('redis');
const client = redis.createClient();

client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const sub_channel = 'holberton school channel'
client.subscribe(sub_channel);
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(sub_channel);
    client.quit();
  }
})
