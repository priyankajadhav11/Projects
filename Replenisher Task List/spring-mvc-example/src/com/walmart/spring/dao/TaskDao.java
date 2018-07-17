package com.walmart.spring.dao;

import java.util.List;

import com.walmart.spring.model.Login;
import com.walmart.spring.model.Task;

public interface TaskDao {
	  void addTask(Task task);
	  List<Task> getTask(Login login);
}
