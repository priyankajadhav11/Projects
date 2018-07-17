<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Welcome</title>
</head>
<body>
<table>
            <tr>
                <td>Welcome ${firstname}</td>
            </tr>
               <tr>
                <td><a href="task">Create Task</a>
                </td>
            </tr>
               <tr>
                <td><a href="home">Home</a>
                </td>
            </tr>
            <c:if test="${not empty tasklist}">
             <c:forEach var="listValue" items="${tasklist}">
        <tr>
            <td>${listValue.taskName}</td>
            <td>${listValue.notes}</td>
            <td>${listValue.feedback}</td>
            <td>${listValue.status}</td>
        </tr> 
       
    </c:forEach> </c:if>
        </table>
</body>
</html>