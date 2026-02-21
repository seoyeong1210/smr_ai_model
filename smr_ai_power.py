# model: How many SMRs are needed for an AI data center?

# 가정
servers = 50000              # AI 서버 개수
power_per_server_kw = 4      # 서버 1대당 평균 전력 (kW)
smr_capacity_mw = 300        # SMR 1기 발전 용량 (MW)

# 총 전력 계산 (kW)
total_power_kw = servers * power_per_server_kw

# MW로 변환
total_power_mw = total_power_kw / 1000

# 필요한 SMR 개수
smr_needed = total_power_mw / smr_capacity_mw

print("Total power needed (MW):", total_power_mw)
print("Estimated SMRs required:", round(smr_needed, 2))
