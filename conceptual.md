### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is a relational database management system that works with SQL.

- What is the difference between SQL and PostgreSQL?
While PostgreSQL is the database management system, SQL is the actual language used to manage the database.

- In `psql`, how do you connect to a database?
\c <DATABASE NAME>;

- What is the difference between `HAVING` and `WHERE`?
WHERE is used to filter rows from the overall table into a result set. HAVING is used to then filter that result set by certain characteristics.

- What is the difference between an `INNER` and `OUTER` join?
An INNER JOIN will return only the data that two tables have in common. An OUTER JOIN will return all data between two tables, regardless of relationship.
Given 2 tables (TABLE 1 and TABLE 2), a LEFT OUTER JOIN will return all the data from TABLE 1, and from TABLE 2 only the data which corresponds to TABLE 1 data. A RIGHT OUTER JOIN is the inverse, containing all data from TABLE 2, and from TABLE 1 only the data which corresponds to TABLE 2 data.

- What is an ORM? What do they do?
An ORM (Object-relational Mapping tool) is a tool used to manipulate databases with more common object-oriented languages like Python and Javascript.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
Making HTTP requests from the client-side (like with AJAX) can be faster and more responsive than using server side "requests". AJAX in particular uses asynchronous requests, meaning the client does not have to wait for a response. However, client-side code must supported by the clients browser in order to work.

- What is CSRF? What is the purpose of the CSRF token?
CSRF (Cross-site request forgery) is an attack on a website that attempts to make malicious requests while appearing to be a "trusted" user.

- What is the purpose of `form.hidden_tag()`?
This tag is used by FLASK-WTF to implement CSRF protection in a form.