# по количеству скамеечек на человека
top_by_benches = ["Auckland", "Osaka", "Adelaide", "Geneva", "Melbourne"]

# по количеству фонтанчиков на человека
top_by_fountains = ["Adelaide", "Geneva", "Osaka", "Melbourne", "Auckland"]

# по количеству качелек на человека
top_by_swings = ["Osaka", "Adelaide", "Geneva", "Melbourne", "Auckland"]

city = input()

print(f"по количеству скамеечек: {top_by_benches.index(city) + 1}\n"
      f"по количеству фонтанчиков: {top_by_fountains.index(city) + 1}\n"
      f"по количеству качелек:{top_by_swings.index(city) + 1}\n"
      f"В среднем занимает позицию:{round((top_by_benches.index(city) + 1 + top_by_fountains.index(city) + 1 + top_by_swings.index(city) + 1) / 3)}")
