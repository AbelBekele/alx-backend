/* eslint-disable no-console */
import { createClient } from 'redis';

const client = createClient();
client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));
