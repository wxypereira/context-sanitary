#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

const scriptPath = path.join(__dirname, '..', 'scripts', 'sanitary_purge.py');
const args = process.argv.slice(2);

const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';
const child = spawn(pythonCmd, [scriptPath, ...args], { stdio: 'inherit' });

child.on('exit', (code) => {
  process.exit(code || 0);
});
