-- Ejecutar estrictamente despues de correr la base

INSERT INTO  FaultStatus (id_status, status) VALUES (1,"Pending");
INSERT INTO  WorklogStatus (id_status, status) VALUES (1,"Pending");
INSERT INTO User_Operator (id_user,approved_hours,pending_hours) VALUES (1,50,20);