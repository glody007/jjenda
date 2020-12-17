require('dotenv').config();
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use(express.static('dist'));

const port = process.env.UI_SERVER_PORT || 8000;

const apiProxyTarget = process.env.API_PROXY_TARGET;
if (apiProxyTarget) {
  app.use('/', createProxyMiddleware({ target: apiProxyTarget }));
}

app.listen(port, () => {
  console.log(`UI started on port ${port}`);
});
