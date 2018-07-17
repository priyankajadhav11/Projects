package com.walmart.spring.dao;

import com.walmart.spring.model.Login;
import com.walmart.spring.model.User;

public interface UserDao {
     void register(User user);
	  User validateUser(Login login);
}
