def healthFilter(medicals, **filters):
    results = []
    for info in medicals:
        match = True
        for key, value in filters.items():
            # adjusting the logic to accept ages >= or <=
            if "_gte" in key:
                field = key.replace("_gte", "")
                if float(info.get(field, 0)) < float(value):
                # Avoids errors if the field is missing.
                # Falls back to 0 if Age doesn’t exist, so the code doesn’t crash
                    match = False
                    break
            elif "_lte" in key:
                field = key.replace("_lte", "")
                if float(info.get(field, 0)) > float(value):
                    match = False
                    break
            else:
                
                if info.get(key, "") != value:
                    match = False
                    break
        if match:
            results.append(info)
    return results