from datetime import datetime, timezone

naive = datetime(2025, 6, 24, 9, 0)
aware = naive.replace(tzinfo=timezone.utc,day=8,hour=0)

print("Naive:", naive)
print("Aware:", aware)
print(naive.isocalendar())