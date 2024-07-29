from datetime import datetime


class EndpointUtil():
    """
    A mixin class to handle common methods between both Competitions and
    Team class.
    """

    def clean_matches_list(self, match_data) -> list:
        """
        Cleans the match data and pulls the necessary information

        :param match_data: JSON object to retrieve data from
        """
        matches = []

        for m in match_data:

            home_team = m["homeTeam"]["name"]
            home_score = m["score"]["fullTime"]["home"]
            away_team = m["awayTeam"]["name"]
            away_score = m["score"]["fullTime"]["away"]
            score = f'{home_score}-{away_score}'

            format_date = datetime.strptime(m["utcDate"], '%Y-%m-%dT%H:%M:%SZ')
            match_date = (f'{format_date.day}/{format_date.month}/'
            f'{format_date.year}')

            match = {
                "Date": match_date,
                "Home": home_team,
                "Score": score,
                "Away": away_team
            }
            matches.append(match)
        return matches
