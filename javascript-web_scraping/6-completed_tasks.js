#!/usr/bin/node
// Retreives count of SW appearances for char id 18

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const tasksComp = {};
    for (const task of tasks) {
      if (task.completed) {
        const userID = task.userId;
        tasksComp[userID] = (tasksComp[userID] + 1 || 1);
      }
    }
    console.log(tasksComp);
  }
});
