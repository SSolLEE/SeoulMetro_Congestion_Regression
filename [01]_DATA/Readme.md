# 데이터 내용정리
1. 서울교통공사 역별 시간대별 혼잡도 (11,13,15,17,19,21,22년도)
  * 혼잡도 (%) 표기, 월별 평균 통계, 평일/토요일/공휴일 구분 , 상/하행 구분
  * 15년 이전데이터는 1시간단위
  * 21년도 데이터는 00시부터의 데이터가 없음 (코로나 시기라 운행단축으로 인해 없는것 같음)

2. 서울교통공사 연도별 일별 역별 시간대별 승하차인원(1_8호선)
  * 승하차인원 (명) 표기, 하루 당 인원 표기, 승차/하차 인원 구분, 상/하행 구분 없음

3. 서울교통공사 월별 승하차인원
  * 승하차인원(명) 표기, 월 전체 인인원표기(?), 상/하행 구분 없음

4. 비율 산출
<<<<<<< HEAD
  * 역별 요일별 비율 산출(2022년 기준)
    - 공휴일 == 일요일로 변경
    - 2022년 각 요일별 평균 계산 후 비율 산출
    - (월요일평균이용객수) / {(일주일전체합평균)/7일}  = 월요일 비율 
  * 역별 월별 비율 산출(2018, 2019, 2022년 기준)
    - 3개년 각 월별 평균 계산 후 비율 산출
    - (1월평균 이용객수) / {(월전체합평균)/12개월} 
=======<<최종 산출 과정>>========
  * 요일별 비율 산출
    - (월요일평균이용객수) / {(일주일전체합평균)/7일}  = 월요일 비율 
    - 2022년 자료 이용
    - 7호선 인천라인 보강
    - 충무로역, 연신내역 결측치는 환승역 혼잡도 비율로 승객수 분리하여 산출
   
   * 월별 비율 산출
    - 2015년~ 2022년 자료(**2022년, 2021년 자료 배제**)
