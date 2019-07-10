docu = 'Shark Water'
drama = 'Three Billboards Outside Ebbing Missouri'
comedy = 'Deadpool 2'
dramedy = 'Little Miss Sunshine'
book = 'Blood Meridian'

print('Rate documentaries on a scale of 1 - 5')
media_docu = input()

print('Rate dramas on a scale of 1 - 5')
media_drama = input()

print('Rate comedies on a scale of 1 - 5')
media_comedy = input()

if media_docu >= 4:
    print('May I reccomed {}'.format(docu))
elif media_docu <= 3 and media_drama >= 4 and media_comedy >= 4:
    print('May I reccomed {}'.format(dramedy))
elif media_drama >= 4 and media_docu < 4 and media_comedy > 4:
    print('May I reccomed {}'.format(drama))
elif media_comedy >= 4 and media_docu < 4 and drama < 4:
    print('May I reccomed {}'.format(comedy))
# elif media_comedy >= 4 and media_drama >= 4:
#     print('May I reccomed {}'.format(dramedy))
else:
    print('May I reccomed {}'.format(book))