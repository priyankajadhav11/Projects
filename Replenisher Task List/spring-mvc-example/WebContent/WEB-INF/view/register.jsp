<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Register User</title>
</head>
<body>
<form:form id="regForm" modelAttribute="user" action="registerProcess" method="post">
                <table align="center">
                    <tr>
                        <td>
                            <form:label path="username">Username</form:label>
                        </td>
                        <td>
                            <form:input path="username" name="username" id="username" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="password">Password</form:label>
                        </td>
                        <td>
                            <form:password path="password" name="password" id="password" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="firstname">FirstName</form:label>
                        </td>
                        <td>
                            <form:input path="firstname" name="firstname" id="firstname" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="lastname">LastName</form:label>
                        </td>
                        <td>
                            <form:input path="lastname" name="lastname" id="lastname" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="emailId">Email</form:label>
                        </td>
                        <td>
                            <form:input path="emailId" name="emailId" id="emailId" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="role">Role</form:label>
                        </td>
                        <td>
                            <form:input path="role" name="role" id="role" />
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <form:label path="roleid">Role Id</form:label>
                        </td>
                        <td>
                            <form:input path="roleid" name="roleid" id="roleid" />
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <form:button id="register" name="register">Register</form:button>
                        </td>
                    </tr>
                    <tr></tr>
                    <tr>
                        <td></td>
                        <td><a href="home">Home</a>
                        </td>
                    </tr>
                </table>
            </form:form>
</body>
</html>