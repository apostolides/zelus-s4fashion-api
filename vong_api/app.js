const createError = require('http-errors');
const express = require('express');
const cookieParser = require('cookie-parser');
const logger = require('morgan');

const dotenv = require('dotenv');
dotenv.config({ path: './.env' });

const { defaultApp } = require('./firebase/firebase')
console.log(`> firebase initialized app: ${defaultApp.name}`);

const indexRouter = require('./routes/index');
const protectedRouter = require('./routes/protected/protected');
const classifierRouter = require('./routes/classifier/classify');

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/', indexRouter);
app.use('/protected', protectedRouter);
app.use('/classifier', classifierRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.send('error');
});

module.exports = app;
