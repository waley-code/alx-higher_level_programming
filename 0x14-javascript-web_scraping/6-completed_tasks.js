#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasksByUser = {};
  tasks.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      if (completedTasksByUser[userId]) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  });
  console.log(completedTasksByUser);
});
