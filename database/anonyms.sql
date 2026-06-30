SELECT rolname, rolcanlogin
FROM pg_roles
WHERE rolname = 'querymind_user';

ALTER ROLE querymind_user LOGIN;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO querymind_user;


GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO querymind_user;