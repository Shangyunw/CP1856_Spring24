# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:49:24 2024

@author: Arun.Rameshbabu
"""


players = {'Joel': {'Position':'S', 'At Bats': 5, 'Strike Rate': 75.5},
           'Anne': {'Position':'LB', 'At Bats': 15, 'Strike Rate': 85.5, 'Hits': 10},
           'Ben': {'Position':'SS', 'At Bats': 4, 'Strike Rate': 15.5, 'Superpower':'Absent'}}

players['Anne']
players['Anne']['Strike Rate']
players['Anne']['Superpower']

players.get('Anne') # Same as line 12
players.get('Anne').get('Strike Rate')

players.get('Mike', {}).get('Strike Rate')

players_list = {'Joe': ['P', 10, 2],
                'Tom': ['SS', 11, 4],
                'Ben': ['C', 4, 1]}
players_list.keys()
players_list['Joe'][2]
players_list.get('Joe')[2]

players['Anne']['Superpower'] = 'Home Run'
players_list.get('Joe').append('Roundhouse Kick')
