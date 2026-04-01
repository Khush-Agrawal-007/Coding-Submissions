def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.sort_values("id").reset_index(drop=True)
    
    for i in range(0, len(seat) - 1, 2):
        seat.loc[i, "student"], seat.loc[i+1, "student"] = (
            seat.loc[i+1, "student"],
            seat.loc[i, "student"]
        )
    
    return seat