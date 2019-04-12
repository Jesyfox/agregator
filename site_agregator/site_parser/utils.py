
def add_post_to_db(data):
    print('data:')
    for k, i in data.items():
        if k != 'body_content':
            print(f'\t{k} --> {i}')
