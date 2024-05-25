import requests

class IDAC(object):
    def __init__(self):
        pass

    # Get

    def get_current_round(self):
        return requests.get('https://initiald.sega.jp/inidac/json/ranking/v1/currentRoundInfo.json').text
    
    def get_const(self):
        return requests.get('https://initiald.sega.jp/inidac/json/ranking/v1/const.json').json()

    def get_course_info(self, course, area = 'all', car = 'all'):
        return requests.get(f'https://initiald.sega.jp/inidac/json/ranking/v1/timeTrial/ta_course-{course}_area-{area}_car-{car}.json').json()
    
    def get_round_info(self, round, area = 'all'):
        return requests.get(f'https://initiald.sega.jp/inidac/json/ranking/v1/roundPoint/rp_round-{round}_area-{area}.json').json()

    def get_store_battle_info(self, area = 'all'):
        return requests.get(f'https://initiald.sega.jp/inidac/json/ranking/v1/shopBattle/sb_area-{area}.json').json()
    
    def get_team_ranking_info(self, _round, rank = 6):
        if (rank < 3 or rank > 6):
            return False
        
        return requests.get(f'https://initiald.sega.jp/inidac/json/ranking/v1/leaguePoint/lp-round-{_round}_rank-{rank}.json').json()
    
    def get_pride_info(self):
        return requests.get('https://initiald.sega.jp/inidac/json/ranking/v1/pride/pride-all.json').json()

    # Find

    def find_in_current_round_by_name(self, driver_name, area = 'all'):
        current_round = self.get_current_round()
        round_info = self.get_round_info(current_round, area)
        player = next((item for item in round_info['records'] if item["name"] == driver_name), None)
        return player
    
    def find_in_time_trial_by_name(self, course, driver_name, area = 'all', car = 'all'):
        course_info = self.get_course_info(self, course, area, car)
        player = next((item for item in course_info['records'] if item["name"] == driver_name), None)

        return player