# PYKRX 모듈을 활용한 모멘텀 전략 백테스팅

PYKRX의 코스피 ohlcv 데이터를 활용하여 국내 유가 증권 시장에서의 상대 모멘텀 전략 효율성을 백테스팅해보았습니다.

---

1. Jegadeesh and Titman의 논문은, 미국 증권 시장에서 **모멘텀이 가장 높은 종목들의 평균 수익률**이 그렇지 않은 종목들의 평균적인 수익률보다 높음을 설명했습니다.
    
    이에 따라 국내 유가증권시장에서의 모멘텀 전략 수익률을 분석해보았습니다. 
    
    $$
    Momentum = (P1 - P0)/P0 * 100
    $$
    
    1. 모멘텀 상위 30개 종목 (우선주 포함)으로 투자 포트폴리오를 구성하였고, 동일 투자 기간 코스피 지수 CAGR(Compound Annual Growth Rate)과 비교하여 전략 효율성을 확인해보았습니다.
        
        $$
        CAGR = (V1-V0)**(1/n)-1
        $$
        
        ![무제.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/60c516c3-f4f5-4664-a9b3-c5fdfce32594/87a6f6b8-abf7-47a7-a587-94c368c09fb6/%E1%84%86%E1%85%AE%E1%84%8C%E1%85%A6.png)
        
        - 모멘텀 계산 값이 큰 상위 30개의 종목으로 포트폴리오를 구성하여, 수익률을 계산하였습니다.
        
        ![momentum.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/60c516c3-f4f5-4664-a9b3-c5fdfce32594/618bd1a6-c027-42d2-9034-860c8ac2be59/momentum.png)
        
        ![momentum porfolio.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/60c516c3-f4f5-4664-a9b3-c5fdfce32594/81122eba-0e34-4875-9cd5-a7dec9e1c2c3/momentum_porfolio.png)
        
        - 평균 수익률은 약 10.95854 %였으며, 동일 기간 코스피 지수 수익률은 약 14.75%로 소형주가 포함되어있는 모멘텀 전략 포트폴리오는 국내 유가증권시장에서 수익성이 다소 떨어짐을 확인할 수 있었습니다.
    2. 한국 유권 시장에서는 상대 모멘텀 전략이 소형주보다 대형주에 효과적으로 알려져있습니다. 따라서, 시가 총액 기준 상위 20개의 대형주를 포트폴리오로 구성하여 상대 모멘텀 전략을 백테스팅 하였습니다.
        - 우선, 모멘텀 값이 큰 200개의 종목을 필터링 하였고 다음으로 시가총액을 기준으로 상위 20개 대형주를 포트폴리오로 구성하였습니다.
        
        ![momentum (big).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/60c516c3-f4f5-4664-a9b3-c5fdfce32594/11d1fa95-2be6-4cb4-a51c-e66592072992/momentum_(big).png)
        
        ![results(cagr).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/60c516c3-f4f5-4664-a9b3-c5fdfce32594/6b8b952b-d7a1-468a-b35a-508c3e9f52ad/results(cagr).png)
        
        대형주로 구성된 포트폴리오의 평균 수익률은 약 269.1327%였으며, 동일 투자 기간 코스피 지수 수익률은 약 -2.51960% 였습니다. 개인적인 의견으로는, 해당 포트폴리오 평균 수익률에 큰 영향을 미친 것은 ‘포스코 DX’ 였으며 투자 기간인 start = '20221102', end = '20231031' 사이에, 포스코 DX는 2023년도 1~3분기 연결기준 영업이익은 964억 원으로 전년 동기보다 95% 급증했습니다. 
        
        대형주로 구성된 포트폴리오가 효과적인 건 명백하지만, 상황적 특수성을 고려하지 못하는 CAGR이치명적인 요인을 가지고 있다는 것 또한 확인할 수 있었습니다.
