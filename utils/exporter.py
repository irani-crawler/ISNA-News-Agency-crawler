import csv

def save_to_csv(data, filename):
    if not data:
        print(f"[⚠️] No data to save for {filename}")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"[💾] Saved {len(data)} records to {filename}")
