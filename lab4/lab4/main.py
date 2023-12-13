from lab4.CustomArtConsole import CustomArtConsole
#
# font = {
#     'm': '1',
#     'e':'2',
#     's':'3'
# }
# art = CustomArt('hp')
#
# # art._size_x = 10
# # art._size_y = 12
# # art.zoom()
# # print(art.prev_view())
# #
# art.justify = 'right'
# art.create()
# print(art)
#
# art.justify = 'center'
# art.create()
# print(art)
#
#
# art.justify = 'left'
# art.create()
# print(art)
#
#
# import pyfiglet
#
# art = pyfiglet.figlet_format('mess')
#
# print([art])

#
# standard_dic = {
#     'd': u'     _ \n  __| |\n / _` |\n| (_| |\n \\__,_|\n       \n',
#     'h': u" _     \n| |__  \n| '_ \\ \n| | | |\n|_| |_|\n       \n",
#     'l': u' _ \n| |\n| |\n| |\n|_|\n   \n',
#     'p': u"       \n _ __  \n| '_ \\ \n| |_) |\n| .__/ \n|_|    \n",
#     't': u' _   \n| |_ \n| __|\n| |_ \n \\__|\n     \n',
#     'x': u'      \n__  __\n\\ \\/ /\n >  <\n'
# }
#
# def align_text(word, alignment='left'):
#     output_lines = []
#
#     max_lines = max(len(standard_dic.get(letter, '').split('\n')) for letter in word)
#     for line_num in range(max_lines):
#
#         line = ""
#         for letter in word:
#             letter_lines = standard_dic.get(letter, '').split('\n')
#             if line_num < len(letter_lines):
#                 if alignment == 'left':
#
#                     line += letter_lines[line_num].ljust(len(letter_lines[0]) + 1)
#                 elif alignment == 'center':
#
#                     line += letter_lines[line_num].center(len(letter_lines[0]) + 1)
#                 elif alignment == 'right':
#
#                     line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
#             else:
#                 line += ' ' * (len(letter_lines[0]) + 1)
#         output_lines.append(line)
#     print(output_lines)
#     output = '\n'.join(output_lines)
#     return output
#
# word = "hip"
# alignment = 'center'
# if alignment == 'center':
#     word = word.rjust(80, ' ')
#     word.center(0, ' ')
# result = align_text(word, alignment)
# print(result)



#
# import pyfiglet
# art = pyfiglet.figlet_format('hp')
#
# art._size_x = 10
# art._size_y = 12
#
# print(art)


art = CustomArtConsole()
art.run()
