package com.walmart.spring.controller;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.walmart.spring.dao.TaskDaoImpl;
import com.walmart.spring.model.Login;
import com.walmart.spring.model.Task;

@Controller
public class TaskController {
	@Autowired
	  public TaskDaoImpl taskService;
	  @RequestMapping(value = "/task", method = RequestMethod.GET)
	  public ModelAndView showTask(HttpServletRequest request, HttpServletResponse response) {
	    ModelAndView mav = new ModelAndView("task");
	    mav.addObject("task", new Task());
	    return mav;
	  }
	  @RequestMapping(value = "/taskProcess", method = RequestMethod.POST)
	  public ModelAndView addTask(HttpServletRequest request, HttpServletResponse response,
	  @ModelAttribute("task") Task task,@ModelAttribute("login") Login login) {
		  ModelAndView mav = null;
	  taskService.addTask(task);
	  List<Task> tasks=taskService.getTask(login);
	  mav=new ModelAndView("welcome");
	  mav.addObject("tasklist", tasks);
	  return mav;
	  }
}
