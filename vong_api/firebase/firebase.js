const admin = require("firebase-admin");
const serviceAccount = require("./key.json");

const defaultApp = admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://vong-370923-default-rtdb.europe-west1.firebasedatabase.app"
});

module.exports = {admin:admin, serviceAccount:serviceAccount, defaultApp:defaultApp}