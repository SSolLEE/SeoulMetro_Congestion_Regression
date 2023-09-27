# SeoulMetro_Congestion_Regression
Project at MultiCampus 

## TITLE OF CONTENTS
- [PLAN](#PLAN)
  - [Outline](#Outline)
  - [BackGround](#BackGround)  
- [DATA](#DATA)
  - [Data_Collection](#Data_Collection)
  - [Data_Preprocessing](#Data_Preprocessing)
- [FINAL_CONGESTION](#FINAL_CONGESTION)
  - [Average_Congestion](#Average_Congestion)
  - [Calculation](#Calculation)
  - [FINAL_CONGESTION](#FINAL_CONGESTION)
- [ML-REGRESSION](#ML-REGRESSION)
  - [LEARNING_METHOD](#LEARNING_METHOD)
  - [Evaluation_Indicators](#Evaluation_Indicators)
- [WEB_SERVICE](#WEB_SERVICE)
  - [SERVICE](#SERVICE)
  - [DASHBOARD](#DASHBOARD)
  - [LOGIC](#LOGIC)
- [CONCLUSION](#CONCLUSION)
  
## PLAN
### Outline
- 프로젝트명: 지하철 혼잡도 예측 및 사용자 분산 서비스
- 팀명: Transit Insights
- 팀원: 이승준, 김은채, 이나윤, 이솔, 최소현, 허준영
- 기간: 2023.09.01~2023.09.26

### BackGround
-  서울 지하철 이용객이 점차 증가함에 따라, 특히 혼잡도가 큰 출퇴근시간대의 지하철 내 안전성 문제가 대두되고 있습니다.
-  이미 서울 지하철의 혼잡도는 아래 이미지와 같이 권고되는 150%를 넘어선 노선이 존재합니다. 
 ![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/0311a4fd-ae3e-4d0f-8538-c6cf9995bccc)
- 현재 지하철 혼잡도를 제공해주는 앱이 존재하지만, 서비스가 중단된 상태이거나 최신 열차 내부에서만 확인이 가능하고, 서비스 제공 시점의 정보만 알 수 있습니다.
- 따라서 이번 프로젝트를 통해
  - **서울교통공사 1~8호선 노선정보를 제공**하고
  - **사용자가 조건을 입력하여 원하는 혼잡도 정보를 제공**하며
  -  지하철 탑승 전 **미리 혼잡도를 예측**함으로써 
- 서울 지하철 이용객들의 안전성과 편의성을 증진하고, 관련 정책에 대한 대책마련의 근거가 되며 운영사에게는 혼잡도 정보를 통해 편익 산출을 할 수 있는 좋은 서비스를 제공하고자 합니다.
 
## DATA
### Data_Collection
- 처음 지하철 혼잡도에 영향을 주는 변수로 생각한 것은 **승객수(혼잡도), 시간대, 날씨**였습니다.
- 따라서 이와 관련한 data를 서울열린데이터광장, 공공데이터포털, 기상청에서 수집하였습니다.
 
### Data_Preprocessing
-  Missing value : 운행하지 않는 시간대의 인원이 0 또는 Null값으로 존재합니다.
  -  0으로 처리
- Data Filtering
  - data 선정 및 기간 설정 :  COVID-19 관련 정부지침으로 2022~2021년 승차인원 패턴이 이전과 달라졌습니다.
    - 혼잡도 data에서 2020~2021년에 해당하는 data는 제외하고 사용
  - 7호선 중 인천교통공사가 담당하는 구간에 해당하는 역의 일부가 연도별로 불규칙하게 포함되어 있습니다.
    - 삭제. 서울교통공사가 제공하는 노선과 역만을 이용하여 프로젝트 진행
  - 모든 역병은 최신화하였습니다.
  - 공휴일은 일요일로 분류하였습니다. 
  -  날씨 데이터 삭제
    - EDA를 진행한 결과 날씨 조건은 지하철 혼잡도에 영향을 주는 유의미한 변수가 아니라고 판단하였습니다.
    - 평균기온 & 강수량과 승차총승객수 사이에 상관관계가 강하게 나타나지 않았습니다.
    - 기상조건별 지하철 이용객 수를 비교했을 때, 오차범위가 크게 나타납니다.
    - 2023년 1~7월 지하철 이용객 수의 큰 차이가 없습니다.
      ![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/eaeb661f-3e34-4854-a24c-cf9102d340d0)

## FINAL_CONGESTION
### Average_Congestion
- 연도별 혼잡도 data는 평일, 토요일, 일요일로 구분되어 있으나 월~일요일로 요일별 구분이 되어 있지 않습니다.
- 또한 월별 데이터가 제공되지 않습니다.
- 따라서 우리는 승차인원 data와 혼잡도 data를 이용하여 최종 혼잡도라는 파생변수를 만들었습니다.
 
### Calculation
![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/b190cdf5-8ffd-48b1-97a2-87ab1807f8fd)

### FINAL_CONGESTION
- 최종혼잡도의 data 형태는 다음과 같습니다.
  - YEAR : 연도
  - MONTH : 월
  - DAY : 일
  - LINE : 호선
  - STATION : 역명
  - DIRECTION : 상선/하선
  - TIME_00 : 시간대(한시간단위)
  - CONGESTION : 최종혼잡도
 ![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/02d317e9-05c0-464b-a304-4aeb0e60cf8f)

## ML-REGRESSION
### LEARNING_METHOD
- 데이터셋 분리 : 독립변수 / 종속변수 분리
- 데이터 분리 : 홀드아웃방식
- 적용 : 원-핫 인코딩
- 파이프라인 생성
- 하이퍼 파라미터 튜닝
- 평가/선정 : **XGBRegressor**
  - 모델 선정 근거 : 결론적으로 성능이 가장 좋은 모델을 선정
    - RandomForestRegressor는 학습 시간이 길면서도 성능 향상인 낮았습니다.
    - LinearRegressor는 범주형 변수를 사용하다보니 설명력이 낮았습니다.
    - LGBMRegressor는 성능이 낮지만 학습 시간이 유리했습니다.
    - XGBRegressor는 가장 높은 성능을 나타냈지만 학습 시간이 오래걸렸습니다.
### Evaluation_Indicators
- 호선별 평가지표는 다음과 같습니다.
  ![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/4683e542-6929-421e-baad-620ad908bad5)

## WEB_SERVICE
- 지하철 혼잡도 예측한 결과를 사용자들이 실제로 웹을 통해서 검색할 수 있습니다.
### SERVICE
- 머신러닝 구현한 결과를 서비스화하였습니다.
- 학습데이터는 pkl 파일로 저장하였고 출발역/도착역, 시간을 변수로 삽입하였습니다.
- 노선도 내에서 지선에 해당하는 노선은 별도 호선으로 관리합니다.
  ![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/39274d3d-1dc5-4b87-a14d-9b20d1f2dc37)
- 웹 구현 영상 : [YOUTUBE LINK](https://www.youtube.com/watch?v=phZRdA8Wsik)

### DASHBOARD
- 최종혼잡도를 평균 또는 표준편차로 처리하여 사용자들이 노선별, 각 역별 혼잡도의 대략적인 경향성을 확인할 수 있도록 제작하였습니다.
- 요일별 혼잡도는 파이 차트로, 시간대별 혼잡도는 상/하선 구분하여 선 그래프로, 시간대와 역을 한번에 볼 수 있는 것은 히트맵으로 구현하였습니다.
![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/72104785-dc4e-4192-a893-bb231a147165)

### LOGIC
![image](https://github.com/SSolLEE/SeoulMetro_Congestion_Regression/assets/139443410/ab97fcfb-1795-48a7-8151-12b17277d71a)

## CONCLUSION
- 서울교통공사가 제공하는 data만 사용하였기 때문데 서울을 지나는 전체 지하철역에 대한 예상 혼잡도 data를 제공할 수 없습니다.
  - 서울시 노선도의 다른 운영사에 혼잡도 data를 요청하여 가용 노선을 늘림으로써 개선할 수 있습니다.
- 실시간 지하철 혼잡도 data를 사용하지 못합니다.
  - 과거 데이터로만 예측을 수행하다보니 실제 상황과 차이가 있을 것입니다.
  - 통신 빅데이터와 융합하여 데이터를 보완하면 실시간 혼잡도를 적용할 수 있습니다. 
- COVID-19 이후 최신 혼잡도 data는 2022년만 존재합니다. 또한 연도별 data 불충분으로, 최종혼잡도 산출 과정에서 오차가 나타날 수 있습니다.
  - 추후 데이터 누적으로 정확도 향상을 기대할 수 있습니다. 
- 웹 서비스는 PC접속은 원활하나, 모바일로 접속했을 때 사용자들의 불편이 컸습니다.
  - 모바일 서비스까지 제공하여 사용자 편의성을 높일 수 있습니다.
  
### THE END ####
