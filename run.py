from Booking.booking import Booking
import time


try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency()
        bot.select_place_to_go(input("where you want to go"))
        bot.select_dates(check_indate=input("check in date"),check_outdate=input("check out date"))
        bot.select_no_person(int(input("no person")))
        bot.click_search()
        bot.apply_filtration()

except Exception as e:
    if 'in PAth' in str(e):
        print("please add to PAth your selenium drivers \n",
            "set PATH=%PATH%;C:path-to-your-folder")
    else:
        raise
