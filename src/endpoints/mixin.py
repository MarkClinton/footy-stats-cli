from datetime import datetime

class Mixin():

    """
    A mixin class to handle common methods between endpoints
    """

    def clean_matches_list(self, match_data) -> list:
        """
        Cleans the match data and pulls the necessary information

        :param match_data: JSON object to retrieve data from
        """
        matches = []

        for m in match_data:
            home_score = m["score"]["fullTime"]["home"]
            away_score = m["score"]["fullTime"]["away"]
            result = f'{home_score}-{away_score}'

            format_date = datetime.strptime(m["utcDate"], '%Y-%m-%dT%H:%M:%SZ')
            match_date = f'{format_date.day}/{format_date.month}/{format_date.year}'
            winner = m["score"]["winner"].replace('_TEAM','')
            
            match = {
                "Date": match_date,
                "Home": m["homeTeam"]["name"],
                "Away": m["awayTeam"]["name"],
                "Winner": winner,
                "Result": result
            }
            matches.append(match)
        return matches