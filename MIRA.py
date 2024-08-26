#!/usr/bin/env python3

about = """
---------------------------------------------------------------
Project: MIRA - GiraSec Solutions's CLI Password Manager
GitHub Repository: https://github.com/z33phyr/MIRA
License: End-User License Agreement (EULA)

Version: 1.3.1
Release Date: 2024-07-26
---------------------------------------------------------------
"""

remember = r'''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣴⣿⣺⣿⣿⡖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣔⣠⣴⣾⣿⠟⠋⢋⣉⣀⠉⠉⠉⠉⠒⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠞⠛⠻⢛⠽⠊⣡⢴⣾⠿⠛⣷⠇⠀⢉⣉⣿⡗⠒⠾⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣟⣤⣂⣠⢖⣥⣤⣾⠗⠋⠀⢀⣾⢸⡀⠖⠉⠉⠛⢿⣶⣖⠺⣷⣦⣅⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⠃⢀⣤⣾⣿⣿⢸⡇⠀⠀⠀⠀⠈⢉⠛⢿⣦⣝⣮⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢾⣇⠀⣿⣿⡟⠟⠃⣾⣿⣖⣂⠀⠀⠀⠀⠉⢹⣿⣷⣽⣿⢷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠏⠝⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣾⣿⡛⠁⢀⣼⣿⣯⣭⣙⡒⠀⠀⠈⠒⢾⣿⣏⠘⣿⣇⠙⣧⡀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⢈⣹⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣙⣷⣶⣿⣿⣿⣿⣛⠷⠄⠀⠀⠀⠀⠀⠘⠏⡆⠀⣿⠀⠀⢳⡀
⠀⠀⠀⠀⠀⠀⠀⢸⣯⣇⡠⣾⠻⠋⠀⣸⠋⡟⠛⠿⣋⣉⣙⢿⣿⡆⠐⠾⠿⣿⣟⡛⠛⡿⠧⡀⣄⠀⠱⡀⠢⡀⠀⣄⡀⢸⡇⠀⠀⢇
⠀⠀⠀⣀⣠⣴⡚⠛⢉⡁⠀⠈⠑⣶⣾⡯⠚⠀⠀⠀⠐⠚⠛⠷⠻⣿⡀⠀⠀⠀⠈⠙⠢⠈⢆⠀⠘⢧⠀⣇⠀⠹⡀⠸⣧⣼⡇⠀⠰⢸
⣠⣖⡛⣿⠉⠉⠀⠀⠀⠈⠑⠂⠀⠀⠀⠀⠒⠒⠀⠀⣀⣀⡀⠀⠀⠙⠟⢦⣹⡶⣤⠂⠀⣄⢈⣷⣀⠀⠁⢡⠀⠀⣧⠀⣿⣿⠀⠀⠀⢺
⠻⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⣀⣀⣀⡤⠖⠛⠙⠛⠉⠁⣀⡀⣀⠀⠈⠙⠀⠹⣦⣹⡿⡟⢿⣧⠀⠈⣆⠀⣿⣦⠟⠃⠀⠀⣆⠘
⠀⠙⠯⣗⢚⣒⣿⠟⣿⣽⣿⣿⣿⣶⣍⣉⡉⠒⠊⠘⠛⠉⢹⡟⣱⣟⠁⣶⣤⣤⣀⡀⣿⣿⣅⠇⠘⠟⣷⠀⣼⣷⣿⠁⠀⠀⢠⣤⣿⠀
⠀⠀⠀⠈⠙⠻⢿⣷⢼⣆⠙⢻⣿⣿⣿⠟⣿⢢⡀⠀⠀⣠⠿⠿⠿⣋⠀⢹⣿⠀⠀⢹⡿⠈⠉⠀⠈⠀⠈⣧⡟⠈⠻⠆⢠⢀⡿⣿⢻⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠸⣦⣿⣧⢱⠀⡔⠁⠀⠀⠐⠦⣱⣾⠽⠀⠀⣀⠀⡀⡄⠀⠀⠀⠀⢉⠀⡀⠀⠀⣸⣾⠁⢻⣸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠇⣹⣟⣼⠾⠀⠀⣰⠶⠾⣟⡛⢻⡇⢰⠀⢠⡇⣸⣿⣧⠀⢀⣴⠀⣼⣰⡇⠀⢰⡿⢡⠄⢈⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣸⠿⣴⣳⣿⠇⢀⡠⠊⠀⠀⠀⠀⢱⣷⠀⣼⠆⣸⣿⣻⢻⣿⢀⣈⣿⣶⡿⢫⢇⣴⠟⢁⡎⣰⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣼⣷⣿⣿⠋⢀⡜⠁⠀⠀⠀⠀⠀⠀⢠⠟⣽⢼⣿⠆⠁⢸⣯⣼⣿⠟⠙⣠⠿⠛⠁⢀⣾⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠷⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⢁⠁⠀⣿⠋⠀⠀⠀⡈⠀⡴⠀⣠⣾⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⣡⡴⠋⠀⠀⠇⣠⠀⠠⠊⣡⣾⣥⠾⠋⠸⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣧⣾⡟⠁⠀⠀⣠⡼⢃⣤⡶⠟⣻⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣠⣴⡾⢿⣿⡿⠋⠁⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠛⠁⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⠀⠀⠀⠀

'''

blehhh = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠸⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⢸⠸⠀⡠⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⢠⣞⣀⡿⠀⠀⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡖⠁⠀⠀⠀⢸⠈⢈⡇⠀⢀⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠩⢠⡴⠀⠀⠀⠀⠀⠈⡶⠉⠀⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠎⢠⣇⠏⠀⠀⠀⠀⠀⠀⠀⠁⠀⢀⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⣿⣴⠀⠀⠀⠀⠀⠀⣆⣀⢾⢟⠴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⠀⠠⣄⠸⢹⣦⠀⠀⡄⠀⠀⢋⡟⠀⠀⠁⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡾⠁⢠⠀⣿⠃⠘⢹⣦⢠⣼⠀⠀⠉⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⢀⣴⠫⠤⣶⣿⢀⡏⠀⠀⠘⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀
⠐⠿⢿⣿⣤⣴⣿⣣⢾⡄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⣨⣟⡍⠉⠚⠹⣇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⢀⡀⣾⡇⠀⠀
⠀⠀⢠⠟⣹⣧⠃⠀⠀⢿⢻⡀⢄⠀⠀⠀⠀⠐⣦⡀⣸⣆⠀⣾⣧⣯⢻⠀⠀
⠀⠀⠘⣰⣿⣿⡄⡆⠀⠀⠀⠳⣼⢦⡘⣄⠀⠀⡟⡷⠃⠘⢶⣿⡎⠻⣆⠀⠀
⠀⠀⠀⡟⡿⢿⡿⠀⠀⠀⠀⠀⠙⠀⠻⢯⢷⣼⠁⠁⠀⠀⠀⠙⢿⡄⡈⢆⠀
⠀⠀⠀⠀⡇⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠀⠀⠀⠀⠀⠀⡇⢹⢿⡀
⠀⠀⠀⠀⠁⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠇⠁

"""

wolf = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠻⣥⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⡿⠻⣆⠙⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠁⠀⠘⣆⡔⢶⣆⠉⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⡿⢿⡀⠉⠀⠞⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡄⠀⡇⠘⣧⣀⣀⣀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠁⢀⣠⠞⣹⢿⠻⡟⢿⣿⣯⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃⠶⠒⠉⠁⣴⠇⢸⡇⡟⡷⢬⡙⠎⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠇⢀⣠⣄⡀⠚⠁⠀⠈⠀⠀⣷⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣽⣿⣶⠋⢉⡿⠇⠀⠀⠀⠀⠀⣰⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣿⣿⠇⠀⣠⣥⣤⡀⠀⠀⠀⢀⡟⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             _____  ._____________    _____   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⢀⣾⡟⠉⢹⡇⠀⠀⠀⢸⠁⡿⠙⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀                            /     \ |   \______   \  /  _  \  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⣇⣾⡟⠀⠸⡏⣄⡀⠀⠀⢹⢀⡇⢀⢘⢿⣮⡙⠀⠀⠀⠀⠀⠀⠀⠀                           /  \ /  \|   ||       _/ /  /_\  \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣇⠀⡀⣧⠰⣿⣶⣄⠀⠀⠀⠘⣎⠳⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀                          /    Y    \   ||    |   \/    |    \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⣆⠹⣿⡐⣾⣷⣹⣆⠀⠀⠀⠘⢷⣄⣻⣿⣿⣷⡄⠀⠀⠀⠀                          \____|__  /___||____|_  /\____|__  / 1.3.1
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣦⠽⣇⣹⣟⢿⠙⠁⠀⠀⠀⣤⠉⠻⣿⣿⣿⣿⣦⡀⠀⠀                                  \/            \/         \/ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⡟⠂⣿⢹⡿⣼⠇⠀⠀⣀⠀⣷⡀⠀⠈⠻⣿⣿⣿⣷⡀⠀                                        Zephyr
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⠀⠉⢸⡇⠈⣀⣠⣾⠇⠀⠻⣿⣦⣤⣴⣿⠿⣿⡿⣷⠀                                        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⡀⠀⢸⠁⣰⠛⣽⡧⠖⠻⢿⡆⠈⠉⠉⠀⠀⢻⣷⠹⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠘⡇⠀⢸⢰⡏⢰⡟⠀⣀⣀⡼⠃⠀⢀⡆⠀⠀⠘⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣶⣷⣶⣾⣿⣧⣾⣤⣄⣀⣀⣤⣤⣶⡿⠀⠀⠀⢠⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣟⡛⠛⠛⠉⠉⠉⠉⢉⣭⣽⡿⠿⠿⠿⠛⠛⠛⠓⠲⠦⠄⣼⢻⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢉⣼⣿⣿⠿⠛⠛⠁⠀⠀⣠⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⣸⡇⠀
⠀⠀⠀⠀⠀⢀⣴⠿⠛⠁⢀⣀⣀⣀⣀⣀⣄⡀⠀⠀⠀⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⣰⣿⠁⠀
⠀⠀⠀⢀⣴⣟⣥⣶⣾⣿⣿⣿⣿⣿⣿⣭⣤⣤⣤⣀⣀⡀⠈⠛⠶⢶⣶⣶⣶⣾⣿⣿⣿⠟⠁⠀⠀
⠀⢀⣴⡿⠟⠋⡽⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀
⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
'''

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from mnemonic import Mnemonic
from mnemonic.mnemonic import ConfigurationError
import base64
import os
import shutil
import stat
import getpass
import argon2
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from secrets import token_bytes
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import re
import time
from password_strength import PasswordPolicy
from datetime import datetime, timedelta
from threading import Thread
from termcolor import colored
import qrcode.constants
from pyotp import TOTP, random_base32
from functools import wraps
import string
from collections import deque
import random
import json
import platform
import logging
import sys
import paramiko
from paramiko.ssh_exception import SSHException
import io
import validators
import uuid
from phonenumbers import carrier
import phonenumbers
import difflib
import requests
import hashlib
import qrcode

def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def get_os_distribution():
    system_info = platform.system()
    if system_info == 'Linux':
        try:
            with open('/etc/os-release', 'r') as f:
                lines = f.readlines()
                distribution_info = {}
                for line in lines:
                    key, value = line.strip().split('=')
                    distribution_info[key] = value.replace('"', '')
                distribution = distribution_info.get('PRETTY_NAME', 'Unknown Distribution')
                version = distribution_info.get('VERSION_ID', 'Unknown Version')
                codename = distribution_info.get('VERSION_CODENAME', 'Unknown Codename')
                base = distribution_info.get('ID_LIKE', 'Unknown Base')
                return f"Linux Distribution: {distribution}\nVersion: {version}\nCodename: {codename}\nBase: {base}\nArchitecture: {platform.architecture()[0]}"
        except FileNotFoundError:
            return "Unable to determine distribution. /etc/os-release file not found."
    elif system_info == 'Darwin':
        version, _, _ = platform.mac_ver()
        return f"macOS Version: {version}\nArchitecture: {platform.architecture()[0]}"
    elif system_info == 'Windows':
        version = platform.version()
        return f"Windows Version: {version}\nArchitecture: {platform.architecture()[0]}"
    else:
        return f"Operating System: {system_info}"
    
def get_python_version():
    return f"Python Version: {platform.python_version()}"

def check_linux_privileges():
    if 'SUDO_UID' in os.environ.keys() or os.getenv('USER') == 'root':
        return True
    return False

def is_admin():
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            return windll.shell32.IsUserAnAdmin()
        except Exception:
            return colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red")
    else:
        return False
    
def check_windows_privileges():
    return is_admin()

def get_current_datetime():
    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%Y-%m-%d")
    time_str = current_datetime.strftime("%H:%M:%S")
    return f"Current Time: {time_str}\nDate: {date_str}"

def move_to_bin():
    if getattr(sys, 'frozen', False):
        current_script = os.path.abspath(sys.executable)
    else:
        current_script = os.path.abspath(__file__)
    target_directory = '/usr/local/bin'
    destination = os.path.join(target_directory, os.path.basename(current_script))
    if os.path.abspath(current_script) == os.path.abspath(destination):
        return
    if not os.path.exists(target_directory):
        print(colored(f"'[-] {target_directory} does not exist.", "red"))
        return
    user_input = input(colored(f"[*] Do you want to use MIRA as a command? (y/N): ", "light_blue")).lower()
    if user_input != 'y':
        print(colored("[-] Abort.", "red"))
        return
    try:
        shutil.move(current_script, destination)
        os.chmod(destination, 0o755)
        print(colored("[+] Now you can launch MIRA by typing 'sudo MIRA'!", "green"))
        time.sleep(3)
    except Exception as e:
        print(colored(f"[-] {e}", "red"))
        return

if os.name == "posix":
    try:
        etc_path = '/etc/'
        data_directory = '.Mira'
        data_directory_path = os.path.join(etc_path, data_directory)
        os.makedirs(data_directory_path, exist_ok=True)
        LOCKOUT_FILE = os.path.join(data_directory_path, '.lockout')
        USER_DATA_FILE = os.path.join(data_directory_path, '.user')
        PASSFILE = os.path.join(data_directory_path, '.pass')
        API = os.path.join(data_directory_path, '.api')
        CARD_PIN_FILE = os.path.join(data_directory_path, '.card')
        SSH = os.path.join(data_directory_path, '.ssh')
        PRIVNOTE = os.path.join(data_directory_path, '.privnote')
        SRCCODE = os.path.join(data_directory_path, '.srccode')
        LOGS = os.path.join(data_directory_path, '.loggings')
        CONFIG_LOGS = os.path.join(data_directory_path, '.configlogs')
        OSPASSFILE = os.path.join(data_directory_path, '.ospassfile')
    except PermissionError:
        print(colored("[-] Mira requires elevated privileges on Linux. QUITTING!", "red"))
        time.sleep(8)
        sys.exit()
elif os.name == "nt":
    try:
        program_files_dir = os.environ.get('ProgramFiles', 'C:\\Program Files')
        app_folder_name = 'Mira'
        app_folder_path = os.path.join(program_files_dir, app_folder_name)
        os.makedirs(app_folder_path, exist_ok=True)
        LOCKOUT_FILE = os.path.join(app_folder_path, 'lockout')
        USER_DATA_FILE = os.path.join(app_folder_path, 'user_data')
        PASSFILE = os.path.join(app_folder_path, 'pass')
        API = os.path.join(app_folder_path, 'api')
        CARD_PIN_FILE = os.path.join(app_folder_path, 'card')
        SSH = os.path.join(app_folder_path, 'ssh')
        PRIVNOTE = os.path.join(app_folder_path, 'notes')
        SRCCODE = os.path.join(app_folder_path, 'srccode')
        LOGS = os.path.join(app_folder_path, 'loggings')
        CONFIG_LOGS = os.path.join(app_folder_path, 'configlogs')
        OSPASSFILE = os.path.join(app_folder_path, 'ospassfile')
    except PermissionError:
        print(colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red"))
        time.sleep(8)
        sys.exit()

class PasswordManager:
    MAX_LOGIN_STR = 20
    MAX_LOGIN_ATTEMPTS = 4 
    LOCKOUT_DURATION_SECONDS = 300

    def __init__(self):
        self.history = InMemoryHistory()
        self.session = PromptSession(history=self.history, auto_suggest=AutoSuggestFromHistory())
        self.master_password = None
        self.cipher = None
        self.ph = PasswordHasher()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename=LOGS, level=logging.INFO, format='%(message)s')
        expiry_thread = Thread(target=self.notify_expiry_background)
        pin_expiry_thread = Thread(target=self.notify_pin_expiry_background)
        pin_expiry_thread.daemon = True
        expiry_thread.daemon = True
        expiry_thread.start()
        pin_expiry_thread.start()
        self.totp_secret_key = None
        self.failed_login_attempts = 0
        self.lockout_time = None
        self.load_lockout_time()
        self.valid_main_menu_commands = ['add_platform_passwd', 'get_platform_passwd', 'ch_platform_passwd', 'del_platform_passwd',
                               'add_os_passwd', 'get_os_passwd', 'ch_os_passwd', 'del_os_passwd',
                               'add_api_key', 'get_api_key', 'ch_api_key', 'del_api_key',
                               'add_card_pin', 'get_card_pin', 'ch_card_pin', 'del_card_pin',
                               'add_ssh_key', 'get_ssh_key', 'ch_ssh_key', 'del_ssh_key',
                               'add_src_code', 'get_src_code', 'ch_src_code', 'del_src_code',
                               'add_priv_note', 'get_priv_note', 'ch_priv_note', 'del_priv_note',
                               'enable2fa', 'genpasswd', 'changemaster',
                               'show_passwd_exp', 'show_passwd_strength', 'show_pin_exp', 'show_api_key', 'show_ssh_key', 'show_src_code', 'show_priv_note', 'show_os_passwd'
                               'mnemonic_enc_key', 'dec_mnemonic',
                               'check_my_passwd_if_pwned', 'show_loggings', 'show_config_loggings', 'lout', 'exit', 'reset', 'about', 'help']
        self.valid_login_commands = ['regis', 'log', 'dec_mnemonic', 'about', 'quit', 'help']
        self.card_patterns = {
            "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
            "Mastercard": r"^5[1-5][0-9]{14}$",
            "American Express": r"^3[47][0-9]{13}$",
            "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
            "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
            "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
            "Maestro": r"^(5018|5020|5038|56|57|58|6304|6759|676[1-3])\d{8,15}$",
            "Verve": r"^(506[01]|507[89]|6500)\d{12,15}$",
        }

    def save_lockout_time(self):
        if self.lockout_time:
            lockout_data = {'lockout_time': self.lockout_time}
            with open(LOCKOUT_FILE, 'w') as lockout_file:
                json.dump(lockout_data, lockout_file)

    def load_lockout_time(self):
        try:
            with open(LOCKOUT_FILE, 'r') as lockout_file:
                lockout_data = json.load(lockout_file)
                self.lockout_time = lockout_data.get('lockout_time')
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def increment_failed_attempts(self):
        if self.lockout_time and time.time() < self.lockout_time:
            print(colored(blehhh, "red"))
            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(self.lockout_time - time.time())} seconds.", "red"))
            time.sleep(8)
            sys.exit()
            return False
        self.failed_login_attempts += 1
        if self.failed_login_attempts >= self.MAX_LOGIN_ATTEMPTS:
            self.lockout_time = time.time() + self.LOCKOUT_DURATION_SECONDS
            self.save_lockout_time()
            print(colored(blehhh, "red"))
            print(colored(f"[-] Account locked. Too many failed login attempts. Account locked for {self.LOCKOUT_DURATION_SECONDS} seconds.", "red"))
            time.sleep(8)
            sys.exit()
            return False
        return True

    def generate_master_password(self, length=15, num_upper=3, num_lower=4, num_digits=3, num_symbols=5):
        upper_chars = ''.join(random.choices(string.ascii_uppercase, k=num_upper))
        lower_chars = ''.join(random.choices(string.ascii_lowercase, k=num_lower))
        digit_chars = ''.join(random.choices(string.digits, k=num_digits))
        symbol_chars = ''.join(random.choices(string.punctuation, k=num_symbols))
        all_chars = upper_chars + lower_chars + digit_chars + symbol_chars
        remaining_length = length - (num_upper + num_lower + num_digits + num_symbols)
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))
        password = upper_chars + lower_chars + digit_chars + symbol_chars + remaining_chars
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        return password
    
    def generate_password(self, length=10, num_upper=2, num_lower=3, num_digits=3, num_symbols=2):
        upper_chars = ''.join(random.choices(string.ascii_uppercase, k=num_upper))
        lower_chars = ''.join(random.choices(string.ascii_lowercase, k=num_lower))
        digit_chars = ''.join(random.choices(string.digits, k=num_digits))
        symbol_chars = ''.join(random.choices(string.punctuation, k=num_symbols))
        all_chars = upper_chars + lower_chars + digit_chars + symbol_chars
        remaining_length = length - (num_upper + num_lower + num_digits + num_symbols)
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))
        password = upper_chars + lower_chars + digit_chars + symbol_chars + remaining_chars
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        return password
    
    def check_password_pwned(self, password):
        try:
            sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            prefix = sha1_password[:5]
            suffix = sha1_password[5:]
            response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
            response.raise_for_status()
            if response.status_code == 200:
                hashes = (line.split(':') for line in response.text.splitlines())
                for h, count in hashes:
                    if h == suffix:
                        return {
                            'status': 'found',
                            'sha1_hash': sha1_password.lower(),
                            'breach_count': int(count),
                            'message': '[!] Password found in breaches. It is strongly recommended to change this password immediately.'
                        }
                return {
                    'status': 'not_found',
                    'sha1_hash': sha1_password.lower(),
                    'breach_count': 0,
                    'message': '[+] Password not found in any breaches.'
                }
        except requests.ConnectionError:
            return {
                'status': 'error',
                'message': '[-] Connection Error: Unable to connect to the internet. Please check your internet connection.'
            }
        except requests.HTTPError as http_err:
            return {
                'status': 'error',
                'message': f'[-] HTTP error occured: {http_err}'
            }
        except requests.Timeout:
            return {
                'status': 'error',
                'message': '[-] Request timed out: The request took too long to complete. Try again later.'
            }
        except Exception as err:
            return {
                'status': 'error',
                'message': f'[-] An unexpected error occurred: {err}'
            }

    def enable_2fa(self):
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        if user_data.get('2fa_enabled', False):
            print(colored("[-] 2FA is already enabled! QR Code cannot be displayed!", "red"))
            return
        self.totp_secret_key = random_base32()
        key = self.encrypt_information(self.totp_secret_key)
        user_data['2fa_enabled'] = True
        user_data['key'] = key
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(user_data, file)
        totp = TOTP(self.totp_secret_key)
        #accusn = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        accusn = self.get_username_log(self.login_username)
        otp_auth_url = totp.provisioning_uri(name=accusn, issuer_name="MIRA (Veilwr4ith)")
        genqr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=1, border=1)
        genqr.add_data(otp_auth_url)
        genqr.make(fit=True)
        print(colored("[+] 2FA Enabled. Scan the QR Code using your authenticator app. After scanning, you will be prompted to enter a 6-digit code to successfully log in.", "green"))
        qr_ascii = genqr.print_ascii()
        print(colored("[!] Warning: If the terminal is cleared, the QR code cannot be displayed. So scan it immediately with your authenticator app.", "yellow"))
    
    def verify_2fa(self, secret_key, code):
        totp = TOTP(secret_key)
        return totp.verify(code)
    
    def notify_expiry_background(self):
        while True:
            try:
                self.notify_expiry()
            except FileNotFoundError:
                pass
            time.sleep(86400)
    
    def notify_expiry(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            for entry in data:
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    time_left = expiry_date - datetime.now()
                    if timedelta(days=1) <= time_left <= timedelta(days=7):
                        days_left = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        print(colored(f"[!] Warning: Some of your passwords will expire in {days_left} days, {hours} hours, {minutes} minutes, and {seconds} seconds. Please update them!", 'yellow'))
                    elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                        print(colored(f"[!!] Alert: Some of your passwords will expire in any minute! Please update them!", 'magenta'))
                    elif time_left <= timedelta(seconds=0):
                        print(colored(f"[!!!] Alert: Some of your passwords has expired. Update is now mandatory for accessibility!", 'red'))
        except FileNotFoundError:
            pass
    
    def notify_pin_expiry_background(self):
        while True:
            try:
                self.notify_pin_expiry()
            except FileNotFoundError:
                pass
            time.sleep(86400)
    
    def notify_pin_expiry(self):
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
            for entry in data:
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    time_left = expiry_date - datetime.now()
                    if timedelta(days=1) <= time_left <= timedelta(days=7):
                        days_left = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        print(colored(f"[!] Warning: Some of your PINs will expire in {days_left} days, {hours} hours, {minutes} minutes, and {seconds} seconds. Please update them!", 'yellow'))
                    elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                        print(colored(f"[!!] Alert: Some of your PINs will expire in any minute! Please update them!", 'magenta'))
                    elif time_left <= timedelta(seconds=0):
                        print(colored(f"[!!!] Alert: Some of your PINs has expired. Update is now mandatory for accessibility!", 'red'))
        except FileNotFoundError:
            pass
    
    def load_encryption_key(self, encryption_key):
        self.cipher = self.initialize_cipher(encryption_key)
    
    def initialize_cipher(self, key):
        return Fernet(key)
    
    def check_master_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=15,
            uppercase=3,
            numbers=3,
            special=5,
        )
        result = policy.test(password)
        if result:
            print(colored("[-] Master password is not strong enough (Not Added). Please follow our password policy for master password:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))
            generate_strong_pass = input(colored("[*] Do you want Mira to generate a strong master password for you> (y/N): ", "light_blue"))
            if generate_strong_pass.lower() == 'y':
                generate_master_password = self.generate_master_password()
                print(colored(f"[+] Generated Password: {colored(generate_master_password, 'green')}", "light_yellow"))
                return False
            else:
                return False
        return True
    
    def check_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=10,
            uppercase=2,
            numbers=3,
            special=2,
        )
        result = policy.test(password)
        if result:
            print(colored("[-] Password is not strong enough:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))
            user_choice = input(colored("[*] Do you want to use this password anyway? (y/N): ", "light_blue"))
            if user_choice.lower() == 'y':
                return True
            else:
                generate_strong_pass = input(colored("[*] Do you want Mira to generate a strong password for you? (y/N): ", "yellow"))
                if generate_strong_pass.lower() == 'y':
                    generate_password = self.generate_password()
                    print(colored(f"[+] Generated Password: {colored(generate_password, 'green')}", "light_yellow"))
                    return False
                else:
                    print(colored("[-] Abort.", "red"))
                    return False
        return True
    
    def register(self, username, master_password):
        if not self.check_master_password_strength(master_password):
            return
        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
            print(colored("[-] Master user already exists!!", "red"))
        else:
            self.master_password = master_password
            salt = token_bytes(100)
            salt_hex = salt.hex()
            saltier = token_bytes(300)
            saltier_hex = salt.hex()
            saltiest = token_bytes(1000)
            saltiest_hex = salt.hex()
            hashed_master_password = self.ph.hash(master_password + saltier_hex)
            hashed_username = self.ph.hash(username + salt_hex)
            encryption_key = Fernet.generate_key()
            fernet = Fernet(encryption_key) 
            encrypted_master_password = fernet.encrypt(hashed_master_password.encode())
            encrypted_username = fernet.encrypt(hashed_username.encode())
            encrypted_username_b64 = base64.b64encode(encrypted_username).decode()
            encrypted_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
            ph = argon2.PasswordHasher()
            hashed_encryption_key = ph.hash(encryption_key.decode() + saltiest_hex)
            user_data = {
                '2328131181237': saltiest_hex,
                '3223245431342': encrypted_username_b64,
                '3543645771234': salt_hex,
                '9034374927023': encrypted_master_password_b64,
                '4017916987192': hashed_encryption_key,
                '2104941992374': saltier_hex
            }
            with open(USER_DATA_FILE, 'w') as file:
                json.dump(user_data, file)
                clear_terminal()
                print(colored(wolf, "blue"))
                print(colored("\n[+] Registration complete!!", "green"))
                print(colored(f"[+] Encryption key: {colored(encryption_key.decode(), 'green')}", "light_yellow"))
                print(colored("\n[!] Caution: Save your encryption key and store it somewhere safe Mira will never recover your encryption key once you forgot it!", "yellow"))
    
    def get_username_log(self, uname):
        return uname
    
    def log_login_attempt(self, login_status):
        try:
            with open(LOGS, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        log_entry = {
            'time': time.strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'Success' if login_status else 'Failed',
            'entered_username': self.get_username_log(login_username)
        }
        if len(data)>= PasswordManager.MAX_LOGIN_STR:
            data = data[5:]
        data.append(log_entry)
        with open(LOGS, 'w') as file:
            json.dump(data, file, indent=4)
        if login_status:
            pass
        else:
            pass
    
    def login(self, username, entered_password, encryption_key):
        if not os.path.exists(USER_DATA_FILE):
            print(colored("\n[-] You have not registered. Do that first!", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        if self.lockout_time and time.time() < self.lockout_time:
            clear_terminal()
            print(colored(blehhh, "red"))
            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(self.lockout_time - time.time())} seconds.", "red"))
            exit()
            return
        stored_encryption_key = user_data.get('4017916987192', '')
        ph = PasswordHasher()
        try:
            if not ph.verify(stored_encryption_key, encryption_key + user_data.get('2328131181237', '')):
                raise VerifyMismatchError("Encryption key mismatch")
        except VerifyMismatchError:
            print(colored("[-] Invalid Login Credentials. Login Failed!", "red"))
            self.log_login_attempt(False)
            if self.increment_failed_attempts():
                return
            else:
                return
        self.load_encryption_key(encryption_key.encode())
        fernet = Fernet(encryption_key)
        decrypted_username = fernet.decrypt(base64.b64decode(user_data.get('3223245431342', ''))).decode()
        decrypted_master_password = fernet.decrypt(base64.b64decode(user_data.get('9034374927023', ''))).decode()
        try:
            self.ph.verify(decrypted_username, username + user_data.get('3543645771234', ''))
            self.ph.verify(decrypted_master_password, entered_password + user_data.get('2104941992374', ''))
            if '2fa_enabled' in user_data and user_data['2fa_enabled']:
                key = self.decrypt_information(user_data['key'])
                code = getpass.getpass(colored("[*] 6-Digit Code (2FA): ", "light_blue")) 
                if not self.verify_2fa(key, code):
                    print(colored("[-] Invalid 2FA Code. Login Failed!", "red"))
                    self.log_login_attempt(False)
                    if self.increment_failed_attempts():
                        return
                    else:
                        return
            print(colored("[+] Login Successful..", "green"))
            print(colored("[..] Proceeding....", "light_cyan"))
            self.log_login_attempt(True)
            time.sleep(10)
            clear_terminal()
            print(colored(wolf, "blue"))
            self.login_username = login_username
            self.master_password = entered_password
            self.main_menu()
        except VerifyMismatchError:
            print(colored("[-] Invalid Login Credentials. Login Failed!", "red"))
            self.log_login_attempt(False)
            if self.increment_failed_attempts():
                return
            else:
                return
    
    def log_changes_event(self, account_id, category, action, status):
        log_entry = {
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "account_id": str(account_id),
            "category": category,
            "action": action,
            "status": status
        }
        if os.path.exists(CONFIG_LOGS):
            with open(CONFIG_LOGS, 'r') as file:
                log_data = json.load(file)
        else:
            log_data = []
        log_data.append(log_entry)
        with open(CONFIG_LOGS, 'w') as file:
            json.dump(log_data, file, indent=4)
    
    def find_similar_main_menu_command(self, user_input):
        close_matches = difflib.get_close_matches(user_input, self.valid_main_menu_commands, cutoff=0.5)
        if close_matches:
            return close_matches[0]
        else:
            return None
    
    def find_similar_login_command(self, user_input):
        close_matches = difflib.get_close_matches(user_input, self.valid_login_commands, cutoff=0.5)
        if close_matches:
            return close_matches[0]
        else:
            return None
    
    def show_loggings(self):
        try:
            with open(LOGS, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    key_status = []
                    for entry in data:
                        key_status.append({
                            'time': entry['time'],
                            'status': entry['status'],
                            'username': entry['entered_username']
                        })
                elif isinstance(data, dict): 
                    key_status = [{
                        'time': data['time'],
                        'status': data['status'],
                        'username': data['entered_username']
                    }]
                else:
                    raise ValueError("Invalid JSON format")
                if key_status:
                    print(colored("[+] All Previous Logs:", "green"))
                    print(colored("\nTime Logged".ljust(31) + "Status".ljust(24) + "Entered Username", "cyan"))
                    print(colored("--------------------".ljust(30) + "-------------".ljust(24) + "--------------------", "cyan"))
                    for user_status in key_status:
                        if user_status['status'] == "Success":
                            status_color = 'green'
                        else:
                            status_color = 'red'
                        print(f"{colored(str(user_status['time']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(24), status_color)}{colored(str(user_status['username']), 'cyan')}")
                else:
                    print(colored("[-] No Logs has been found.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Logs has been found.", "red"))
    
    def show_config_loggings(self):
        try:
            with open(CONFIG_LOGS, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    key_status = []
                    for entry in data:
                        key_status.append({
                            'time': entry['time'],
                            'ID': entry['account_id'],
                            'category': entry['category'],
                            'action': entry['action'],
                            'status': entry['status']
                        })
                elif isinstance(data, dict): 
                    key_status = [{
                        'time': entry['time'],
                        'ID': entry['account_id'],
                        'category': entry['category'],
                        'action': entry['action'],
                        'status': entry['status']
                    }]
                else:
                    raise ValueError("Invalid JSON format")
                if key_status:
                    print(colored("[+] All Previous Configuration Logs:", "green"))
                    print(colored("\nTime Configured".ljust(29) + "ID".ljust(22) + "Category".ljust(26) + "Action".ljust(24) + "Status", "cyan"))                  
                    print(colored("-------------------".ljust(28) + "-------------".ljust(22) + "-----------------".ljust(26) + "-------------".ljust(24) + "-------------", "cyan"))
                    for user_status in key_status:
                        if user_status['status'] == "Success":
                            status_color = 'green'
                        else:
                            status_color = 'red'
                        print(f"{colored(str(user_status['time']).ljust(28), 'cyan')}{colored(str(user_status['ID']).ljust(22), 'cyan')}{colored(str(user_status['category']).ljust(26), 'cyan')}{colored(str(user_status['action']).ljust(24), 'cyan')}{colored(str(user_status['status']).ljust(23), status_color)}")
                else:
                    print(colored("[-] No Configuration Logs has been found.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Logs has been found.", "red"))
    
    def show_ssh_key(self):
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
            key_id = input(colored("[*] Key ID: ", "light_blue"))
            if key_id.isdigit():
                key_id = int(key_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['key_id'] == key_id or (isinstance(key_id, str) and key_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'key_id': entry['key_id'],
                        'username': self.decrypt_information(entry['username']),
                        'key_name': self.decrypt_information(entry['key_name']),
                        'added_at': added_at,
                        'password_protected': entry['password_protected']
                    })
            if key_status:
                if key_id == 'all' or not key_id:
                    print(colored("[+] All Available SSH Keys:", "green"))
                    print(colored("\nKey ID".ljust(23) + "Username".ljust(30) + "SSH Key Name".ljust(30) + "Added At".ljust(30) + "Passphrase-Protected", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "--------------------".ljust(30) + "-------------------".ljust(30) + "--------------------", "cyan"))
                    for user_status in key_status:
                        if user_status['password_protected'] == "True":
                            status_color = 'green'
                        else:
                            status_color = 'red'
                        print(f"{colored(str(user_status['key_id']).ljust(22), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['key_name']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(30), 'cyan')}{colored(str(user_status['password_protected']), status_color)}")
                else:
                    print(colored(f"[+] Info about this Key ID {key_id}:", "green"))
                    print(colored("\nUsername".ljust(28) + "SSH Key Name".ljust(29) + "Added At".ljust(29) + "Passphrase-Protected", "cyan"))
                    print(colored("--------------------".ljust(27) + "--------------------".ljust(29) + "-------------------".ljust(29) + "--------------------", "cyan"))
                    for user_status in key_status:
                        if user_status['password_protected'] == "True":
                            status_color = 'green'
                        else:
                            status_color = 'red'
                        print(f"{colored(str(user_status['username']).ljust(27), 'cyan')}{colored(str(user_status['key_name']).ljust(29), 'cyan')}{colored(str(user_status['added_at']).ljust(29), 'cyan')}{colored(str(user_status['password_protected']), status_color)}")
            else:
                print(colored("[-] No matching entries found for the specified Key ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No SSH Key saved. Show SSH Keys failed!", "red"))
    
    def show_src_code_status(self):
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
            code_id = input(colored("[*] Code ID: ", "light_blue"))
            if code_id.isdigit():
                code_id = int(code_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['code_id'] == code_id or (isinstance(code_id, str) and code_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'code_id': entry['code_id'],
                        'language': self.decrypt_information(entry['language']),
                        'filename': self.decrypt_information(entry['filename']),
                        'added_at': added_at
                    })
            if key_status:
                if code_id == 'all' or not code_id:
                    print(colored("[+] All Available Source Codes:", "green"))
                    print(colored("\nCode ID".ljust(23) + "Programming Language".ljust(32) + "File Name".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "-------------------------".ljust(32) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['code_id']).ljust(22), 'cyan')}{colored(str(user_status['language']).ljust(32), 'cyan')}{colored(str(user_status['filename']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Code ID {code_id}:", "green"))
                    print(colored("\nProgramming Language".ljust(32) + "File Name".ljust(27) + "Added At", "cyan"))
                    print(colored("-------------------------".ljust(31) + "--------------------".ljust(27) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['language']).ljust(31), 'cyan')}{colored(str(user_status['filename']).ljust(27), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
            else:    
                print(colored("[-] No matching entries found for the specified Code ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Source Code saved. Show Source Code failed!", "red"))
    
    def show_api_key(self):
        try:
            with open(API, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "light_blue"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['unique_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'unique_id': entry['unique_id'],
                        'platform': self.decrypt_information(entry['platform']),
                        'username': self.decrypt_information(entry['key_name']),
                        'added_at': added_at
                    })
            if key_status:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available API Keys:", "green"))
                    print(colored("\nAccount ID".ljust(23) + "Platform".ljust(30) + "API Key Name".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['unique_id']).ljust(22), 'cyan')}{colored(str(user_status['platform']).ljust(30), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(28) + "API Key Name".ljust(30) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['platform']).ljust(27), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['added_at'].ljust(25)), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No API Key saved. Show API Key failed!", "red"))

    def show_os_passwd_status(self):
        try:
            with open(OSPASSFILE, 'r') as file:
                data = json.load(file)
            os_id = input(colored("[*] OS ID: ", "light_blue"))
            if os_id.isdigit():
                os_id = int(os_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['account_id'] == os_id or (isinstance(os_id, str) and os_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'os_id': entry['account_id'],
                        'operating_system': self.decrypt_information(entry['operating_system']),
                        'password_type': self.decrypt_information(entry['password_type']),
                        'username': self.decrypt_information(entry['username']),
                        'added_at': added_at
                    })
            if key_status:
                if os_id == 'all' or not os_id:
                    print(colored("[+] All Available OS Passwords:", "green"))
                    print(colored("\nOS ID".ljust(17) + "Operating System".ljust(26) + "Password Type".ljust(20) + "Username".ljust(26) + "Added At", "cyan"))
                    print(colored("----------".ljust(16) + "--------------------".ljust(26) + "---------------".ljust(20) + "--------------------".ljust(26) + "--------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['os_id']).ljust(16), 'cyan')}{colored(str(user_status['operating_system']).ljust(26), 'cyan')}{colored(str(user_status['password_type']).ljust(20), 'cyan')}{colored(str(user_status['username']).ljust(26), 'cyan')}{colored(str(user_status['added_at']), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this OS ID {os_id}:", "green"))
                    print(colored("\nOperating System".ljust(26) + "Password Type".ljust(22) + "Username".ljust(26) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(25) + "---------------".ljust(22) + "--------------------".ljust(26) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['operating_system']).ljust(25), 'cyan')}{colored(str(user_status['password_type']).ljust(22), 'cyan')}{colored(str(user_status['username']).ljust(26), 'cyan')}{colored(str(user_status['added_at']), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified OS ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No OS Passwords saved. Show OS Passwords failed!", "red"))

    def show_priv_note_status(self):
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
            note_id = input(colored("[*] Note ID: ", "light_blue"))
            if note_id.isdigit():
                note_id = int(note_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['note_id'] == note_id or (isinstance(note_id, str) and note_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'note_id': entry['note_id'],
                        'title': self.decrypt_information(entry['title']),
                        'added_at': added_at
                    })
            if key_status:
                if note_id == 'all' or not note_id:
                    print(colored("[+] All Available Notes:", "green"))
                    print(colored("\nNote ID".ljust(23) + "Title".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['note_id']).ljust(22), 'cyan')}{colored(str(user_status['title']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Note ID {note_id}:", "green"))
                    print(colored("\nTitle".ljust(28) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['title']).ljust(27), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Note ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Private Notes saved. Show Private Notes failed!", "red"))
    
    def show_pin_expiry_status(self):
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
            card_id = input(colored("[*] Card ID: ", "light_blue"))
            if card_id.isdigit():
                card_id = int(card_id)
            else:
                pass
            card_status = []
            for entry in data:
                if entry['card_id'] == card_id or (isinstance(card_id, str) and card_id.lower() == 'all'):
                    expiry_status, remaining_time = self.check_expiry_status(entry.get('expiry_at'))
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    expiry_at = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    card_status.append({
                        'card_id': entry['card_id'],
                        'card_brand': self.decrypt_information(entry['card_brand']),
                        'card_type': self.decrypt_information(entry['card_type']),
                        'card_number': self.decrypt_information(entry['card_number']),
                        'status': expiry_status,
                        'added_at': added_at,
                        'expiry_at': expiry_at,
                        'remaining_time': remaining_time
                    })
            if card_status:
                if card_id == 'all' or not card_id:
                    print(colored("[+] All Available Card IDs:", "green"))
                    print(colored("\nCard ID".ljust(16) + "Card Brand".ljust(26) + "Card Type".ljust(21) + "Card Number".ljust(30) + "Status".ljust(20) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(15) + "--------------------".ljust(26) + "----------".ljust(21) + "--------------------".ljust(30) + "----------".ljust(20) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in card_status:
                        print(f"{colored(str(user_status['card_id']).ljust(15), 'cyan')}{colored(str(user_status['card_brand']).ljust(26), 'cyan')}{colored(str(user_status['card_type']).ljust(21), 'cyan')}{colored(str(user_status['card_number']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(29), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(25), 'cyan')}{colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
                else:
                    print(colored("[+] All Available Card IDs:", "green"))
                    print(colored("\nCard ID".ljust(16) + "Card Brand".ljust(26) + "Card Type".ljust(21) + "Card Number".ljust(30) + "Status".ljust(20) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(15) + "--------------------".ljust(26) + "----------".ljust(21) + "--------------------".ljust(30) + "----------".ljust(20) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in card_status:
                        print(f"{colored(str(user_status['card_id']).ljust(15), 'cyan')}{colored(str(user_status['card_brand']).ljust(26), 'cyan')}{colored(str(user_status['card_type']).ljust(21), 'cyan')}{colored(str(user_status['card_number']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(29), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(25), 'cyan')}{colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Card ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No PIN saved. Show expiry status failed!", "red"))
    
    def show_passwd_strength(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "light_blue"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            passwd_strength = []
            for entry in data:
                if entry['account_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    password = self.decrypt_password(entry['password'])
                    strength = self.check_password_strngth(password)
                    passwd_strength.append({
                        'acc_id': entry['account_id'],
                        'website': self.decrypt_information(entry['website']),
                        'username': self.decrypt_information(entry['username']),
                        'strength': strength
                    })
            if passwd_strength:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available Users:", "green"))
                    print(colored("\nAccount ID".ljust(25) + "Platform".ljust(31) + "Username".ljust(30) + "Strength", "cyan"))
                    print(colored("----------".ljust(24) + "--------------------".ljust(31) + "--------------------".ljust(30) + "----------", "cyan"))
                    for user_status in passwd_strength:
                        print(f"{colored(str(user_status['acc_id']).ljust(24), 'cyan')}{colored(str(user_status['website']).ljust(31), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['strength']), 'cyan')}")
                else:
                    print(colored(f"[+] Password Strength of this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(29) + "Username".ljust(31) + "Strength", "cyan"))
                    print(colored("--------------------".ljust(28) + "--------------------".ljust(31) + "----------", "cyan"))
                    for user_status in passwd_strength:
                        print(f"{colored(str(user_status['website']).ljust(28), 'cyan')}{colored(str(user_status['username']).ljust(31), 'cyan')}{str(user_status['strength'])}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Show password strength failed!", "red"))
    
    def check_password_strngth(self, password):
        is_length_valid = len(password) >= 10
        uppercase_count = sum(1 for char in password if char.isupper())
        lowercase_count = sum(1 for char in password if char.islower())
        digit_count = sum(1 for char in password if char.isdigit())
        special_char_count = sum(1 for char in password if not char.isalnum())
        has_required_uppercase = uppercase_count >= 2
        has_required_lowercase = lowercase_count >= 3
        has_required_digits = digit_count >= 3
        has_required_special_chars = special_char_count >= 2
        conditions_met = [is_length_valid, has_required_uppercase, has_required_lowercase, has_required_digits, has_required_special_chars]
        num_conditions_met = sum(conditions_met)
        if num_conditions_met == 5:
            return colored("Strong", "green")
        elif num_conditions_met >= 3:
            return colored("Moderate", "yellow")
        else:
            return colored("Weak", "red")
    
    def show_expiry_status(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "light_blue"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            usernames_status = []
            for entry in data:
                if entry['account_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    expiry_status, remaining_time = self.check_expiry_status(entry.get('expiry_at'))
                    website = self.decrypt_information(entry['website'])
                    username = self.decrypt_information(entry['username'])
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    expiry_at = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    usernames_status.append({
                        'account_id': entry['account_id'],
                        'website': website,
                        'username': username,
                        'status': expiry_status,
                        'added_at': added_at,
                        'expiry_at': f"{expiry_at}",
                        'remaining_time': remaining_time
                    })
            if usernames_status:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available Platforms:", "green"))
                    print(colored("\nAccount ID".ljust(15) + "Platform".ljust(25) + "Username".ljust(25) + "Status".ljust(21) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(14) + "--------------------".ljust(25) + "--------------------".ljust(25) + "----------".ljust(21) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in usernames_status:
                        print(f"{colored(str(user_status['account_id']).ljust(14), 'cyan')}{colored(str(user_status['website']).ljust(25), 'cyan')}{colored(str(user_status['username']).ljust(25), 'cyan')}{str(user_status['status']).ljust(30)}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(24), 'cyan')} {colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
                else:
                    print(colored(f"[+] Status of this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(26) + "Username".ljust(24) + "Status".ljust(21) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("--------------------".ljust(25) + "--------------------".ljust(24) + "----------".ljust(21) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in usernames_status:
                        print(f"{colored(user_status['website'].ljust(25), 'cyan')}{colored(user_status['username'].ljust(24), 'cyan')}{user_status['status'].ljust(30)}{colored(user_status['added_at'].ljust(25), 'cyan')}{colored(user_status['expiry_at'].ljust(24), 'cyan')} {colored(user_status['remaining_time'].ljust(30), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Show expiry status failed!", "red"))
    
    def check_expiry_status(self, expiry_date):
        if expiry_date:
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d %H:%M:%S")
            time_left = expiry_date - datetime.now()
            if timedelta(days=1) <= time_left <= timedelta(days=7):
                return colored("Nearly Expired", "yellow"), str(time_left)
            elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                return colored("About to Expire", "magenta"), str(time_left)
            elif time_left <= timedelta(seconds=0):
                return colored("Expired", "red"), colored("00:00:00.000000", "red")
            else:
                days_left = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                remaining_time = f"{days_left} days, {hours} hours, {minutes} minutes, {seconds} seconds"
                return colored("Updated", "green"), str(time_left)
        return "OK", "N/A"
    
    def main_menu(self):
        login_username = self.get_username_log(self.login_username)
        prompt = True
        while prompt:
            prompt = HTML(f"<ansiblue>{login_username}@MIRA ~> </ansiblue>")
            choice = self.session.prompt(prompt)
            if choice == "":
                continue

            elif choice == 'add_platform_passwd':
                website = input(colored("[*] Platform: ", "light_blue"))
                if not validators.url(website):
                    print(colored("[-] The format you've entered is Invalid! Please make sure that it's in URL form.", "red"))
                    continue
                email_or_phone = input(colored("[*] Email Address/Phone(CC): ", "light_blue"))
                if not (validators.email(email_or_phone) or self.validate_phone_number(email_or_phone)):
                    print(colored("[-] The Email/Phone you've entered is Invalid!", "red"))
                    continue
                username = input(colored("[*] Username: ", "light_blue"))
                if not username:
                    print(colored("[-] No username provided!", "red"))
                    continue
                password = getpass.getpass(colored("[*] Password: ", "light_blue"))
                if not password:
                    print(colored("[-] No password provided!", "red"))
                    continue
                re_enter = getpass.getpass(colored("[*] Re-Enter Password: ", "light_blue"))
                if re_enter != password:
                    print(colored("[-] Password did not match! QUITTING!", "red"))
                else:
                    self.add_password(website, email_or_phone, username, password)
                    self.notify_expiry()
                    self.notify_pin_expiry()

            elif choice == 'add_os_passwd':
                operating_system = input(colored("[*] Operating System: ", "light_blue")).lower()
                if operating_system not in ['windows', 'mac', 'linux', 'android', 'ios']:
                    print(colored("[-] Invalid Operating System or Not Supported Operating System!", "red"))
                    continue
                if operating_system == 'ios':
                    formatted_operating_system = operating_system.upper()
                else:
                    formatted_operating_system = operating_system.title()
                password_type = input(colored("[*] Password Type: ", "light_blue")).lower()
                if password_type not in ['pattern', 'phrase', 'pin']:
                    print(colored("[-] Invalid Password Type or Not Supported!", "red"))
                    continue
                if password_type == 'pin':
                    formatted_password_type = password_type.upper()
                else:
                    formatted_password_type = password_type.title()
                if formatted_password_type == 'Phrase':
                    username = input(colored("[*] Username: ", "light_blue"))
                    if not username:
                        print(colored("[-] No username provided!", "red"))
                        continue
                    password = getpass.getpass(colored("[*] OS Phrase Password: ", "light_blue"))
                    if not password:
                        print(colored("[-] No OS Phrase password provided!", "red"))
                        continue
                    re_enter = getpass.getpass(colored("[*] Re-Enter OS Phrase Password: ", "light_blue"))
                    if re_enter != password:
                        print(colored("[-] OS Password did not match! QUITTING!", "red"))
                        continue
                elif formatted_password_type == 'PIN':
                    username = input(colored("[*] Username: ", "light_blue"))
                    if not username:
                        print(colored("[-] No username provided!", "red"))
                        continue
                    password = getpass.getpass(colored("[*] OS PIN Password: ", "light_blue"))
                    if password.isdigit():
                        if not password:
                            print(colored("[-] No OS PIN password provided!", "red"))
                            continue
                        re_enter = getpass.getpass(colored("[*] Re-Enter OS PIN Password: ", "light_blue"))
                        if re_enter != password:
                            print(colored("[-] OS PIN Password did not match! QUITTING!", "red"))
                            continue
                    else:
                        print(colored("[-] Invalid! PIN should be numeric.", "red"))
                        continue
                elif formatted_password_type == 'Pattern':
                    username = input(colored("[*] Username: ", "light_blue"))
                    if not username:
                        print(colored("[-] No username provided!", "red"))
                        continue
                    password = getpass.getpass(colored("[*] Describe the pattern of your OS Password: ", "light_blue"))
                    if not password:
                        print(colored("[-] No Description for OS password provided!", "red"))
                        continue
                self.add_os_password(formatted_operating_system, formatted_password_type, username, password)
                self.notify_expiry()
                self.notify_pin_expiry()

            elif choice == 'get_os_passwd':
                try:
                    acc_id = int(input(colored("[*] OS ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid OS ID.", "red"))
                    continue
                decrypted_os_password = self.get_os_password(acc_id)
                try:
                    with open(OSPASSFILE, 'r') as file:
                        data = json.load(file)
                    account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
                    if not account_entry:
                        print(colored(f"[-] OS ID {acc_id} not found.", "red"))
                        continue
                    if decrypted_os_password is not None:
                        print(colored(f"[+] Operating System: {colored(self.decrypt_information(account_entry['operating_system']), 'green')}", "light_yellow"))
                        print(colored(f"[+] Password Type: {colored(self.decrypt_information(account_entry['password_type']), 'green')}", "light_yellow"))
                        print(colored(f"[+] Username: {colored(self.decrypt_information(account_entry['username']), 'green')}", "light_yellow"))
                        print(colored(f"[+] Password: {colored(decrypted_os_password, 'green')}", "light_yellow"))
                        self.notify_expiry()
                        self.notify_pin_expiry()
                except FileNotFoundError:
                    print(colored("[-] No passwords have been saved yet. Retrieve passwords failed!", "red"))
                    continue

            elif choice == 'get_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid account ID.", "red"))
                    continue
                decrypted_password = self.get_password(acc_id)
                try:
                    with open(PASSFILE, 'r') as file:
                        data = json.load(file)
                    account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
                    if not account_entry:
                        print(colored(f"[-] Account ID {acc_id} not found.", "red"))
                        continue
                    if 'expiry_at' in account_entry and account_entry['expiry_at']:
                        expiry_date = datetime.strptime(account_entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                        if datetime.now() > expiry_date:
                            response = input(colored("[*] Password has expired. Do you want to update the password or delete the account for this platform? (U/D): ", "light_blue")).lower()
                            if response == 'u':
                                username = self.decrypt_information(account_entry['username'])
                                current_password = getpass.getpass(colored(f"[*] Current password for account ID {acc_id} (Username: {username}): ", "light_blue"))
                                if current_password != self.decrypt_password(account_entry['password']):
                                    print(colored("[-] Incorrect current password. Update password failed!", "red"))
                                    self.log_changes_event(acc_id, "Platform Password", "Update", "Failed")
                                    continue
                                new_password = getpass.getpass(colored("[*] New Password: ", "light_blue"))
                                re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "light_blue"))
                                if new_password != re_enter:
                                    print(colored("[-] Passwords did not match! Update password failed.", "red"))
                                    continue
                                if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                                    print(colored("[-] Password has been used. Avoid reusing passwords! Update password failed.", "red"))
                                    self.log_changes_event(acc_id, "Platform Password", "Update", "Failed")
                                    continue
                                if not self.check_password_strength(new_password):
                                    print(colored("[-] Password strength requirements not met. Update password failed.", "red"))
                                    self.log_changes_event(acc_id, "Platform Password", "Update", "Failed")
                                    continue
                                account_entry['password'] = self.encrypt_password(new_password)
                                account_entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                                with open(PASSFILE, 'w') as file:
                                    json.dump(data, file, indent=4)
                                print(colored("[+] Password updated successfully.", "green"))
                                self.log_changes_event(acc_id, "Platform Password", "Update", "Success")
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            elif response == 'd':
                                caution = input(colored("[!] Caution: Once you remove it, it will be permanently deleted from your system. Are you sure you want to proceed? (y/N): ", "yellow"))
                                if caution == 'y':
                                    master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
                                    with open(USER_DATA_FILE, 'r') as file:
                                        user_data = json.load(file)
                                    decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
                                    try:
                                        self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
                                    except VerifyMismatchError:
                                        print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
                                        self.log_changes_event(acc_id, "Platform Password", "Delete", "Failed")
                                        continue
                                    data = [e for e in data if not (e['account_id'] == acc_id)]
                                    with open(PASSFILE, 'w') as file:
                                        json.dump(data, file, indent=4)
                                    print(colored("[+] Account permanently deleted.", "green"))
                                    self.log_changes_event(acc_id, "Platform Password", "Delete", "Success")
                                    self.notify_expiry()
                                    self.notify_pin_expiry()
                                elif caution == 'n':
                                    print(colored("[-] Delete operation aborted.", "red"))
                                else:
                                    print(colored("[-] Invalid option.", "red"))
                            else:
                                print(colored("[-] Invalid option.", "red"))
                        else:
                            email_phone = self.decrypt_information(account_entry['email_address/phone'])
                            if email_phone.lstrip('+').isdigit():
                                parsed_phone = phonenumbers.parse(email_phone, None)
                                if phonenumbers.is_valid_number(parsed_phone):
                                    carrier_name = carrier.name_for_number(parsed_phone, "en")
                                    email_phone = f"{email_phone} ({carrier_name})"
                            if decrypted_password is not None:
                                print(colored(f"[+] Platform: {colored(self.decrypt_information(account_entry['website']), 'green')}", "light_yellow"))
                                print(colored(f"[+] Email/Phone: {colored(email_phone, 'green')}", "light_yellow"))
                                print(colored(f"[+] Username: {colored(self.decrypt_information(account_entry['username']), 'green')}", "light_yellow"))
                                print(colored(f"[+] Password: {colored(decrypted_password, 'green')}", "light_yellow"))
                                result = self.check_password_pwned(decrypted_password)
                                if result['status'] == 'found':
                                    print(colored(result['message'], "light_magenta"))
                                elif result['status'] == 'not_found':
                                    pass
                                else:
                                    pass
                                self.notify_expiry()
                                self.notify_pin_expiry()
                    else:
                        print(colored("[-] Password not found for this account ID.", "red"))
                except FileNotFoundError:
                    print(colored("[-] No passwords have been saved yet. Retrieve passwords failed!", "red"))
            
            elif choice == 'changemaster':
                self.change_master_password()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'genpasswd':
                generated_password = self.generate_password()
                print(colored(f"[+] Generated Password: {colored(generated_password, 'green')}", "light_yellow"))
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'del_platform_passwd':
                self.delete_password()
                self.notify_expiry()
                self.notify_pin_expiry()

            elif choice == 'del_os_passwd':
                self.delete_os_password()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'del_card_pin':
                self.delete_card_pin()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'del_api_key':
                self.delete_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_api_key':
                self.show_api_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'add_priv_note':
                title = input(colored("[*] Title: ", "light_blue"))
                if not title:
                    print(colored("[-] No Title provided!", "red"))
                    continue
                print(colored("[*] Paste your Note (Type 'END' on a new line to finish):", "light_blue"))
                note_lines = []
                try:
                    while True:
                        line = input()
                        note_lines.append(line)
                        if line.upper() == "END":
                            if len(note_lines) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                note = '\n'.join(note_lines[:-1])
                                self.add_private_note(title, note)
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                except Exception as e:
                    print("Error:", e)
                    continue
            
            elif choice == 'get_priv_note':
                try:
                    try:
                        note_id = int(input(colored("[*] Note ID: ", "light_blue")))
                    except ValueError:
                        print(colored("[-] Invalid Note ID", "red"))
                        continue
                    with open(PRIVNOTE, 'r') as file:
                        data = json.load(file)
                    if note_id not in [entry['note_id'] for entry in data]:
                        print(colored(f"[-] This ID {note_id} doesn't exist", "red"))
                    key_found = False
                    for entry in data:
                        if entry['note_id'] == note_id:
                            decrypted_note = self.get_private_note(note_id)
                            key_found = True
                            if decrypted_note is not None:
                                print(colored(f"[+] Title: {colored(self.decrypt_information(entry.get('title')), 'green')}", "light_yellow"))
                                print(colored(f"[+] Note:", "light_yellow"))
                                formatted_note = ''.join(decrypted_note)
                                print(colored(formatted_note, "green"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("[-] Private Note not found. QUITTING!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                except FileNotFoundError:
                    print(colored("[-] Private Note not found. QUITTING!", "red"))
                    continue
            
            elif choice == 'del_priv_note':
                self.delete_private_note()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'ch_priv_note':
                try:
                    note_id = int(input(colored("[*] Note ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Note ID", "red"))
                    continue
                try:
                    with open(PRIVNOTE, 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    print(colored("[-] No Private Note Saved! Changing Failed!", "red"))
                    self.log_changes_event(note_id, "Private Note", "Change", "Failed")
                    continue
                index = -1
                for i, entry in enumerate(data):
                    if entry['note_id'] == note_id:
                        index = i
                        break
                if index == -1:
                    print(colored("[-] Note ID not found. QUITTING!", "red"))
                    continue
                existing_content = self.decrypt_information(data[index]['note'])
                print(colored("[*] Current Note Content:", "light_yellow"))
                print(colored(existing_content, "green"))
                additional_content = []
                print(colored("[*] Paste New Content, type 'END' in a new line to finish:", "light_blue"))
                try:
                    while True:
                        line = input()
                        additional_content.append(line)
                        if line.upper() == "END":
                            if len(additional_content) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                break
                except Exception as e:
                    print("Error:", e)
                    continue
                new_content = '\n'.join(additional_content[:-1])
                data[index]['note'] = self.encrypt_information(new_content)
                with open(PRIVNOTE, 'w') as file:
                    json.dump(data, file, indent=4)
                print(colored("[+] New content added to the Private Note successfully!", "green"))
                self.log_changes_event(note_id, "Private Note", "Change", "Success")
            
            elif choice == 'add_src_code':
                programming_language = input(colored("[*] Programming Language: ", "light_blue")).title()
                if not programming_language:
                    print(colored("[-] No Programming Language provided!", "red"))
                    continue
                filename = input(colored("[*] File Name: ", "light_blue"))
                if not filename:
                    print(colored("[-] No filename provided!", "red"))
                    continue
                print(colored("[*] Paste the Source Code Below (Type 'END' on a new line to finish):", "light_blue"))
                source_code_lines = []
                try:
                    while True:
                        code = input()
                        source_code_lines.append(code)
                        if code.upper() == "END":
                            if len(source_code_lines) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                source_code = '\n'.join(source_code_lines[:-1])
                                self.add_source_code(programming_language, filename, source_code)
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                except Exception as e:
                    print("Error:", e)
                    continue

            elif choice == 'get_src_code':
                try:
                    try:
                        code_id = int(input(colored("[*] Code ID: ", "light_blue")))
                    except ValueError:
                        print(colored("[-] Invalid Code ID", "red"))
                        continue
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                    if code_id not in [entry['code_id'] for entry in data]:
                        print(colored(f"[-] This ID {code_id} doesn't exist", "red"))
                    decrypted_code = self.get_source_code(code_id)
                    key_found = False
                    for entry in data:
                        if entry['code_id'] == code_id:
                            key_found = True
                            if decrypted_code is not None:
                                print(colored(f"[+] Programming Language: {colored(self.decrypt_information(entry.get('language')), 'green')}", "yellow"))
                                print(colored(f"[+] File Name: {colored(self.decrypt_information(entry.get('filename')), 'green')}", "yellow"))
                                print(colored(f"[+] Source Code:", "yellow"))
                                formatted_code = ''.join(decrypted_code)
                                print(colored(formatted_code, "green"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("[-] Source Code not found.", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                except FileNotFoundError:
                    print(colored("[-] Source Code not found.", "red"))
                    continue
            
            elif choice == 'del_src_code':                                        
                self.delete_source_code()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'ch_src_code':
                try:
                    code_id = int(input(colored("[*] Code ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Code ID", "red"))
                    return
                updated_source_code = []
                try:
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    print(colored("[-] No Source Code Saved! Changing Failed!", "red"))
                    self.log_changes_event(code_id, "Source Code", "Change", "Failed")
                    return
                index = -1
                for i, entry in enumerate(data):
                    if entry['code_id'] == code_id:
                        index = i
                        break
                if index == -1:
                    print(colored("[-] Code ID not found. QUITTING!", "red"))
                    continue
                filename = self.decrypt_information(data[index]['filename'])
                print(colored(f"[i] File Name: {colored(filename, 'green')}", "light_grey"))
                print(colored("[*] Paste Updated Source Code Below (Type 'END' on a new line to finish):", "light_blue"))
                try:
                    while True:
                        line = input()
                        updated_source_code.append(line)
                        if line.upper() == "END":
                            if len(updated_source_code) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                break
                except Exception as e:
                    print("Error:", e)
                    continue
                source_code = '\n'.join(updated_source_code[:-1])
                try:
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                for entry in data:
                    if entry['code_id'] == code_id:                        
                        entry['code'] = self.encrypt_information(source_code)
                        with open(SRCCODE, 'w') as file:           
                            json.dump(data, file, indent=4)               
                            decrypted_code = self.decrypt_information(entry['code'])
                        if decrypted_code:
                            print(colored("[+] Source Code updated successfully!", "green"))
                            self.log_changes_event(code_id, "Source Code", "Update", "Success")
                            self.notify_expiry()
                            self.notify_pin_expiry()
                        else:
                            print(colored("[-] Source Code update failed.", "red")) 
                            self.log_changes_event(code_id, "Source Code", "Update", "Failed")
                            self.notify_expiry()
                            self.notify_pin_expiry()
            
            elif choice == 'add_ssh_key':
                username = input(colored("[*] Username: ", "light_blue"))
                if not username:
                    print(colored("[-] No username provided! QUITTING!", "red"))
                    continue
                key_name = input(colored("[*] Key Name: ", "light_blue"))
                if not key_name:
                    print(colored("[-] No key name provided! QUITTING!", "red"))
                    continue
                print(colored("[*] Paste the Private Key Below (Type 'END' on a new line to finish):", "light_blue"))
                private_key_lines = []
                try:
                    while True:
                        line = input()
                        private_key_lines.append(line)
                        if line.upper() == "END":
                            if len(private_key_lines) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                break
                except Exception as e:
                    print(colored("[-] Error:", e, "red"))
                    continue
                if private_key_lines[-1].upper() == "END" and len(private_key_lines) == 1:
                    continue
                print(colored("[*] Paste the Public Key Below (Type 'END' on a new line to finish):", "light_blue"))
                public_key_lines = []
                try:
                    while True:
                        line = input()
                        public_key_lines.append(line)
                        if line.upper() == "END":
                            if len(public_key_lines) == 1:
                                print(colored("[-] Editor is empty! Nothing to save!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            else:
                                break
                except Exception as e:
                    print(colored("[-] Error:", e, "red"))
                    continue
                if public_key_lines[-1].upper() == "END" and len(public_key_lines) == 1:
                    continue
                private_key = '\n'.join(private_key_lines[:-1])
                public_key = '\n'.join(public_key_lines[:-1])
                if not private_key.startswith("-----BEGIN OPENSSH PRIVATE KEY-----") or not private_key.endswith("-----END OPENSSH PRIVATE KEY-----"):
                    print(colored("[-] Invalid SSH Private Key!", "red"))
                    continue
                if not public_key.startswith("ssh-rsa"):
                    print(colored("[-] Invalid SSH Public Key!", "red"))
                    continue
                is_password_protected = False
                passphrase = None
                try:
                    password_protected = "False"
                    key = paramiko.RSAKey(file_obj=io.StringIO(private_key))
                    self.add_ssh_key(username, key_name, private_key, public_key, password_protected)
                    self.notify_expiry()
                    self.notify_pin_expiry()
                except paramiko.ssh_exception.PasswordRequiredException:
                    is_password_protected = True
                    try:
                        if is_password_protected:
                            print(colored("[i] The private key is Password-Protected!", "light_grey"))
                            passphrase = getpass.getpass(colored("[*] Private key passphrase: ", "light_blue"))
                            re_enter = getpass.getpass(colored("[*] Re-Enter passphrase: ", "light_blue"))
                            if re_enter != passphrase:
                                print(colored("[-] Passphrase did not match! QUITTING!", "red"))
                                continue
                            else:
                                key = paramiko.RSAKey(file_obj=io.StringIO(private_key), password=passphrase)
                        else:
                            key = paramiko.RSAKey(file_obj=io.StringIO(private_key))
                    except Exception as e:
                        print(colored(f"[-] {e}", "red"))
                    else:
                        password_protected = "True"
                        self.add_ssh_key(username, key_name, private_key, public_key, password_protected, passphrase)
                        self.notify_expiry()
                        self.notify_pin_expiry()
            
            elif choice == 'get_ssh_key':
                try:
                    try:
                        key_id = int(input(colored("[*] Key ID: ", "light_blue")))
                    except ValueError:
                        print(colored("[-] Invalid Key ID", "red"))
                        continue
                    with open(SSH, 'r') as file:
                        data = json.load(file)
                    if key_id not in [entry['key_id'] for entry in data]:
                        print(colored(f"[-] This ID {key_id} doesn't exist", "red"))
                    key_found = False
                    for entry in data:
                        if entry['key_id'] == key_id:
                            key_found = True
                            print(colored(f"[+] Username: {colored(self.decrypt_information(entry.get('username')), 'green')}", "light_yellow"))
                            print(colored(f"[+] Key Name: {colored(self.decrypt_information(entry.get('key_name')), 'green')}", "light_yellow"))
                            private_key_lines = self.get_private_ssh_key(key_id)
                            if private_key_lines is not None:
                                print(colored("[+] Private Key:", "light_yellow"))
                                formatted_private_key = ''.join(private_key_lines)
                                print(colored(formatted_private_key, "green"))
                            else:
                                print(colored("[-] Private Key not found!", "red"))
                            public_key_lines = self.get_public_ssh_key(key_id)
                            if public_key_lines is not None:
                                print(colored("\n[+] Public Key:", "light_yellow"))
                                formatted_public_key = ''.join(public_key_lines)
                                print(colored(formatted_public_key, "green"))
                            else:
                                print(colored("[-] Public Key not found!", "red"))
                            decrypted_passphrase = self.get_passphrase_private_ssh_key(key_id)
                            if decrypted_passphrase != 'null':
                                print(colored(f"\n[+] Passphrase: {colored(decrypted_passphrase, 'green')}", "light_yellow"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("\n[i] This key has no Passphrase", "light_grey"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                    if not key_found:
                        print(colored(f"[-] This Key ID {key_id} is not available in your vault.", "red"))
                except FileNotFoundError:
                    print(colored("[-] No SSH Key have been saved. Retrieve SSH Key failed!", "red"))
            
            elif choice == 'del_ssh_key':
                self.delete_ssh_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'ch_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Account ID", "red"))
                    continue
                self.change_password(acc_id)
                self.notify_expiry()
                self.notify_pin_expiry()

            elif choice == 'ch_os_passwd':
                try:
                    acc_id = int(input(colored("[*] OS ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid OS ID", "red"))
                    continue
                self.change_os_password(acc_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'ch_card_pin':
                try:
                    card_id = int(input(colored("[*] Card ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Card ID!", "red"))
                    continue
                self.change_pin(card_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'ch_ssh_key':
                try:
                    key_id = int(input(colored("[*] Key ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Key ID", "red"))
                    continue
                self.change_ssh_key(key_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'enable2fa':
                with open(USER_DATA_FILE, 'r') as file:
                    user_data = json.load(file)
                if user_data.get('2fa_enabled', False):
                    print(colored("[-] 2FA is already enabled for this user.", "red"))
                    continue
                verify = input(colored("[*] After this, you will need to provide the 6-digit code before you can successfully logged in to your vault. Are you sure you want to proceed? (y/N): ", "light_blue"))
                if verify == 'y':
                    self.enable_2fa()
                    self.notify_expiry()
                    self.notify_pin_expiry()
                else:
                    print(colored("[-] Abort!", "red"))
            
            elif choice == 'show_passwd_exp':
                self.show_expiry_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_pin_exp':
                self.show_pin_expiry_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_priv_note':
                self.show_priv_note_status()
                self.notify_expiry()
                self.notify_pin_expiry()

            elif choice == 'show_os_passwd':
                self.show_os_passwd_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_src_code':
                self.show_src_code_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_ssh_key':
                self.show_ssh_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_passwd_strength':
                self.show_passwd_strength()
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'show_config_loggings':
                self.show_config_loggings()
            
            elif choice == 'reset':
                caution = input(colored("[!] Caution: After attempting to do reset, all of the data including your passwords and your master user in mira will be deleted permanently! Are you sure that you want to proceed? (y/N): ", "yellow"))
                if caution == 'y':
                    master_password = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
                    if master_password is None:
                        print(colored("[-] Incorrect current master password. Reset procedure failed!", "red"))
                        continue
                    with open(USER_DATA_FILE, 'r') as file:
                        user_data = json.load(file)
                    stored_master_password = self.decrypt_password((base64.b64decode(user_data.get('9034374927023', ''))).decode())
                    try:
                        self.ph.verify(stored_master_password, master_password + user_data.get('2104941992374', ''))
                    except VerifyMismatchError:
                        print(colored("[-] Incorrect current master password. Reset procedure failed!", "red"))
                        continue
                    if os.path.exists(LOCKOUT_FILE):
                        os.remove(LOCKOUT_FILE)
                    else:
                        pass
                    if os.path.exists(PASSFILE):
                        os.remove(PASSFILE)
                    else:
                        pass
                    if os.path.exists(CARD_PIN_FILE):
                        os.remove(CARD_PIN_FILE)
                    else:
                        pass
                    if os.path.exists(API):
                        os.remove(API)
                    else:
                        pass
                    if os.path.exists(PRIVNOTE):
                        os.remove(PRIVNOTE)
                    else:
                        pass
                    if os.path.exists(SSH):
                        os.remove(SSH)
                    else:
                        pass
                    if os.path.exists(SRCCODE):
                        os.remove(SRCCODE)
                    else:
                        pass
                    if os.path.exists(CONFIG_LOGS):
                        os.remove(CONFIG_LOGS)
                    else:
                        pass
                    if os.path.exists(OSPASSFILE):
                        os.remove(OSPASSFILE)
                    else:
                        pass
                    os.remove(USER_DATA_FILE)
                    print(colored("[+] All data has been successfully removed.", "green"))
                    start_again = input(colored("[*] Do you want to start a new account? (y/N): ", "light_blue"))
                    if start_again == 'y':
                        username = input(colored("[*] New Username: ", "light_blue"))
                        registration = True
                        while registration:
                            master_password = getpass.getpass(colored("[*] New Master Password: ", "light_blue"))
                            re_enter = getpass.getpass(colored("[*] Re-enter Master Password: ", "light_blue"))
                            if re_enter != master_password:
                                print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                continue
                            else:
                                show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "light_blue"))
                                if show_password_option.lower() == 'y':
                                    print(colored(f"[i] Master Password: {colored(master_password, 'light_green')}", "light_grey"))
                                    confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "light_blue"))
                                    if confirm_password_option.lower() == 'n':
                                        print(colored("[*] Please enter a new master password.", "light_blue"))
                                        continue
                                    elif confirm_password_option.lower() == 'y':
                                        self.register(username, master_password)
                                        registration = False
                                        prompt = False
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration = False
                                        prompt = False
                                elif show_password_option.lower() == 'n':
                                    self.register(username, master_password)
                                    registration = False
                                    prompt = False
                                else:
                                    print(colored("[-] Invalid Option!", "red"))
                                    registration = False
                                    prompt = False
                    else:
                        print(colored("[-] Abort.", "red"))
                        break
                else:
                    print(colored("[-] Abort.", "red"))
                    continue
            
            elif choice == 'add_api_key':
                platform = input(colored("[*] Platform: ", "light_blue"))
                if not validators.url(platform):
                    print(colored("[-] The platform you've entered is Invalid! Please make sure that it's in URL form.", "red"))
                    continue
                key_name = input(colored("[*] Key Name: " , "light_blue"))
                if not key_name:
                    print(colored("[-] No key name provided! QUITTING!", "red"))
                    continue
                key = getpass.getpass(colored("[*] API Key: ", "light_blue"))
                if not key:
                    print(colored("[-] No key provided! QUITTING!", "red"))
                    continue
                self.add_key(platform, key_name, key)
                self.notify_expiry()
                self.notify_pin_expiry()
            
            elif choice == 'add_card_pin':
                card_brand = input(colored("[*] Card Brand: ", "light_blue")).lower()
                if card_brand not in ['visa', 'mastercard', 'american express', 'discover', 'jcb', 'diners club', 'maestro', 'verve']:
                    print(colored("[-] Invalid Card Brand or Card Brand Not Supported!", "red"))
                    continue
                if card_brand== 'jcb':
                    formatted_card_brand = card_brand.upper()
                else:
                    formatted_card_brand = card_brand.title()
                card_type = input(colored("[*] Card Type: ", "light_blue")).title()
                if card_type not in ['Debit', 'Credit', 'Prepaid']:
                    print(colored("[-] Invalid Card Type!", "red"))
                    continue
                try:
                    card_number = input(colored("[*] Card Number: ", "light_blue"))
                    if formatted_card_brand in self.card_patterns:
                        pattern = self.card_patterns[formatted_card_brand]
                        if not re.match(pattern, card_number):
                            print(colored(f"[-] The card number is invalid for card brand {formatted_card_brand}", "red"))
                            continue
                        pin = getpass.getpass(colored("[*] Card PIN: ", "light_blue"))
                        if not pin:
                            print(colored("[-] No PIN provided! QUITTING!", "red"))
                            continue
                        digits = [char for char in pin if char.isdigit()]
                        num_digits = len(digits)
                        if pin.isdigit() and len(pin) in (4, 6):
                            re_enter = getpass.getpass(colored("[*] Re-Enter Card PIN: ", "light_blue"))
                            if not re_enter:
                                print(colored("[-] Re-Enter your PIN! QUITTING!", "red"))
                                continue
                            if re_enter != pin:
                                print(colored("[-] PIN did not match. QUITTING!", "red"))
                                continue
                            self.add_card_pin(formatted_card_brand, card_type, card_number, pin)
                            self.notify_expiry()
                            self.notify_pin_expiry()
                        else:
                            print(colored(f"[-] Typical length of PINs ranges from 4 to 6 digits, the length of the PIN that you've entered has {num_digits} digits.", "red"))
                except ValueError:
                    print(colored("[-] No Account Number provided. QUTTING!", "red"))
                    continue
            
            elif choice == 'show_loggings':
                self.show_loggings()
            
            elif choice == 'get_api_key':
                try:
                    key_id = int(input(colored("[*] Account ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Account ID.", "red"))
                    continue
                decrypted_key = self.get_key(key_id)
                try:
                    with open(API, 'r') as file:
                        data = json.load(file)
                    if key_id not in [entry['unique_id'] for entry in data]:
                        print(colored(f"[-] This ID {key_id} doesn't exist", "red"))
                    for entry in data:
                        if entry["unique_id"] == key_id:
                            print(colored(f"[+] Platform: {colored(self.decrypt_information(entry.get('platform')), 'green')}", "light_yellow"))
                            print(colored(f"[+] Keyname: {colored(self.decrypt_information(entry.get('key_name')), 'green')}", "light_yellow"))
                            print(colored(f"[+] API Key: {colored(decrypted_key, 'green')}", "light_yellow"))
                            self.notify_expiry()
                            self.notify_pin_expiry()
                            break
                    else:
                        continue
                except FileNotFoundError:
                    print(colored("[-] API Key not found. QUITTING!", "red"))
                    continue
            
            elif choice == 'get_card_pin':
                try:
                    card_id = int(input(colored("[*] Card ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Card ID!", "red"))
                    continue
                decrypted_pin = self.get_card_pin(card_id)
                try:
                    with open(CARD_PIN_FILE, 'r') as file:
                        data = json.load(file)
                    if card_id not in [entry['card_id'] for entry in data]:
                        print(colored(f"[-] This card type {card_id} is not available in your vault.", "red"))
                    else:
                        for entry in data:
                            if entry['card_id'] == card_id:
                                expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S") if 'expiry_at' in entry else None
                                if expiry_date and datetime.now() > expiry_date:
                                    response = input(colored("[*] Card PIN has expired. Do you want to update the PIN or delete the card details? (U/D): ", "light_blue")).lower()
                                    if response == 'u':
                                        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
                                        with open(USER_DATA_FILE, 'r') as file:
                                            user_data = json.load(file)
                                        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
                                        try:
                                            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
                                        except VerifyMismatchError:
                                            print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
                                            self.log_changes_event(card_id, "Card PIN", "Update", "Failed")
                                            continue
                                        new_pin = getpass.getpass(colored("[*] New Card PIN: ", "light_blue"))
                                        re_enter = getpass.getpass(colored("[*] Re-Enter New Card PIN: ", "light_blue"))
                                        if new_pin.isdigit() and len(new_pin) not in (4, 6):
                                            print(colored(f"[-] Typical length of PINs ranges from 4 to 6 digits. QUITTING!", "red"))
                                            continue
                                        if re_enter != new_pin:
                                            print(colored("[-] PIN did not match. QUITTING!", "red"))
                                            continue
                                        if any(self.decrypt_information(entry['pin']) == new_pin for entry in data):
                                            print(colored("[-] Card PIN has been used, avoid reusing PINs. QUITTING!", "red"))
                                            continue
                                        entry['pin'] = self.encrypt_information(new_pin)
                                        entry['expiry_at'] = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
                                        with open(CARD_PIN_FILE, 'w') as file:
                                            json.dump(data, file, indent=4)
                                        decrypted_pin = self.decrypt_information(entry['pin'])
                                        if decrypted_pin:
                                            print(colored("[+] Card PIN Updated Successfully!", "green"))
                                            self.log_changes_event(card_id, "Card PIN", "Update", "Success")
                                            self.notify_expiry()
                                            self.notify_pin_expiry()
                                        else:
                                            print(colored("[-] Card PIN Updated Failed.", "red"))
                                            self.log_changes_event(card_id, "Card PIN", "Update", "Failed")
                                            self.notify_expiry()
                                            self.notify_pin_expiry()
                                        continue
                                    elif response == 'd':
                                        caution = input(colored("[!] Caution: Once you remove it, it will be permanently deleted from your system. Are you sure you want to proceed? (y/N): ", "yellow"))
                                        if caution == 'n':
                                            print(colored("[-] Abort.", "red"))
                                            continue
                                        elif caution == 'y':
                                            master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
                                            with open(USER_DATA_FILE, 'r') as file:
                                                user_data = json.load(file)
                                            decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
                                            try:
                                                self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
                                            except VerifyMismatchError:
                                                print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
                                                self.log_changes_event(card_id, "Card PIN", "Update", "Failed")
                                                continue
                                            data = [e for e in data if not (e['card_id'] == card_id)]
                                            with open(CARD_PIN_FILE, 'w') as file:
                                                json.dump(data, file, indent=4)
                                            print(colored("[+] Card details permanently deleted.", "green"))
                                            self.log_changes_event(card_id, "Card PIN", "Delete", "Success")
                                            self.notify_expiry()
                                            self.notify_pin_expiry()
                                        continue
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        continue
                                else:
                                    if decrypted_pin is not None:
                                        print(colored(f"[+] Card Brand: {colored(self.decrypt_information(entry.get('card_brand')), 'green')}", "light_yellow"))
                                        print(colored(f"[+] Card Type: {colored(self.decrypt_information(entry.get('card_type')), 'green')}", "light_yellow"))
                                        print(colored(f"[+] Card Number: {colored(self.decrypt_information(entry.get('card_number')), 'green')}", "light_yellow"))
                                        print(colored(f"[+] Key Content: {colored(decrypted_pin, 'green')}", "light_yellow"))
                                        self.notify_expiry()
                                        self.notify_pin_expiry()
                                    else:
                                        print(colored("[-] Card PIN not found. QUITTING!", "red"))
                except FileNotFoundError:
                    print(colored("[-] No card details have been saved. ", "red"))
            
            elif choice == 'ch_api_key':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
                except ValueError:
                    print(colored("[-] Invalid Account ID!", "red"))
                    continue
                self.change_key(acc_id)
            
            elif choice == 'mnemonic_enc_key':
                encryption_key = input(colored("[*] Key: ", "light_blue"))
                if not encryption_key:
                    print(colored("[-] No encryption key provided!", "red"))
                    continue
                chosen_language = input(colored("[*] Language: ", "light_blue"))
                try:
                    if not chosen_language:
                        print(colored("[i] No language provided, default to English.", "light_grey"))
                        chosen_language = "english"
                    encryption_key = encryption_key.replace('-', '+').replace('_', '/')
                    key = base64.b64decode(encryption_key)
                    hex_key = key.hex()
                    mnemonic = Mnemonic(chosen_language)
                    mnemonic_phrase = mnemonic.to_mnemonic(bytes.fromhex(hex_key))
                    print(colored(f"[+] Mnemonic Phrase: {colored(mnemonic_phrase, 'green')}", "light_yellow"))
                    print(colored(f"[i] It's advisable to write this phrases on a paper or memorize it if you can.", "light_grey"))
                    continue
                except ValueError:
                    print(colored("[-] The key you provided is not acceptable. Make sure that it's in the correct format.", "red"))
                    continue
                except ConfigurationError as e:
                    print(colored(f"[-] {e}", "red"))
                    continue
            
            elif choice == 'dec_mnemonic':
                mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "light_blue"))
                chosen_language = input(colored("[*] Language: ", "light_blue"))
                if not mnemonic_phrase:
                    print(colored("[-] No mnemonic phrase provided!", "red"))
                    continue
                try:
                    if not chosen_language:
                        print(colored("[i] No language provided, default to English.", "light_grey"))
                        chosen_language = "english"
                    mnemonic = Mnemonic(chosen_language)
                    key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                    key_base64 = base64.b64encode(key_bytes).decode()
                    encryption_key = key_base64.replace('+', '-').replace('/', '_')
                    print(colored(f"[+] Encryption Key: {colored(encryption_key, 'green')}", "light_yellow"))
                    continue
                except ValueError:
                    print(colored("[-] Insufficient number of words or not the correct language!", "red"))
                    continue
                except ConfigurationError as e:
                    print(colored(f"[-] Error: {e}", "red"))
                    continue
            
            elif choice == 'check_my_passwd_if_pwned':
                try:
                    print(colored("[*] Choose one of the following:\n1. Enter your Password Manually\n2. Enter Account ID", "light_blue"))
                    choice = int(input(colored("[*] Choice: ", "light_blue")))
                    if choice == 1:
                        user_password = getpass.getpass(colored("[*] Your Password: ", "light_blue"))
                        result = self.check_password_pwned(user_password)
                        if result['status'] == 'found':
                            print(colored(f"[!] Password found in breaches!", "light_magenta"))
                            print(colored(f"[i] SHA-1 Hash: {result['sha1_hash']}", "light_grey"))
                            print(colored(f"[!] Number of breaches: {result['breach_count']}", "light_magenta"))
                            print(colored(result['message'], "light_magenta"))
                        elif result['status'] == 'not_found':
                            print(colored(f"[+] Password not found in any breaches.", "green"))
                            print(colored(f"[i] SHA-1 Hash: {result['sha1_hash']}", "light_grey"))
                        else:
                            print(colored(result['message'], "red"))
                    elif choice == 2:
                        acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
                        if not os.path.exists(PASSFILE):
                            return None
                        try:
                            with open(PASSFILE, 'r') as file:
                                data = json.load(file)
                        except FileNotFoundError:
                            print(colored("[-] No Password Saved! Checking Failed!", "red"))
                            continue
                        except json.JSONDecodeError:
                            data = {}
                        if acc_id not in [entry['account_id'] for entry in data]:
                            print(colored(f"[-] This ID {acc_id} doesn't exist", "red"))
                        if isinstance(data, list):
                            account_data = next((item for item in data if item.get("account_id") == acc_id), None)
                        elif isinstance(data, dict):
                            if data.get("account_id") == acc_id:
                                account_data = data
                            else:
                                account_data = None
                        else:
                            account_data = None
                        if account_data:
                            decrypted_key_content = self.decrypt_password(account_data.get("password"))
                            result = self.check_password_pwned(decrypted_key_content)
                            if result['status'] == 'found':
                                print(colored(f"[!] Password found in breaches!", "light_magenta"))
                                print(colored(f"[i] SHA-1 Hash: {result['sha1_hash']}", "light_grey"))
                                print(colored(f"[!] Number of breaches: {result['breach_count']}", "light_magenta"))
                                print(colored(result['message'], "light_magenta"))
                            elif result['status'] == 'not_found':
                                print(colored(f"[+] Password not found in any breaches.", "green"))
                                print(colored(f"[i] SHA-1 Hash: {result['sha1_hash']}", "light_grey"))
                            else:
                                print(colored(result['message'], "red"))
                    else:
                        print(colored("[-] Invalid Choice!", "red"))
                        continue
                except ValueError:
                    print(colored("[-] Invalid Option!", "red"))
                    continue

            elif choice == 'lout':
                self.logout()
                break
            
            elif choice == 'h' or choice == 'help':
                print(colored("[*] Choose what type of options you want MIRA to show:\n1. Adding Credentials\n2. Retrieving Credentials\n3. Deleting Credentials\n4. Changing Credentials\n5. Listing and Analysis\n6. Security and other Configuration\n7. User Actions", "light_blue"))
                try:
                    help_choice = int(input(colored("[*] Enter the number of the Category: ", "light_blue")))
                    if help_choice == 1:
                        print(colored("[+] Available Commands for Adding Credentials:\n'add_platform_passwd' - Add a new password\n'add_api_key' - Add a new API key\n'add_card_pin' - Add a new PIN\n'add_ssh_key' - Add a new SSH Key\n'add_src_code' - Add a new Source Code\n'add_priv_note' - Add a new Private Note\n'add_os_passwd' - Add a new Operating System Password", "light_green"))
                    elif help_choice == 2:
                        print(colored("[+] Available Commands for Retrieving Credentials:\n'get_platform_passwd' - Retrieve the plaintext version of the password for the desired account ID\n'get_api_key' - Retrieve the plaintext version of the key of the desired account ID\n'get_card_pin' - Retrieve the plaintext version of the PIN for the desired card ID\n'get_ssh_key' - Retrieve the plaintext version of the SSH Key for the desired key ID\n'get_src_code' - Retrieve the plaintext version of the Source Code for the desired code ID\n'get_priv_note' - Retrieve the plaintext version of the Private Note for the desired note ID\n'get_os_passwd' - Retrieve the plaintext version of the Operating System for the desired OS ID", "light_green"))
                    elif help_choice == 3:
                        print(colored("[+] Available Commands for Deleting Credentials:\n'del_platform_passwd' - Delete a saved password according to your desired account ID\n'del_api_key' - Delete key according to your desired account ID\n'del_card_pin' - Delete a saved PIN according to your desired card ID\n'del_ssh_key' - Delete a saved SSH Key according to your desired key ID\n'del_src_code' - Delete a saved Source Code according to your desired code ID\n'del_priv_note' - Delete a saved Private Note according to your desired note ID\n'del_os_passwd' - Delete a saved Operating System Password according to your desired OS ID", "light_green"))
                    elif help_choice == 4:
                        print(colored("[+] Available Commands for Changing Credentials:\n'ch_platform_pass' - Change the password for the desired account ID\n'ch_card_pin' - Change the password for the desired pin ID\n'ch_api_key' - Change the API Key for the desired account ID\n'ch_ssh_key' - Chabge the SSH Key for the desired key ID\n'ch_src_code' - Change the Source Code for the desired code ID\n'ch_priv_note' - Change the Private Note for the desired note ID\n'ch_os_passwd' - Change the Operating System Password for the desired OS ID", "light_green"))
                    elif help_choice == 5:
                        print(colored("[+] Available Commands for Listing and Analaysis:\n'show_passwd_exp' - List the usernames and their status on a specific platform or all\n'show_pin_exp' - List the card numbers and their status on a specific card type or all\n'show_api_key' - List the available API Key with their Key ID, Platform, Key Name, and their date when they were added (No Expiry when it comes to API Keys)\n'show_ssh_key' - List the available SSH Key with their Key ID, Username, Key Name and their date when they were added (No Expiry when it comes to SSH Keys)\n'show_src_code' - List the available Source Code with their Code ID, File Name, and their date when they were added (No Expiry when it comes to Source Code)\n'show_priv_note' - List the available Private Note with their note ID, Title, and when they were added (No Expiry when it comes to Private Notes)\n'show_os_passwd' - List the available Operating System Passwords with their model, username, and when they were added (No Expiry when it comes to Operating System Passwords)\n'show_passwd_strength' - List the strength of the password of a username on a specific platform\n'show_loggings' - List all the previous logins\n'show_config_loggings' - List all the previous configurations", "light_green"))
                    elif help_choice == 6:
                        print(colored("[+] Available Commands for Security and other Configurations:\n'enable2fa' - Enable Two-Factor Authentication for added security\n'genpasswd' - Generate a strong password\n'changemaster' - Change the masterkey\n'check_my_passwd_if_pwned' - Check if your password has been compromised in existing data breaches (Internet Connection Required!)\n'mnemonic_enc_key' - Convert the encryption key to a mnemonic phrase\n'dec_mnemonic' - Decode a mnemonic phrase to the original encryption key", "light_green"))
                    elif help_choice == 7:
                        print(colored("[+] Available Commands for User Actions:\n'lout' - Logout\n'exit' - Terminate MIRA\n'reset' - Delete all data, including the user account permanently (Be cautious with this command! It can result in permanent data loss!)", "light_green"))
                    else:
                        print(colored("[-] Invalid Option!", "red"))
                except ValueError:
                    print(colored("[-] Invalid Option!", "red"))
            
            elif choice == 'exit':
                print(colored("[*] MIRA Terminated!", "red"))
                sys.exit()
            
            elif choice == 'clear':
                clear_terminal()
            
            elif choice == 'about':
                clear_terminal()
                print(colored(wolf, "blue"))
                print(colored(about, "cyan"))
            
            else:
                similar_command = self.find_similar_main_menu_command(choice)
                if similar_command:
                    print(colored(f"[-] Invalid Command. Did you mean '{similar_command}'?", "red"))
                else:
                    print(colored("[-] Invalid Command", "red"))
                
    def check_username_reuse(self, new_website, new_username, existing_data):
        for entry in existing_data:
            existing_website = self.decrypt_information(entry['website'])
            existing_username = self.decrypt_information(entry['username'])
            if existing_website == new_website and existing_username == new_username:
                return True
        return False

    def check_os_password_reuse(self, new_password, existing_data):
        for entry in existing_data:
            decrypted_password = self.decrypt_password(entry['password'])
            if decrypted_password == new_password:
                return True
        return False
    
    def check_email_reuse(self, new_email, existing_data):
        for entry in existing_data:
            decrypted_email = self.decrypt_information(entry['email_address'])
            if decrypted_email == new_email:
                user_input = input(colored(f"[*] The email '{new_email}' already exists. Do you want to proceed? (y/N): ", "light_blue"))
                if user_input.lower() == 'y':
                    return True
                else:
                    return False
        return False
    
    def check_password_reuse(self, new_password, existing_data):
        for entry in existing_data:
            decrypted_password = self.decrypt_password(entry['password'])
            if decrypted_password == new_password:
                return True
        return False
    
    def validate_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)
            return phonenumbers.is_valid_number(parsed_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False
    
    def add_password(self, website, email_address, username, password):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(PASSFILE):
            data = []
        else:
            try:
                with open(PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        asked_once = False
        for entry in data:
            decrypted_email = self.decrypt_information(entry['email_address/phone'])
            if decrypted_email == email_address:
                if not asked_once:
                    user_input = input(colored(f"[*] The email/phone {email_address} already exists. Do you want to proceed? (y/N): ", "light_blue")).lower()
                    if user_input == 'y':
                        print(colored("[!] It's advisable not to use the same email/phone for another account.", "yellow"))
                        asked_once = True
                        pass
                    else:
                        print(colored("[-] Abort.", "red"))
                        return
        if self.check_username_reuse(website, username, data):
            print(colored(f"[-] The username {username} already exists for this platform!", "red"))
            return
        if self.check_password_reuse(password, data):
            print(colored("[-] Password has been used to other platforms. (Password not added) Avoid using the same password on other platforms!", "red"))
            return
        if self.check_password_strength(password):
            encrypted_website = self.encrypt_information(website)
            encrypted_password = self.encrypt_password(password)
            encrypted_email = self.encrypt_information(email_address)
            encrypted_username = self.encrypt_information(username)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password_entry = {
                'account_id': unique_id,
                'website': encrypted_website,
                'email_address/phone': encrypted_email,
                'username': encrypted_username,
                'password': encrypted_password,
                'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'expiry_at': (datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(password_entry)
            with open(PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored(f"[+] Password added! Account ID for this account: {colored(unique_id, 'green')}", "light_yellow"))
            self.log_changes_event(unique_id, "Platform Password", "Add", "Success")
        else:
            pass

    def add_os_password(self, operating_system, password_type, username, password):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(OSPASSFILE):
            data = []
        else:
            try:
                with open(OSPASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_os_password_reuse(password, data):
            print(colored("[-] Password has been used to other Operating Systems. (Password not added) Avoid using the same password on other devices!", "red"))
            return
        encrypted_os = self.encrypt_information(operating_system)
        encrypted_password_type = self.encrypt_information(password_type)
        encrypted_username = self.encrypt_information(username)
        encrypted_password = self.encrypt_information(password)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        password_entry = {
            'account_id': unique_id,
            'operating_system': encrypted_os,
            'password_type': encrypted_password_type,
            'username': encrypted_username,
            'password': encrypted_password,
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(password_entry)
        with open(OSPASSFILE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Operating System Password added! Account ID for this account: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "OS Password", "Add", "Success")

    def get_os_password(self, i_d):
        if not os.path.exists(OSPASSFILE):
            return None
        try:
            with open(OSPASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Passwords Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        for entry in data:
            if entry['account_id'] == i_d and entry.get('username'):
                decrypted_os = self.decrypt_information(entry['operating_system'])
                decrypted_username = self.decrypt_information(entry['username'])
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    if datetime.now() > expiry_date:
                        return None
                decrypted_password = self.decrypt_password(entry['password'])
                return decrypted_password
        return None

    def get_password(self, i_d):
        if not os.path.exists(PASSFILE):
            return None
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Passwords Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        for entry in data:
            if entry['account_id'] == i_d and entry.get('email_address/phone') and entry.get('username'):
                decrypted_website = self.decrypt_information(entry['website'])
                decrypted_email = self.decrypt_information(entry['email_address/phone'])
                decrypted_username = self.decrypt_information(entry['username'])
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    if datetime.now() > expiry_date:
                        return None
                decrypted_password = self.decrypt_password(entry['password'])
                return decrypted_password
        return None
    
    def delete_password(self):
        try:
            acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid Account ID", "red"))
            return
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Deletion failed!", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Delete", "Failed")
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['account_id'] == acc_id and entry.get('email_address/phone') and entry.get('username')), None)
        if deleted_entry:
            master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
            if not os.path.exists(PASSFILE):
                print(colored("[-] No passwords saved. Deletion failed!", "red"))
                self.log_changes_event(acc_id, "Platform Password", "Delete", "Failed")
                return
            with open(USER_DATA_FILE, 'r') as file:
                user_data = json.load(file)
            decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
            try:
                self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
            except VerifyMismatchError:
                print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
                self.log_changes_event(acc_id, "Platform Password", "Delete", "Failed")
                return
            data.remove(deleted_entry)
            with open(PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Password deleted successfully!", "green"))
            self.log_changes_event(acc_id, "Platform Password", "Delete", "Success")
            if not data:
                os.remove(PASSFILE)
                return
        else:
            print(colored("[-] Password not found! Deletion failed!", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Delete", "Failed")

    def delete_os_password(self):
        try:
            acc_id = int(input(colored("[*] OS ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid OS ID", "red"))
            return
        try:
            with open(OSPASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Deletion failed!", "red"))
            self.log_changes_event(acc_id, "OS Password", "Delete", "Failed")
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['account_id'] == acc_id and entry.get('username')), None)
        if deleted_entry:
            master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
            if not os.path.exists(OSPASSFILE):
                print(colored("[-] No passwords saved. Deletion failed!", "red"))
                self.log_changes_event(acc_id, "OS Password", "Delete", "Failed")
                return
            with open(USER_DATA_FILE, 'r') as file:
                user_data = json.load(file)
            decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
            try:
                self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
            except VerifyMismatchError:
                print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
                self.log_changes_event(acc_id, "OS Password", "Delete", "Failed")
                return
            data.remove(deleted_entry)
            with open(OSPASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] OS Password deleted successfully!", "green"))
            self.log_changes_event(acc_id, "OS Password", "Delete", "Success")
            if not data:
                os.remove(OSPASSFILE)
                return
        else:
            print(colored("[-] Password not found! Deletion failed!", "red"))
            self.log_changes_event(acc_id, "OS Password", "Delete", "Failed")
    
    def change_password(self, acc_id):
        data = []
        if not os.path.exists(PASSFILE):
            print(colored("[-] No passwords saved!", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
            return
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Passwords Saved! Deletion Failed!", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
            return
        except json.JSONDecodeError:
            pass
        account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
        if account_entry:
            username = self.decrypt_information(account_entry['username'])
            current_password = getpass.getpass(colored(f"[*] Current password for the given account ID (Usn: {username}): ", "light_blue"))
        else:
            print(colored("[-] This account ID is not available in your vault.", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
            return
        decrypted_password = self.get_password(acc_id)
        if decrypted_password is not None and current_password == decrypted_password:
            new_password = getpass.getpass(colored("[*] New Password: ", "light_blue"))
            if not new_password:
                print(colored("[-] No New Password Provided!", "red"))
                return
            re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "light_blue"))
            if not self.check_password_strength(new_password):
                return
            if new_password != re_enter:
                print(colored("[-] New Passwords Did Not Match! Change password failed!", "red"))
                self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
                return
            encrypted_new_password = self.encrypt_password(new_password)
            if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                print(colored("[-] Password has been used. (Change password failed) Avoid reusing passwords!", "red"))
                self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
                return
            try:
                with open(PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['account_id'] == acc_id:
                    entry['password'] = encrypted_new_password
                    entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                    with open(PASSFILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_password = self.decrypt_password(entry['password'])
                    if decrypted_password:
                        print(colored("[+] Password updated successfully!", "green"))
                        self.log_changes_event(acc_id, "Platform Password", "Change", "Success")
                    else:
                        print(colored("[-] Password update failed.", "red"))
                        self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")
                    return
        else:
            print(colored("[-] Incorrect current password. Change password failed!", "red"))
            self.log_changes_event(acc_id, "Platform Password", "Change", "Failed")

    def change_os_password(self, acc_id):
        data = []
        if not os.path.exists(OSPASSFILE):
            print(colored("[-] No passwords saved!", "red"))
            self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
            return
        try:
            with open(OSPASSFILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Passwords Saved! Deletion Failed!", "red"))
            self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
            return
        except json.JSONDecodeError:
            pass
        account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
        if account_entry:
            username = self.decrypt_information(account_entry['username'])
            current_password = getpass.getpass(colored(f"[*] Current password for the given OS ID (Usn: {username}): ", "light_blue"))
        else:
            print(colored("[-] This OS ID is not available in your vault.", "red"))
            self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
            return
        decrypted_password = self.get_os_password(acc_id)
        if decrypted_password is not None and current_password == decrypted_password:
            new_password_type = input(colored("[*] Password Type: ", "light_blue")).lower()
            if new_password_type not in ['pattern', 'phrase', 'pin']:
                print(colored("[-] Pattern Invalid or Not Supported!", "red"))
                return
            if new_password_type == 'pin':
                formatted_password_type = new_password_type.upper()
            else:
                formatted_password_type = new_password_type.title()
            if formatted_password_type == 'Pattern':
                new_password = getpass.getpass(colored("[*] Describe the new Pattern: ", "light_blue"))
                if not new_password:
                    print(colored("[-] No Pattern Provided!", "red"))
                    self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                    return
            elif formatted_password_type == 'Phrase':
                new_password = getpass.getpass(colored("[*] New OS Password: ", "light_blue"))
                if not new_password:
                    print(colored("[-] No New Password Provided!", "red"))
                    return
                re_enter = getpass.getpass(colored("[*] Re-Enter New OS Password: ", "light_blue"))
                if new_password != re_enter:
                    print(colored("[-] New OS PIN Did Not Match! Change PIN failed!", "red"))
                    self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                    return
            elif formatted_password_type == 'PIN':
                new_password = getpass.getpass(colored("[*] New OS PIN: ", "light_blue"))
                if new_password.isdigit():
                    if not new_password:
                        print(colored("[-] No PIN Provided!", "red"))
                        return
                    re_enter = getpass.getpass(colored("[*] Re-Enter New OS PIN: ", "light_blue"))
                    if new_password != re_enter:
                        print(colored("[-] New OS PIN Did Not Match! Change PIN failed!", "red"))
                        self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                        return
                else:
                    print(colored("[-] Invalid! PIN should be numeric!", "red"))
                    self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                    return
            encrypted_new_password = self.encrypt_password(new_password)
            encrypted_new_password_type = self.encrypt_information(formatted_password_type)
            if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                print(colored("[-] OS Password has been used. (Change password failed) Avoid reusing passwords!", "red"))
                self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                return
            try:
                with open(OSPASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['account_id'] == acc_id:
                    entry['password_type'] = encrypted_new_password_type
                    entry['password'] = encrypted_new_password
                    with open(OSPASSFILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_password = self.decrypt_password(entry['password'])
                    if decrypted_password:
                        print(colored("[+] OS Password updated successfully!", "green"))
                        self.log_changes_event(acc_id, "OS Password", "Change", "Success")
                    else:
                        print(colored("[-] OS Password update failed.", "red"))
                        self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
                    return
        else:
            print(colored("[-] Incorrect current password. Change password failed!", "red"))
            self.log_changes_event(acc_id, "OS Password", "Change", "Failed")
    
    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()
    
    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()
    
    def change_master_password(self):
        current_password = getpass.getpass(colored("[*] Current Master Password: ", "light_blue"))
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = self.decrypt_password((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(stored_master_password, current_password + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Change password failed!", "red"))
            return
        while True:
            new_password = getpass.getpass(colored("[*] New Master Password: ", "light_blue"))
            re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "light_blue"))
            if new_password != re_enter:
                print(colored("[-] New Master Password Did Not Match! Please try again!", "red"))
                continue
            else:
                show_password_option = input(colored("[*] Do you want to show the new master password for verification? (y/N): ", "light_blue"))
                if show_password_option.lower() == 'y':
                    print(colored(f"[i] New Master Password: {colored(new_password, 'light_green')}", "light_grey"))
                    confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "light_blue"))
                    if confirm_password_option.lower() == 'n':
                        print(colored("[*] Please enter a new master password.", "light_blue"))
                        continue
                    elif confirm_password_option.lower() == 'y':
                        if not self.check_master_password_strength(new_password):
                            break
                        fernet = Fernet(encryption_key) 
                        salt = user_data['2104941992374']
                        hashed_new_master_password = self.ph.hash(new_password + salt)
                        encrypted_master_password = fernet.encrypt(hashed_new_master_password.encode())
                        encrypted_new_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
                        user_data['9034374927023'] = encrypted_new_master_password_b64
                        with open(USER_DATA_FILE, 'w') as file:
                            json.dump(user_data, file)
                        self.master_password = new_password
                        print(colored("[+] Master Password changed successfully!", "green"))
                        self.log_changes_event("0000", "Master Password", "Change", "Success")
                        break
                    else:
                        print(colored("[-] Invalid Option!", "red"))
                        break
                elif show_password_option.lower() == 'n':
                    if not self.check_master_password_strength(new_password):
                        break
                    fernet = Fernet(encryption_key) 
                    salt = user_data['2104941992374']
                    hashed_new_master_password = self.ph.hash(new_password + salt)
                    encrypted_master_password = fernet.encrypt(hashed_new_master_password.encode())
                    encrypted_new_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
                    user_data['9034374927023'] = encrypted_new_master_password_b64
                    with open(USER_DATA_FILE, 'w') as file:
                        json.dump(user_data, file)
                    self.master_password = new_password
                    print(colored("[+] Master Password changed successfully!", "green"))
                    self.log_changes_event("0000", "Master Password", "Change", "Success")
                    break
                else:
                    print(colored("[-] Invalid Option!", "red"))
                    break
    
    def check_keyname_reuse(self, new_platform, new_key_name, existing_data):
        for entry in existing_data:
            existing_platform = self.decrypt_information(entry['platform'])
            existing_key_name = self.decrypt_information(entry['key_name'])
            if existing_platform == new_platform and existing_key_name == new_key_name:
                return True
        return False
    
    def check_key_reuse(self, new_key, existing_data):
        for entry in existing_data:
            decrypted_key = self.decrypt_information(entry['key'])
            if decrypted_key == new_key:
                return True
        return False
    
    def add_key(self, platform, key_name, key):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(API):
            data = []
        else:
            try:
                with open(API, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_keyname_reuse(platform, key_name, data):
            print(colored(f"[-] The key name {key_name} already exists for this Platform!", "red"))
            return
        if self.check_key_reuse(key, data):
            print(colored("[-] API Key has been used to other Key Name. (API Key not added) Avoid using the same API on other Key Name!!", "red"))
            return
        api_key_entry = {
            'unique_id': unique_id,
            'platform': self.encrypt_information(platform),
            'key_name': self.encrypt_information(key_name),
            'key': self.encrypt_information(key),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(api_key_entry)
        with open(API, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] API Key added! Account ID for this API Key: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "API Key", "Add", "Success")
    
    def check_cardnumber_reuse(self, new_card_number, existing_data):
        for entry in existing_data:
            existing_card_number = self.decrypt_information(entry['card_number'])
            if existing_card_number == new_card_number:
                return True
        return False
    
    def check_pin_reuse(self, new_pin, existing_data):
        for entry in existing_data:
            decrypted_pin = self.decrypt_information(entry['pin'])
            if decrypted_pin == new_pin:
                return True
        return False
    
    def add_card_pin(self, card_brand, card_type, card_number, pin):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(CARD_PIN_FILE):
            data = []
        else:
            try:
                with open(CARD_PIN_FILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_cardnumber_reuse(card_number, data):
            print(colored(f"[-] The card number {card_number} already exists", "red"))
            return
        if self.check_pin_reuse(pin, data):
            print(colored("[-] PIN has been used to other card number. (PIN not added) Avoid using the same PIN on other card numbers!!", "red"))
            return
        card_pin_entry = {
            'card_id': unique_id,
            'card_brand': self.encrypt_information(card_brand),
            'card_type': self.encrypt_information(card_type),
            'card_number': self.encrypt_information(card_number),
            'pin': self.encrypt_information(pin),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'expiry_at': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(card_pin_entry)
        with open(CARD_PIN_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Card PIN added! Card ID for this PIN: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "Card PIN", "Add", "Success")
    
    def get_key(self, acc_id):
        if not os.path.exists(API):
            return None
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No API Keys Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['unique_id'] == acc_id:
                decrypted_key_name = self.decrypt_information(entry['key_name'])
                decrypted_key = self.decrypt_information(entry['key'])
                return decrypted_key
        return None
    
    def get_card_pin(self, card_id):
        if not os.path.exists(CARD_PIN_FILE):
            return None
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Card PIN Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['card_id'] == card_id:
                decrypted_pin = self.decrypt_information(entry['pin'])
                return decrypted_pin
        return None
    
    def delete_card_pin(self):
        try:
            card_id = int(input(colored("[*] Card ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid Card ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
        if not os.path.exists(CARD_PIN_FILE):
            print(colored("[-] No PIN saved. Deletion failed!", "red"))
            return
        try:
            with open(USER_DATA_FILE, 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Card PIN Saved! Retrieval Failed!", "red"))
            return
        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            self.log_changes_event(card_id, "Card PIN", "Delete", "Failed")
            return
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Card PIN saved. Deletion failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['card_id'] == card_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(CARD_PIN_FILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Card PIN deleted successfully!", "green"))
            self.log_changes_event(card_id, "Card PIN", "Delete", "Success")
            if not data:
                os.remove(CARD_PIN_FILE)
                return
        else:
            print(colored("[-] PIN not found! Deletion failed!", "red"))
            self.log_changes_event(card_id, "Card PIN", "Delete", "Failed")
    
    def delete_key(self):
        try:
            acc_id = int(input(colored("[*] Account ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid Account ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
        if not os.path.exists(API):
            print(colored("[-] No API Keys saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            self.log_changes_event(acc_id, "API Key", "Delete", "Failed")
            return
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No API Keys Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['unique_id'] == acc_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(API, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] API Key successfully deleted!", "green"))
            self.log_changes_event(acc_id, "API Key", "Delete", "Success")
            if not data:
                os.remove(API)
                return
        else:
            print(colored("[-] API Key not found! Deletion failed!", "red"))
            self.log_changes_event(acc_id, "API Key", "Delete", "Failed")
    
    def change_pin(self, card_id):
        data = []
        if not os.path.exists(CARD_PIN_FILE):
            print(colored("[-] No PIN saved!", "red"))
            return
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No PINs Saved! Changing Failed!", "red"))
            self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
            return
        except json.JSONDecodeError:
            pass
        pin_entry = next((entry for entry in data if entry['card_id'] == card_id), None)
        if pin_entry:
            card_number = self.decrypt_information(pin_entry['card_number'])
            current_pin = getpass.getpass(colored(f"[*] Current PIN for the given card ID (No: {card_number}): ", "light_blue"))
        else:
            print(colored(f"[-] This Card ID {card_id} is not available on your PIN vault.", "red"))
            return
        decrypted_pin = self.get_card_pin(card_id)
        if decrypted_pin is not None and current_pin == decrypted_pin:
            try:
                new_pin = getpass.getpass(colored("[*] New PIN: ", "light_blue"))
                digits = [char for char in new_pin if char.isdigit()]
                num_digits = len(digits)
                if new_pin.isdigit() and len(new_pin) not in (4, 6):
                    print(colored(f"[-] Typical length of PINs ranges from 4 to 6 digits! The PIN you've entered has {num_digits} digits.", "red"))
                    return
                if not new_pin:
                    print(colored("[-] No PIN provided! Changing process failed.", "red"))
                    self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
                    return
                new_pin_input = int(new_pin)
                re_enter = getpass.getpass(colored("[*] Re-Enter New PIN: ", "light_blue"))
                if not re_enter:
                    print(colored("[-] Please Re-Enter your new PIN! QUITTING!", "red"))
                    return
                re_enter_input = int(re_enter)
            except ValueError:
                print(colored("[-] Please provide a PIN", "red"))
                return
            if new_pin_input != re_enter_input:
                print(colored("[-] New PINs Did Not Match! Change PIN failed!", "red"))
                self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
                return
            encrypted_new_pin = self.encrypt_information(new_pin)
            if any(self.decrypt_information(entry['pin']) == new_pin for entry in data):
                print(colored("[-] PIN has been used. (Change PIN failed) Avoid reusing PINs!", "red"))
                self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
                return
            try:
                with open(CARD_PIN_FILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['card_id'] == card_id:
                    entry['pin'] = encrypted_new_pin
                    entry['expiry_at'] = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
                    with open(CARD_PIN_FILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_pin = self.decrypt_information(entry['pin'])
                    if decrypted_pin:
                        print(colored("[+] PIN changed successfully!", "green"))
                        self.log_changes_event(card_id, "Card PIN", "Change", "Success")
                    else:
                        print(colored("[-] PIN change failed.", "red"))
                        self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
                    return
        else:
            print(colored("[-] Incorrect current PIN. Change PIN failed!", "red"))
            self.log_changes_event(card_id, "Card PIN", "Change", "Failed")
    
    def change_key(self, acc_id):
        data = []
        if not os.path.exists(API):
            print(colored("[-] No KEYS saved!", "red"))
            return
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Keys Saved! Changing Failed!", "red"))
            self.log_changes_event(acc_id, "API Key", "Change", "Failed")
            return
        except json.JSONDecodeError:
            pass
        account_entry = next((entry for entry in data if entry['unique_id'] == acc_id), None)
        if account_entry:
            keyname = self.decrypt_information(account_entry['key_name'])
            current_key = getpass.getpass(colored(f"[*] Current key for the given account ID (Usn: {keyname}): ", "light_blue"))
        else:
            print(colored(f"[-] This account ID {acc_id} is not available in your vault.", "red"))
            self.log_changes_event(acc_id, "API Key", "Change", "Failed")
            return
        decrypted_key = self.get_key(acc_id)
        if decrypted_key is not None and current_key == decrypted_key:
            new_key = getpass.getpass(colored("[*] New API Key: ", "light_blue"))
            if not new_key:
                print(colored("[-] No New Key Provided!", "red"))
                return
            re_enter = getpass.getpass(colored("[*] Re-Enter New API Key: ", "light_blue"))
            if new_key != re_enter:
                print(colored("[-] New API Key Did Not Match! Change Key failed!", "red"))
                self.log_changes_event(acc_id, "API Key", "Change", "Failed")
                return
            encrypted_new_key = self.encrypt_information(new_key)
            if any(self.decrypt_information(entry['key']) == new_key for entry in data):
                print(colored("[-] API Key has been used. (Change Key failed) Avoid reusing Keys!", "red"))
                self.log_changes_event(acc_id, "API Key", "Change", "Failed")
                return
            try:
                with open(API, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['unique_id'] == acc_id:
                    entry['key'] = encrypted_new_key
                    with open(API, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_key = self.decrypt_information(entry['key'])
                    if decrypted_key:
                        print(colored("[+] API Key changed successfully!", "green"))
                        self.log_changes_event(acc_id, "API Key", "Change", "Success")
                    else:
                        print(colored("[-] API Key changed failed.", "red"))
                        self.log_changes_event(acc_id, "API Key", "Change", "Failed")
                    return
        else:
            print(colored("[-] Incorrect current API Key. Change Key failed!", "red"))
            self.log_changes_event(acc_id, "API Key", "Change", "Failed")
    
    def check_ssh_keyname_reuse(self, new_username, new_key_name, existing_data):
        for entry in existing_data:
            existing_username = self.decrypt_information(entry['username'])
            existing_key_name = self.decrypt_information(entry['key_name'])
            if existing_username == new_username and existing_key_name == new_key_name:
                return True
        return False
    
    def check_ssh_key_reuse(self, public_key, private_key, existing_data):
        for entry in existing_data:
            decrypted_pub_key = self.decrypt_information(entry['public_key'])
            decrypted_priv_key = self.decrypt_information(entry['private_key'])
            if decrypted_pub_key == public_key and decrypted_priv_key == private_key:
                return True
        return False
    
    def is_valid_ssh_private_key(self, private_key):
        if not private_key.startswith("-----BEGIN OPENSSH PRIVATE KEY-----"):
            return False
    
    def is_valid_ssh_public_key(self, public_key):
        if not public_key.startswith("ssh-rsa"):
            return False
    
    def add_ssh_key(self, username, key_name, private_key, public_key, password_protected, passphrase=None):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(SSH):
            data = []
        else:
            try:
                with open(SSH, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_ssh_keyname_reuse(username, key_name, data):
            print(colored(f"[-] The key name '{key_name}' already exists for this username!", "red"))
            return
        if self.check_ssh_key_reuse(public_key, private_key, data):
            print(colored("[-] The key has been used to other Key Name. (Both Key not added) Avoid using the same Key on other Key Name!!", "red"))
            return
        ssh_key_entry = {
            'key_id': unique_id,
            'username': self.encrypt_information(username),
            'key_name': self.encrypt_information(key_name),
            'public_key': self.encrypt_information(public_key),
            'private_key': self.encrypt_information(private_key),
            'passphrase': self.encrypt_information(passphrase) if passphrase else 'null',
            'password_protected': password_protected,
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(ssh_key_entry)
        with open(SSH, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] SSH Key added! Key ID for this Key: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "SSH Key", "Add", "Success")
    
    def get_private_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No SSH Keys Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                decrypted_priv_key = self.decrypt_information(entry['private_key'])
                return decrypted_priv_key
        return None
    
    def get_public_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No SSH Keys Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                decrypted_pub_key = self.decrypt_information(entry['public_key'])
                return decrypted_pub_key
        return None
    
    def get_passphrase_private_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No SSH Keys! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                encrypted_passphrase = entry['passphrase']
                if encrypted_passphrase.lower() == 'null':
                    return 'null'
                else:
                    passphrase = self.decrypt_information(encrypted_passphrase)
                    return passphrase.lower() if passphrase else None
        return None
    
    def delete_ssh_key(self):
        try:
            key_id = int(input(colored("[*] Key ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid Key ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
        if not os.path.exists(SSH):
            print(colored("[-] No SSH Keys saved. Deletion failed", "red"))
            self.log_changes_event(key_id, "SSH Key", "Delete", "Failed")
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            self.log_changes_event(key_id, "SSH Key", "Delete", "Failed")
            return
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No SSH Keys Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['key_id'] == key_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(SSH, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] SSH Key successfully deleted!", "green"))
            self.log_changes_event(key_id, "SSH Key", "Delete", "Success")
            if not data:
                os.remove(SSH)
                return
        else:
            print(colored("[-] SSH Key not found! Deletion failed!", "red"))
            self.log_changes_event(key_id, "SSH Key", "Delete", "Failed")
    
    def change_ssh_key(self, key_id):
        data = []
        if not os.path.exists(SSH):
            print(colored("[-] No SSH Keys saved!", "red"))
            return
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No SSH Keys Saved! Changing Failed!", "red"))
            self.log_changes_event(key_id, "SSH Key", "Change", "Failed")
            return
        except json.JSONDecodeError:
            pass
        for entry in data:
            if key_id not in [entry['key_id'] for entry in data]:
                print(colored(f"[-] This username {key_id} is not available on your SSH Key vault.", "red"))
                return
        for entry in data:
            if entry["key_id"] == key_id:
                if entry['passphrase'] == 'null':
                    print(colored(f"[i] This key name '{self.decrypt_information(entry.get('key_name'))}' has no passphrase.", "light_grey"))
                    pass
                else:
                    current_passphrase = getpass.getpass(colored(f"[*] Current Passphrase for verification (Kname: {self.decrypt_information(entry.get('key_name'))}): ", "light_blue"))
                    decrypted_passphrase = self.decrypt_information(entry['passphrase'])
                    if current_passphrase != decrypted_passphrase:
                        print(colored("[-] Incorrect current passphrase!", "red"))
                        return
        print(colored("[*] Paste the New Private Key Below (Type 'END' on a new line to finish):", "light_blue"))
        new_private_key_lines = []
        try:
            while True:
                line = input()
                new_private_key_lines.append(line)
                if line.upper() == "END":
                    if len(new_private_key_lines) == 1:
                        print(colored("[-] Editor is empty! Nothing to save!", "red"))
                        self.notify_expiry()
                        self.notify_pin_expiry()
                        break
                    else:
                        break
        except Exception as e:
            print("Error: ", e)
            return
        if new_private_key_lines[-1].upper() == "END" and len(new_private_key_lines) == 1:
            return
        print(colored("[*] Paste the New Public Key Below (Type 'END' on a new line to finish):", "light_blue"))
        new_public_key_lines = []
        try:
            while True:
                line = input()
                new_public_key_lines.append(line)
                if line.upper() == "END":
                    if len(new_public_key_lines) == 1:
                        print(colored("[-] Editor is empty! Nothing to save!", "red"))
                        self.notify_expiry()
                        self.notify_pin_expiry()
                        break
                    else:
                        break
        except Exception as e:
            print(colored("[-] Error: ", e, "red"))
            return
        if new_public_key_lines[-1].upper() == "END" and len(new_public_key_lines) == 1:
            return
        new_private_key = '\n'.join(new_private_key_lines[:-1])
        new_public_key = '\n'.join(new_public_key_lines[:-1])
        if not new_private_key.startswith("-----BEGIN OPENSSH PRIVATE KEY-----") or not new_private_key.endswith("-----END OPENSSH PRIVATE KEY-----"):
            print(colored("[-] Invalid SSH Private Key!", "red"))
            self.log_changes_event(key_id, "SSH Key", "Change", "Failed")
            return
        if not new_public_key.startswith("ssh-rsa"):
            print(colored("[-] Invalid SSH Public Key!", "red"))
            self.log_changes_event(key_id, "SSH Key", "Change", "Failed")
            return
        is_password_protected = False
        passphrase = None
        try:
            new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key))
            for entry in data:
                if entry['key_id'] == key_id:
                    entry['private_key'] = self.encrypt_information(new_private_key)
                    entry['public_key'] = self.encrypt_information(new_public_key)
                    entry['password_protected'] = "False"
                    entry['passphrase'] = 'null'
            with open(SSH, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] SSH Key updated successfully!", "green"))
            self.log_changes_event(key_id, "SSH Key", "Change", "Success")
        except paramiko.ssh_exception.PasswordRequiredException:
            is_password_protected = True
            try:
                if is_password_protected:
                    print(colored("[i] The new private key is Password-Protected!", "light_grey"))
                    new_passphrase = getpass.getpass(colored("[*] Enter the new private key passphrase: ", "light_blue"))
                    re_enter = getpass.getpass(colored("[*] Re-Enter new private key passphrase: ", "light_blue"))
                    if re_enter != new_passphrase:
                        print(colored("[-] New Password did not match. QUITTING!"))
                        self.log_changes_event(key_id, "SSH Key", "Change", "Failed")
                        return
                    new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key), password=new_passphrase)
                else:
                    new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key))
            except Exception as e:
                print(colored(f"[-] {e}", "red"))
                self.log_changes_event(key_id, "SSH Key", "Change", "Failed")
                return
            else:
                for entry in data:
                    if entry['key_id'] == key_id:
                        entry['private_key'] = self.encrypt_information(new_private_key)
                        entry['public_key'] = self.encrypt_information(new_public_key)
                        entry['password_protected'] = "True"
                        entry['passphrase'] = self.encrypt_information(new_passphrase)
                with open(SSH, 'w') as file:
                    json.dump(data, file, indent=4)
                print(colored("[+] SSH Key updated successfully!", "green"))
                self.log_changes_event(key_id, "SSH Key", "Change", "Success")
    
    def check_title_reuse(self, title, existing_data):
        for entry in existing_data:
            decrypted_title = self.decrypt_information(entry['title'])
            if decrypted_title == title:
                return True
        return False
    
    def add_private_note(self, title, note):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(PRIVNOTE):
            data = []
        else:
            try:
                with open(PRIVNOTE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_title_reuse(title, data):
            print(colored(f"[-] The title '{title}' already exists", "red"))
            return
        priv_note_entry = {
            'note_id': unique_id,
            'title': self.encrypt_information(title),
            'note': self.encrypt_information(note),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(priv_note_entry)
        with open(PRIVNOTE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Private Note added! Note ID for this Note: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "Private Note", "Add", "Success")
    
    def get_private_note(self, note_id):
        if not os.path.exists(PRIVNOTE):
            return None
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Private Notes Saved! Retrieving Failed!", "red"))
            return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['note_id'] == note_id:
                decrypted_title = self.decrypt_information(entry['title'])
                decrypted_note = self.decrypt_information(entry['note'])
                return decrypted_note
        return None
    
    def delete_private_note(self):
        try:
            note_id = int(input(colored("[*] Note ID: ", "light_blue")))
        except ValueError:
            print(colored("[-] Invalid Note ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
        if not os.path.exists(PRIVNOTE):
            print(colored("[-] No Private Note saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            self.log_changes_event(note_id, "Private Note", "Delete", "Failed")
            return
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Private Note Saved! Changing Failed!", "red"))
            self.log_changes_event(note_id, "Private Note", "Change", "Failed")
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['note_id'] == note_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(PRIVNOTE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Private Note successfully deleted!", "green"))
            self.log_changes_event(note_id, "Private Note", "Delete", "Success")
            if not data:
                os.remove(PRIVNOTE)
                return
        else:
            print(colored("[-] Private Note not found! Deletion failed!", "red"))
            self.log_changes_event(note_id, "Private Note", "Delete", "Failed")
    
    def check_filename_reuse(self, filename, existing_data):
        for entry in existing_data:
            decrypted_filename = self.decrypt_information(entry['filename'])
            if decrypted_filename == filename:
                return True
        return False
    
    def add_source_code(self, language, filename, code):
        unique_id = int(uuid.uuid4().hex[:4],  16)
        if not os.path.exists(SRCCODE):
            data = []
        else:
            try:
                with open(SRCCODE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_filename_reuse(filename, data):
            print(colored(f"[-] The filename {filename} already exists", "red"))
            return
        source_code_entry = {                                                  
            'code_id': unique_id,
            'language': self.encrypt_information(language),
            'filename': self.encrypt_information(filename),
            'code': self.encrypt_information(code),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(source_code_entry)
        with open(SRCCODE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Source Code added! Code ID for this Code: {colored(unique_id, 'green')}", "light_yellow"))
        self.log_changes_event(unique_id, "Source Code", "Add", "Success")
    
    def get_source_code(self, code_id):
        if not os.path.exists(SRCCODE):
            return None
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
             print(colored("[-] No Source Code Saved! Changing Failed!", "red"))
             return
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['code_id'] == code_id:
                decrypted_language = self.decrypt_information(entry['language'])
                decrypted_filename = self.decrypt_information(entry['filename'])
                decrypted_code = self.decrypt_information(entry['code'])
                return decrypted_code
        return None
    
    def delete_source_code(self):
        try:
            code_id = int(input(colored("[*] Code ID: ", "light_blue")))
        except ValueError:                                     
            print(colored("[-] Invalid Code ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "light_blue"))
        if not os.path.exists(SRCCODE):
            print(colored("[-] No Source Code saved. Deletion failed", "red"))
            self.log_changes_event(code_id, "Source Code", "Delete", "Failed")
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        decrypted_master_password = self.decrypt_information((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(decrypted_master_password, master_pass + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            self.log_changes_event(code_id, "Source Code", "Delete", "Failed")
            return
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(colored("[-] No Source Code Saved! Retrieval Failed!", "red"))
            return
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['code_id'] == code_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(SRCCODE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Source Code successfully deleted!", "green"))
            self.log_changes_event(code_id, "Source Code", "Delete", "Success")
            if not data:
                os.remove(SRCCODE)
                return
        else:
            print(colored("[-] Source Code not found! Deletion failed!", "red"))
            self.log_changes_event(code_id, "Source Code", "Delete", "Failed")
    
    def encrypt_information(self, information):
        return self.cipher.encrypt(information.encode()).decode()
    
    def decrypt_information(self, encrypted_information):
        return self.cipher.decrypt(encrypted_information.encode()).decode()
    
    def logout(self):
        self.master_password = None
        self.cipher = None
        print(colored("[..] Logging Out......", "light_cyan"))
        time.sleep(4)
        print(colored("[i] Logged Out!", "light_grey"))

if __name__ == '__main__':
    if platform.system() == 'Linux':
        if not check_linux_privileges():
            print(colored("[-] Mira requires elevated privileges on Linux. QUITTING!", "red"))
            time.sleep(8)
            sys.exit()
        else:
            try:
                move_to_bin()
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[..] Starting Mira Password Manager.....", "light_cyan"))
                password_manager = PasswordManager()
                time.sleep(20)
                if password_manager.lockout_time and time.time() < password_manager.lockout_time:                                         
                    clear_terminal()
                    print(colored(blehhh, "red"))
                    print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                    time.sleep(5)
                    sys.exit()
                clear_terminal()
                print(colored(wolf, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    
                    elif choice == 'regis':
                        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))                                                         
                        else:
                            username = input(colored("[*] New Username: ", "light_blue"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "light_blue"))                                     
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "light_blue"))                                       
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "light_blue"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[i] Master Password: {colored(master_password, 'light_green')}", "light_grey"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "light_blue"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[*] Please enter a new master password.", "light_blue"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    
                    elif choice == 'log':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        if os.path.exists(USER_DATA_FILE):
                            login_username = input(colored("[*] Username: ", "light_blue"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "light_blue"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "light_blue"))
                            password_manager.login(login_username, master_password, encryption_key)
                            password_manager.get_username_log(login_username)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    
                    elif choice == 'help' or choice == 'h':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        print(colored("[*] Available Commands:", "light_blue"))
                        choices = ["- log: Login (Make sure you're registered before attempt to login)", "- regis: Register for new user (Only one user!)", "- quit: Terminate MIRA", 
                                   "- dec_mnemonic: Decode a mnemonic phrase", "- about: More information about MIRA"]
                        for choice in choices:
                            print(colored(choice, "light_green"))
                    
                    elif choice == 'dec_mnemonic':                                                                                                                   
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))                                                                                                                
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "light_blue"))
                        chosen_language = input(colored("[*] Language: ", "light_blue"))
                        if not mnemonic_phrase:
                            print(colored("[-] No mnemomic phrase provided", "red"))
                            continue
                        try:
                            if not chosen_language:
                                print(colored("[i] No language provided, default to English.", "light_grey"))
                                chosen_language = "english"
                            mnemonic = Mnemonic(chosen_language)
                            key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                            key_base64 = base64.b64encode(key_bytes).decode()                                                                                            
                            encryption_key = key_base64.replace('+', '-').replace('/', '_')
                            print(colored(f"[+] Encryption Key: {colored(encryption_key, 'green')}", "light_yellow"))
                        except ValueError:
                            print(colored("[-] Insufficient number of words or not the correct language.", "red"))
                            continue
                        except ConfigurationError as e:
                            print(colored(f"[-] {e}", "red"))
                            continue
                    
                    elif choice == 'quit':
                        print(colored("\n[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(remember, "cyan"))
                        print(colored("[##] Protecting passwords is like leading a team of wolves through the wilderness: every step must be calculated, every move strategic, and trust must be absolute. In this digital age, where predators lurk around every corner, it takes more than just strength to keep your data safe; it takes wisdom, vigilance, and the courage to face the unknown.", "cyan"))
                        time.sleep(8)
                        sys.exit()
                    
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(wolf, "cyan"))
                        print(colored(about, "cyan"))
                    
                    elif choice == 'clear':
                        clear_terminal()
                    
                    else:
                        similar_command = password_manager.find_similar_login_command(choice)
                        if similar_command:
                            print(colored(f"[-] Invalid Command. Did you mean '{similar_command}'?", "red"))
                        else:
                            print(colored("[-] Invalid Command", "red"))
            except (KeyboardInterrupt, EOFError):
                try:
                    password_manager = PasswordManager()
                    print(colored("[-] Exiting Mira.....", "red"))
                    time.sleep(3)
                    clear_terminal()
                    print(colored(remember, "cyan"))
                    print(colored("[##] Protecting passwords is like leading a team of wolves through the wilderness: every step must be calculated, every move strategic, and trust must be absolute. In this digital age, where predators lurk around every corner, it takes more than just strength to keep your data safe; it takes wisdom, vigilance, and the courage to face the unknown.", "cyan"))
                    time.sleep(8)
                    sys.exit()
                except KeyboardInterrupt:
                    password_manager = PasswordManager()
                    sys.exit()

    elif platform.system() == 'Windows':
        if not check_windows_privileges():
            print(colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red"))
            time.sleep(8)
            sys.exit()
        else:
            try:
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[..] Starting Mira Password Manager.....", "light_cyan"))
                password_manager = PasswordManager()
                time.sleep(20)
                if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                    clear_terminal()
                    print(colored(blehhh, "red"))
                    print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                    time.sleep(5)
                    sys.exit()
                clear_terminal()
                print(colored(wolf, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    
                    elif choice == 'regis':
                        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))
                        else:
                            username = input(colored("[*] New Username: ", "light_blue"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "light_blue"))                            
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "light_blue"))                              
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "light_blue"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[i] Master Password: {colored(master_password, 'light_green')}", "light_grey"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "light_blue"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[*] Please enter a new master password.", "light_blue"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    
                    elif choice == 'log':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        if os.path.exists(USER_DATA_FILE):
                            login_username = input(colored("[*] Username: ", "light_blue"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "light_blue"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "light_blue"))
                            password_manager.login(login_username, master_password, encryption_key)
                            password_manager.get_username_log(login_username)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    
                    elif choice == 'help' or choice == 'h':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        print(colored("[*] Available Commands:", "light_blue"))
                        choices = ["- log: Login (Make sure you're registered before attempt to login)", "- regis: Register for new user (Only one user!)", "- quit: Terminate MIRA", 
                                   "- dec_mnemonic: Decode a mnemonic phrase", "- about: More information about MIRA"]
                        for choice in choices:
                            print(colored(choice, "light_green"))
                    
                    elif choice == 'dec_mnemonic':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. Too many failed login attempts. If you are the legitimate user, please try again in {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            time.sleep(5)
                            sys.exit()
                        mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "light_blue"))
                        chosen_language = input(colored("[*] Language: ", "light_blue"))
                        if not mnemonic_phrase:
                            print(colored("[-] No mnemonic phrase provided!", "red"))
                            continue
                        try:
                            if not chosen_language:
                                print(colored("[i] No language provided, default to English.", "light_grey"))
                                chosen_language = "english"
                            mnemonic = Mnemonic(chosen_language)
                            key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                            key_base64 = base64.b64encode(key_bytes).decode()
                            encryption_key = key_base64.replace('+', '-').replace('/', '_')
                            print(colored(f"[+] Encryption Key: {colored(encryption_key, 'green')}", "light_yellow"))
                        except ValueError:
                            print(colored("[-] Insufficient number of words or not the correct language.", "red"))
                            continue
                        except ConfigurationError as e:
                            print(colored(f"[-] {e}", "red"))
                            continue
                    
                    elif choice == 'quit':
                        print(colored("[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(remember, "cyan"))
                        print(colored("[##] Protecting passwords is like leading a team of wolves through the wilderness: every step must be calculated, every move strategic, and trust must be absolute. In this digital age, where predators lurk around every corner, it takes more than just strength to keep your data safe; it takes wisdom, vigilance, and the courage to face the unknown.", "cyan"))
                        time.sleep(8)
                        sys.exit()
                    
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(wolf, "blue"))
                        print(colored(about, "cyan"))
                    
                    elif choice == 'clear':
                        clear_terminal()
                    
                    else:
                        similar_command = password_manager.find_similar_login_command(choice)
                        if similar_command:
                            print(colored(f"[-] Invalid Command. Did you mean '{similar_command}'?", "red"))
                        else:
                            print(colored("[-] Invalid Command", "red"))

            except (KeyboardInterrupt, EOFError):
                try:
                    print(colored("[-] Exiting Mira.....", "red"))
                    time.sleep(3)
                    clear_terminal()
                    print(colored(remember, "cyan"))
                    print(colored("[##] Protecting passwords is like leading a team of wolves through the wilderness: every step must be calculated, every move strategic, and trust must be absolute. In this digital age, where predators lurk around every corner, it takes more than just strength to keep your data safe; it takes wisdom, vigilance, and the courage to face the unknown.", "cyan"))
                    time.sleep(8)
                    sys.exit()
                except KeyboardInterrupt:
                    sys.exit()

