const { admin } = require('../firebase/firebase');

async function checkAuth(req, res, next) {
    if(!req.headers.authorization){
      return res.status(403).json({message:'Missing authorization headers.'});
    }
    
    if(!req.headers.authorization.startsWith("Bearer ")){
      return res.status(403).json({message:'Incorrect authorization schema.'});
    }
  
    let token = req.headers.authorization.substring(7, req.headers.authorization.length);
  
    if(!token){
      return res.status(403).json({message:'Missing authorization token.'});
    }
  
    try{
      let decodedToken = await admin.auth().verifyIdToken(token);
      res.locals.decodedToken = decodedToken;
      next();
    }
    catch(err){
      return res.status(403).json({message:'Unauthorized'});
    }
}

module.exports = {checkAuth:checkAuth}