const express = require('express');
const router = express.Router();
const { checkAuth } = require('../../security/checkAuth');

router.use(checkAuth);

router.post('/classify', function(req, res, next) {
    if(!req.body.url){
        return res.status(400).json({message:'bad request.'});
    }
  
    return res.json({message:'classification results'});
});

module.exports = router;
