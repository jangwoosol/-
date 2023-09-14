-- 코드를 입력하세요
select a.APNT_NO, patient.pt_name,	a.PT_NO,	a.MCDP_CD,	a.DR_NAME,	a.APNT_YMD
from (select appointment.APNT_NO,	appointment.PT_NO,	doctor.MCDP_CD,	doctor.DR_NAME,	appointment.APNT_YMD from doctor join appointment on doctor.dr_id=appointment.mddr_id where APNT_CNCL_YN="N") as a join patient on a.pt_no=patient.pt_no
where a.APNT_YMD like "2022-04-13%" and a.mcdp_cd="CS"
order by a.APNT_YMD