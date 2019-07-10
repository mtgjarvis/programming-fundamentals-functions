docu = 'Shark Water'
drama = 'Three Billboards Outside Ebbing Missouri'
comedy = 'Deadpool 2'
dramedy = 'Little Miss Sunshine'
book = 'Blood Meridian'

print('Do you like documentaries? Yes or No')
media_docu = input().lower()

print('Do you like dramas? Yes or No')
media_drama = input().lower()

print('Do you like comedies? Yes or No')
media_comedy = input().lower()


if media_docu == 'yes':
    print('May I reccomed {}'.format(docu))
elif media_drama == 'yes':
    print('May I reccomed {}'.format(drama))
elif media_comedy == 'yes':
    print('May I reccomed {}'.format(comedy))
elif media_comedy == 'yes' and media_drama == 'yes':
    print('May I reccomed {}'.format(dramedy))
else:
    print('May I reccomed {}'.format(book))
        