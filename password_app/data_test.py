data_line = {'google': 'we_wr', '123': '456', 'ASD': 'DFG', '__123__': '__456__'}
expected_create_line = {'google': 'google:we_wr was added to the storage',
                        '123': '123:456 was added to the storage',
                        'ASD': 'ASD:DFG was added to the storage',
                        '__123__': '__123__:__456__ was added to the storage'}
expected_del_line = {'test': 'test:test  was removed from storage', '__': '__:__  was removed from storage',
                     '123': '123:', '!@#': '!@#:$%^  was removed from',
                     '__123__': '__123:__123__  was removed from'}
expected_change_line = {'test': 'test:test was change from storage', '__': '__:__ was change from storage',
                        '123': '123:123 was change from storage', '!@#': '!@#:$%^ was removed from',
                        '__123__': '__123:__123__ was removed from'}
expected_read_line = {'google': 'we_wr', '123': '456', 'ASD': 'DFG', '__123__': '__456__'}
