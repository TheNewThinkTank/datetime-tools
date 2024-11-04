

def bisect_year(half_year: int) -> list[str] | str:
    halfyear_months = {
        1: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        2: ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    }
    return halfyear_months.get(half_year, "Invalid value. Must be 1 or 2")
