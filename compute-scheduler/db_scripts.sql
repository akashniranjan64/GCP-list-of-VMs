insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','instance-3',1,'2023-04-07 08:00:00','2023-04-07 17:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','test-notebook-1',2,'2023-04-07 09:00:00','2023-04-07 18:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','testssh',3,'2023-04-07 10:00:00','2023-04-07 19:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','tfclonetestanslwr001',4,'2023-04-07 11:00:00','2023-04-07 20:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','vlapssreplgrndtst',5,'2023-04-07 12:00:00','2023-04-07 21:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','cluster-f540-m',5,'2023-04-07 13:00:00','2023-04-07 22:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','instance-2',5,'2023-04-07 14:00:00','2023-04-07 23:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('playground-aps-sre-sb','vwapssredev001',4,'2023-04-07 15:00:00','2023-04-07 23:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('test-project-for-test','instance-of-test-project',1,'2023-04-07 08:00:00','2023-04-07 17:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('test-project-for-test','instance-of-test-project',1,'2023-04-07 08:00:00','2023-04-07 17:00:00',false);
insert into VMs_list(project_name,vm_name,vm_schedule_temp,vm_sch_start,vm_sch_stop,vm_status) values('test-project-for-test','instance-of-test-project',1,'2023-04-07 08:00:00','2023-04-07 17:00:00',false);

----------------------------------------------------------

insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','instance-3','08:00:00','13:00:00',false,'northamerica-northeast1-a');
insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','test-notebook-1','09:00:00','14:00:00',false,'northamerica-northeast1-a');
insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','testssh','10:00:00','15:00:00',false,'northamerica-northeast1-a');
insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','tfclonetestanslwr001','11:00:00','16:00:00',false,'northamerica-northeast1-a');
insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','cluster-f540-m','13:00:00','18:00:00',false,'northamerica-northeast1-b');
insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_status,vm_zone) values('playground-aps-sre-sb','instance-2','14:00:00','19:00:00',false,'northamerica-northeast1-b');



insert into VMs_list_TEMP(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone,day_of_week) values('playground-aps-sre-sb','instance-2','14:00:00','19:00:00','northamerica-northeast1-b','mon,tue,wed');
insert into VMs_list_TEMP(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone,day_of_week) values('playground-aps-sre-sb','instance-3','14:00:00','19:00:00','northamerica-northeast1-b','tue,wed,fri');
insert into VMs_list_TEMP(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone,day_of_week) values('playground-aps-sre-sb','instance-3','15:00:00','22:00:00','northamerica-northeast1-b','sat,sun');
insert into VMs_list_TEMP(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone,day_of_week) values('playground-aps-sre-sb','instance-4','15:00:00','22:00:00','northamerica-northeast1-b','3,4');


update VMs_list set vm_sch_stop='17:00:00';
update table VMs_list_TEMP



SELECT project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone from VMs_list_TEMP where day_of_week = (select DAYOFWEEK(CURDATE()));

ALTER table VMs_list ADD start_days varchar(255) NOT NULL;

ALTER table VMs_list ADD stop_days varchar(255) NULL;

