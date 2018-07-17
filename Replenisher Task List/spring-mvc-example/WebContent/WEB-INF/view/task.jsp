<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<form:form id="taskForm" modelAttribute="task" action="taskProcess"
		method="post">
		<table align="center">
			<tr>
				<td><form:label path="taskName">Task Name</form:label></td>
				<td><form:input path="taskName" name="taskName" id="taskName" />
				</td>
			</tr>
			<tr>
				<td><form:label path="notes">Notes</form:label></td>
				<td><form:input path="notes" name="notes" id="notes" /></td>
			</tr>
			<tr>
				<td><form:label path="feedback">Feedback</form:label></td>
				<td><form:input path="feedback" name="feedback" id="feedback" />
				</td>
			</tr>
			<tr>
				<td><form:label path="estHours">Estimated Hours</form:label></td>
				<td><form:input path="estHours" name="estHours" id="estHours" />
				</td>
			</tr>
			<tr>
				<td><form:label path="assignedto">Assigned To</form:label></td>
				<td><form:input path="assignedto" name="assignedto"
						id="assignedto" /></td>
			</tr>
			<tr>
				<td><form:label path="assignedby">Assigned By</form:label></td>
				<td><form:input path="assignedby" name="assignedby" id="role" />
				</td>
			</tr>
			<tr>
				<td><form:label path="priority">Priority</form:label></td>
				<td><form:select path="priority">
						<form:option selected="selected" value="Low">LOW</form:option>
						<form:option value="Medium">MEDIUM</form:option>
						<form:option value="High">HIGH</form:option>
					</form:select></td>
			</tr>
			<tr>
				<td></td>
				<td><form:button id="task" name="task">Create Task</form:button>
				</td>
			</tr>
			<tr></tr>
			<tr>
				<td></td>
				<td><a href="home">Home</a></td>
			</tr>
		</table>
	</form:form>

	<table align="center">
		<tr>
			<td style="font-style: italic; color: red;">${message}</td>
		</tr>
	</table>
</body>
</html>