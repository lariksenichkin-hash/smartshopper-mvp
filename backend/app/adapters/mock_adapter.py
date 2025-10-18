# Возвращает простой список mock-предложений

def search_mock(query: str):
    # Простейшая логика: базовые примеры для лекарств, одежды, техники
    q = query.lower()
    items = []
    if 'ибупрофен' in q or 'парацетамол' in q or 'лекар' in q:
        items = [
            {"title": "Ибупрофен 200 мг, 20 таб", "price": 120, "source": "Аптека А", "type": "medicine", "availability": "in_stock", "pickup": {"distance_km": 0.8}},
            {"title": "Ибупрофен суспензия 100мг/5мл", "price": 250, "source": "Аптечная сеть B", "type": "medicine", "availability": "in_stock", "pickup": {"distance_km": 2.2}},
        ]
    elif 'куртка' in q or 'зимняя' in q or 'одежд' in q:
        items = [
            {"title": "Зимняя куртка X, размер L", "price": 8999, "source": "Маркетплейс Y", "type": "clothing", "availability": "warehouse", "pickup": {"distance_km": 5}},
        ]
    else:
        items = [
            {"title": "Универсальный товар A", "price": 1999, "source": "AliExpress", "type": "general", "availability": "online", "pickup": None},
        ]
    return items
