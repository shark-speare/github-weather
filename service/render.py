from service.location import Location, TimeSlot

dtformat = "%m/%d %H:%M"

def _slot_rows(now: TimeSlot, fut: TimeSlot, key: str, unit: str = "") -> str:
    """產生現在／未來兩列的 markdown table rows"""
    now_val = getattr(now, key)
    fut_val = getattr(fut, key)
    return (
        f"| 現在 | `{now_val.start.strftime(dtformat)}` ～ `{now_val.end.strftime(dtformat)}` | **{now_val.value}{unit}** |\n"
        f"| 未來 | `{fut_val.start.strftime(dtformat)}` ～ `{fut_val.end.strftime(dtformat)}` | **{fut_val.value}{unit}** |"
    )


def _uv_rows(now: TimeSlot, fut: TimeSlot) -> str:
    return (
        f"| 現在 | `{now.uv.start.strftime(dtformat)}` ～ `{now.uv.end.strftime(dtformat)}` | **{now.uv.index}** | {now.uv.level} |\n"
        f"| 未來 | `{fut.uv.start.strftime(dtformat)}` ～ `{fut.uv.end.strftime(dtformat)}` | **{fut.uv.index}** | {fut.uv.level} |"
    )


def _sun_row(sun) -> str:
    return (
        f"| {sun.date} "
        f"| 🌄 `{sun.rise}` "
        f"| 🕛 `{sun.transit_time}`（仰角 {sun.transit_alt}°）"
        f"| 🌇 `{sun.set}` |"
    )


def format_article(loc: Location) -> str:
    now, fut = loc.now, loc.future

    return f"""\
# 📍 {loc.name} 天氣預報

---

## 🌡️ 氣溫

| 時段 | 時間區間 | 氣溫 |
|------|----------|------|
{_slot_rows(now, fut, "temperature", " °C")}

---

## 🌧️ 降雨機率

| 時段 | 時間區間 | 機率 |
|------|----------|------|
{_slot_rows(now, fut, "rain", " %")}

---

## 💨 風況

### 風向

| 時段 | 時間區間 | 風向 |
|------|----------|------|
{_slot_rows(now, fut, "direction")}

### 風速

| 時段 | 時間區間 | 風速 |
|------|----------|------|
{_slot_rows(now, fut, "speed", " m/s")}

---

## 🔆 紫外線

| 時段 | 時間區間 | 指數 | 等級 |
|------|----------|------|------|
{_uv_rows(now, fut)}

---

## 🌤️ 天氣現象

| 時段 | 時間區間 | 現象 |
|------|----------|------|
| 現在 | `{now.weather.start.strftime(dtformat)}` ～ `{now.weather.end.strftime(dtformat)}` | {now.weather.value} |
| 未來 | `{fut.weather.start.strftime(dtformat)}` ～ `{fut.weather.end.strftime(dtformat)}` | {fut.weather.value} |

---

## 📝 綜合描述

> **現在**（`{now.desc.start.strftime(dtformat)}` ～ `{now.desc.end.strftime(dtformat)}`）
>
> {now.desc.value}

> **未來**（`{fut.desc.start.strftime(dtformat)}` ～ `{fut.desc.end.strftime(dtformat)}`）
>
> {fut.desc.value}

---

## 🌅 日出日落

| 日期 | 日出 | 過中天 | 日落 |
|------|------|--------|------|
{_sun_row(now.sun)}
{_sun_row(fut.sun)}
"""


if __name__ == "__main__":
    from service.fetch import fetch

    city = "臺北市"
    raw = fetch(city)
    loc = Location.from_dict(raw)
    print(format_article(loc))