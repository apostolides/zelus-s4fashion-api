const express = require('express');
const router = express.Router();
const { checkAuth } = require('../../security/checkAuth');

router.use(checkAuth);

router.get('/', function(req, res, next) {
  res.send(res.locals.decodedToken);
});

module.exports = router;
