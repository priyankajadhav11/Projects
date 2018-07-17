package com.walmart.spring.dao;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import com.walmart.spring.model.Login;
import com.walmart.spring.model.Task;

public class TaskDaoImpl implements TaskDao {

	@Autowired
	DataSource datasource;
	@Autowired
	JdbcTemplate jdbcTemplate;

	public void addTask(Task task) {
		Timestamp timestamp = new Timestamp(System.currentTimeMillis());
		String sql = "insert into task values(?,?,?,?,?,?,?,?,?,?,?)";
		jdbcTemplate.update(sql,
				new Object[] { task.getTaskName(), task.getNotes(), task.getFeedback(), "Started", task.getAssignedto(),
						task.getAssignedby(), task.getTaskId(), task.getPriority(), timestamp, null,
						task.getEstHours() });
	}

	@Override
	public List<Task> getTask(Login login) {
		String sql = "select * from task where assignedto='" + login.getUsername() + "'";
		List<Task> tasks = new ArrayList<Task>();

		List<Map<String, Object>> rows = jdbcTemplate.queryForList(sql);
		for (Map row : rows) {
			Task task = new Task();
			task.setTaskName((String) (row.get("taskname")));
			task.setNotes((String) row.get("notes"));
			task.setFeedback((String) row.get("feedback"));
			task.setStatus((String) row.get("status"));
			// task.setFeedback((Integer)row.get("AGE"));
			tasks.add(task);
		}
		if (tasks.size() > 0) {
			// tasks.sort((e1, e2) ->
			// (e1.getCreatedTime()).compareTo((e2.getCreatedTime())));
			/*
			 * Collections.sort(tasks, new Comparator<Task>() {
			 * 
			 * @Override public int compare(final Task object1, final Task
			 * object2) { return
			 * object1.getTaskName().compareTo(object2.getTaskName()); } });
			 */
		}
		return tasks.size() > 0 ? tasks : null;
	}
}

class TaskMapper implements RowMapper<Task> {
	public Task mapRow(ResultSet rs, int arg1) throws SQLException {
		Task task = new Task();
		task.setTaskName(rs.getString("taskname"));
		task.setNotes(rs.getString("notes"));
		task.setFeedback(rs.getString("feedback"));
		task.setStatus(rs.getString("status"));
		task.setAssignedby(rs.getString("assignedby"));
		task.setAssignedto(rs.getString("assignedto"));
		task.setTaskId(rs.getInt("taskid"));
		return task;
	}
}
