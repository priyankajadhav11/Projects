package com.walmart.spring.model;
import java.sql.*;
public class Task {
	public String taskName;
	public String notes;
	public String feedback;
	public String status;
	public String assignedto;
	public String assignedby;
	public int taskId;
	public String priority;
	public Timestamp createdTime;
	public Timestamp endTime;
	public Timestamp getCreatedTime() {
		return createdTime;
	}
	public void setCreatedTime(Timestamp createdTime) {
		this.createdTime = createdTime;
	}
	public Timestamp getEndTime() {
		return endTime;
	}
	public void setEndTime(Timestamp endTime) {
		this.endTime = endTime;
	}
	public Timestamp getEstimatedTime() {
		return null;
	}
	public int estHours;
	
	public int getEstHours() {
		return estHours;
	}
	public void setEstHours(int estHours) {
		this.estHours = estHours;
	}
	public String getPriority() {
		return priority;
	}
	public void setPriority(String priority) {
		this.priority = priority;
	}
	public String getTaskName() {
		return taskName;
	}
	public void setTaskName(String taskName) {
		this.taskName = taskName;
	}
	public String getNotes() {
		return notes;
	}
	public void setNotes(String notes) {
		this.notes = notes;
	}
	public String getFeedback() {
		return feedback;
	}
	public void setFeedback(String feedback) {
		this.feedback = feedback;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	public String getAssignedto() {
		return assignedto;
	}
	public void setAssignedto(String assignedto) {
		this.assignedto = assignedto;
	}
	public String getAssignedby() {
		return assignedby;
	}
	public void setAssignedby(String assignedby) {
		this.assignedby = assignedby;
	}
	public int getTaskId() {
		return taskId;
	}
	public void setTaskId(int taskId) {
		this.taskId = taskId;
	}
}
