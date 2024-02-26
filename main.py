global loggedin  # inserted
import requests
import threading
import string
import random
import colorama
import os
import bs4
import time
import subprocess
loggedin = False
try:
    cookies = open('cookies.txt', 'r').read().splitlines()
    proxies = open('proxies.txt', 'r').read().splitlines()
except:
    print('- You need cookies.txt and proixes.txt')
    input()
    quit()
os.system('title Skillfuel v3.0')
colorama.init()

def reboot():
    file_name = 'Skillfuel'
    dir = os.listdir()
    for i in dir:
        if i.split('.')[0] == file_name:
            file_name = i
            os.startfile(i)
            quit()
    print('-> If you see this message the auto opener is broken.')
    input()
    quit()

def check_cookie(cookie):
    with requests.session() as session:
        try:
            session.cookies['.ROBLOSECURITY'] = cookie
            users = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
            print(f'-> Valid | {users}')
            open('checked_cookies.txt', 'a').write(f'{cookie}\n')
        except:
            print('-> Not Valid')

def select_cookie_checker():
    for x in cookies:
        threading.Thread(target=check_cookie, args=(x,)).start()
    input()
    reboot()

def check_description(cookie):
    with requests.session() as session:
        try:
            session.cookies['.ROBLOSECURITY'] = cookie
            desc = session.get('https://accountinformation.roblox.com/v1/description').json()['description']
            print(f'-> {desc}')
        except:
            print('-> ERROR_UNKNOWN')

def select_check_description():
    for x in cookies:
        threading.Thread(target=check_description, args=(x,)).start()
    input()
    reboot()

def check_proxy(proxy):
    with requests.session() as session:
        try:
            session.proxies = {'http': proxy, 'https': proxy}
            roblox = session.get('http://www.roblox.com')
            if roblox.status_code == 200:
                print(f'-> VALID | {proxy}')
                open('checked_proxies.txt', 'a').write(f'{proxy}\n')
        except:
            print(f'-> INVALID | {proxy}')

def select_proxies_checker():
    for x in proxies:
        threading.Thread(target=check_proxy, args=(x,)).start()
    input()
    reboot()

def change_theme(type, cookie):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            if type == 1:
                s = session.patch('https://accountsettings.roblox.com/v1/themes/user', data={'themeType': 'Light'})
            else:  # inserted
                s = session.patch('https://accountsettings.roblox.com/v1/themes/user', data={'themeType': 'Dark'})
            print(f'- Changed Theme Type | {s.status_code}')
    except:
        print('- Unable to Change')

def select_theme_change():
    print('- Background Theme Selection:\n[1]: Light\n[2]: Dark')
    selec = input('>>> ')
    selec = int(selec)
    for x in cookies:
        threading.Thread(target=change_theme, args=(selec, x)).start()
    input()
    reboot()

def select_proxy_scraper():
    print('- Locating proxies...')
    gproxies = ''
    for x in requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').iter_content(chunk_size=1028):
        if x:
            x = x.decode()
            gproxies += x
    gproxies = gproxies.splitlines()
    print(f'- Found {len(gproxies)} | Downloading..')
    with open('scraped_proxies.txt', 'a') as scraped:
        for proxy in gproxies:
            scraped.write(f'{proxy}\n')
    print('- Downloaded to scraped_proxies.txt | FINISHED')
    input()
    reboot()

def check_robux(cookie):
    try:
        @requests.session()
        with session:
            session.cookies['.ROBLOSECURITY'] = cookie
            balance = session.get('https://api.roblox.com/currency/balance').json()['robux']
            if int(balance) > 0:
                open('robux_cookies.txt', 'a').write(f'{cookie}\n')
            print(f'- BALANCE | {balance}')
    except:
        print('- INVALID COOKIE')

def select_robux_checker():
    for x in cookies:
        @threading.Thread(target=check_robux, args=(x,)).start()
        break
    input()
    reboot()

def change_display_name(cookie, name_):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            userid = session.get('https://users.roblox.com/v1/users/authenticated').json()['id']
            display_name = session.patch(f'https://users.roblox.com/v1/users/{userid}/display-names', json={'newDisplayName': name_})
            print(f'- Display Name | {display_name.status_code}')
    except:
        print('- INVALID COOKIE')

def select_display_name_bot():
    print('- Select Display Name: ')
    name_ = input('>>> ')
    for x in cookies:
        @threading.Thread(target=change_display_name, args=(x, name_)).start()
        break
    input()
    reboot()

def send_friend(cookie, userid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            friend = session.post(f'https://friends.roblox.com/v1/users/{userid}/request-friendship')
            print(f'- Friend Request | {friend.status_code}')
    except:
        print('- INVALID COOKIE')

def select_friend_request_bot():
    print('- Enter UserId: ')
    userid = input('>>> ')
    for x in cookies:
        threading.Thread(target=send_friend, args=(x, userid)).start()
    input()
    reboot()

def send_follow(cookie, userid):
    for x in range(50):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
                follow = session.post(f'https://friends.roblox.com/v1/users/{userid}/follow', proxies={'http': random.choice(proxies), 'https': random.choice(proxies)}, timeout=500)
                if follow.status_code == 200:
                    print(f'- Follow Bot | {follow.status_code}')
                else:  # inserted
                    print(f'- Failed Captcha | {follow.status_code}')
        except:
            pass

def select_follow_bot():
    print('- Enter UserId: ')
    userid = input('>>> ')
    for x in cookies:
        threading.Thread(target=send_follow, args=(x, userid)).start()
    input()
    reboot()

def send_favorite(cookie, assetid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            fav = session.post('https://www.roblox.com/favorite/toggle', data={'assetID': assetid}, proxies={'http': random.choice(proxies), 'https': random.choice(proxies)}, timeout=500)
            print(f'- Favortie Bot | {fav.status_code}')
    except:
        pass

def select_favorite_bot():
    print('- Enter AssetId: ')
    asset = input('>>> ')
    for x in cookies:
        threading.Thread(target=send_favorite, args=(x, asset)).start()
    input()
    reboot()

def select_game_joiner():
    print('- Enter GameId: ')
    gameid = input('>>> ')
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = random.choice(cookies)
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            session.headers['referer'] = f'https://www.roblox.com/games/{gameid}/'
            auth = session.post('https://auth.roblox.com/v1/authentication-ticket/').headers['rbx-authentication-ticket']
            browserId = random.randint(1000000, 10000000)
            ticket = f'roblox-player:1+launchmode:play+gameinfo:{auth}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameid}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:'
            os.startfile(ticket)
            print('- Launched Game | UNKNOWN')
        input()
        reboot()
    except:
        print('- Failed to Launch (Cookies)')
        input()
        reboot()

def select_roblox_visit_bot():
    print('- Enter GameId: ')
    gameid = input('>>> ')
    while True:  # inserted
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = random.choice(cookies)
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
                session.headers['referer'] = f'https://www.roblox.com/games/{gameid}/'
                auth = session.post('https://auth.roblox.com/v1/authentication-ticket/').headers['rbx-authentication-ticket']
                browserId = random.randint(1000000, 10000000)
                ticket = f'roblox-player:1+launchmode:play+gameinfo:{auth}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameid}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:'
                os.startfile(ticket)
                print('- Launched Game | UNKNOWN')
        except:
            print('- Failed to Launch (Cookies)')
        time.sleep(20)

def change_social(cookie, youtube, facebook, twitter, twitch):
    with requests.session() as session:
        try:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            s = session.post('https://accountinformation.roblox.com/v1/promotion-channels', data={'facebook': facebook, 'youtube': youtube, 'twitch': twitch, 'twitter': twitter, 'promotionChannelsVisibilityPrivacy': 'AllUsers'})
            print(f'- Promotion Channels | {s.status_code}')
        except:
            print('- Failed (cookies)')

def select_promotion_bot():
    print('- Enter your Youtube URL: / You can leave empty to skip')
    yt = input('>>> ')
    print('- Enter your Twitter URL: / You can leave empty to skip')
    twitter = input('>>> ')
    print('- Enter your Twitch URL: / You can leave empty to skip')
    twitch = input('>>> ')
    print('- Enter your Facebook URL: / You can leave empty to skip')
    facebook = input('>>> ')
    print('========================================================================================')
    for x in cookies:
        threading.Thread(target=change_social, args=(x, yt, facebook, twitter, twitch)).start()
    input()
    reboot()

def change_description(cookie, desc):
    with requests.session() as session:
        try:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            desc = session.post('https://accountinformation.roblox.com/v1/description', data={'description': desc})
            print(f'- Description | {desc.status_code}')
        except:
            print('- Failed (cookie)')

def select_description_change():
    print('- Enter Description')
    desc = input('>>> ')
    for x in cookies:
        threading.Thread(target=change_description, args=(x, desc)).start()
    input()
    reboot()

def send_ally(cookie, groupId):
    try:
        @requests.session()
        with session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            ally = session.post('https://groups.roblox.com/v1/groups/', proxies=f'{groupId}/relationships/allies/{random.randint(1, 5420999)}', timeout={'http': random.choice(proxies), 'https': random.choice(proxies)}, timeout=500)
            print(f'- Ally Bot | {ally.status_code}')
    except:
        pass

def select_group_ally_bot():
    print('- Using first cookie in cookies.txt')
    print('- Enter your GroupId: ')
    groupid = input('>>> ')
    while True:  # inserted
        threading.Thread(target=send_ally, args=(cookies[0], groupid)).start()

def buy_model(productId, OwnerId, AssetId):
    while True:  # inserted
        try:
            cookie = random.choice(cookies)
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = random.choice(cookies)
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
                buy = session.post('https://economy.roblox.com/v1/purchases/products/', data=f'{productId}', proxies={'expectedCurrency': 1, 'expectedPrice': 0, 'expectedSellerId': OwnerId}, timeout={'http': random.choice(proxies), 'https': random.choice(proxies)}, buy=1500)
                delete = session.post('https://www.roblox.com/asset/delete-from-inventory', data={'assetId': AssetId})
                print(f'- Model Bot | {buy.status_code} | {delete.status_code}')
        except:
            pass

def select_model_bot():
    print('- Enter AssetId: ')
    asset = input('>>> ')
    with requests.session() as session:
        print('- Finding a valid cookie..')
        while True:  # inserted
            try:
                session.cookies['.ROBLOSECURITY'] = random.choice(cookies)

                @session.post('https://friends.roblox.com/v1/users/1/unfriend')
                session.headers['x-csrf-token'] = session.headers['x-csrf-token']
                info = session.post('https://catalog.roblox.com/v1/catalog/items/details', json={'items': [{'itemType': 'Asset', 'id': asset}]})
                productid = info.json()['data'][0]['productId']
                userid = info.json()['data'][0]['creatorTargetId']
                break
            except:
                pass
    for x in range(1000):
        threading.Thread(target=buy_model, args=(productid, userid, asset)).start()

def equip_item(cookie, asset):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
            wear = session.post(f'https://avatar.roblox.com/v1/avatar/assets/{asset}/wear')
            print(f'- Wear Asset | {wear.status_code}')
    except:
        print('- Failed (cookie)')

def select_equip_item_bot():
    print('- Enter AssetId: ')
    asset = input('>>> ')
    for x in cookies:
        @threading.Thread(target=equip_item, args=(x, asset)).start()
        break
    input()
    reboot()

def dequip_item(cookie, asset):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
            wear = session.post(f'https://avatar.roblox.com/v1/avatar/assets/{asset}/remove')
            print(f'- Wear Asset | {wear.status_code}')
    except:
        print('- Failed (cookie)')

def select_dequip_item_bot():
    print('- Enter AssetId: ')
    asset = input('>>> ')
    for x in cookies:
        threading.Thread(target=dequip_item, args=(x, asset)).start()
    input()
    reboot()

def kill_cookie(cookie):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
            out = session.post('https://auth.roblox.com/v2/logout')
            print(f'- Killed Cookie | {out.status_code}')
    except:
        print('- Failed (cookie)')

def select_cookie_killer():
    print('- WARNING: YOU ARE ABOUT TO DESTROY YOUR COOKIES ARE YOU SURE TO PROCEED: [Y/N]')
    s = input('>>> ')
    if s == 'Y' or s == 'y':
        pass
    else:  # inserted
        reboot()
        quit()
    for x in cookies:
        threading.Thread(target=kill_cookie, args=(x,)).start()
    input()
    reboot()

def check_cookie_ver(cookie):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            verified = session.get('https://accountsettings.roblox.com/v1/email').json()['verified']
            if verified == True:
                open('verified_cookies.txt', 'a').write(f'{cookie}\n')
            print(f'- Verified Checker | {verified}')
    except:
        print('- Failed (cookie)')

def select_verified_checker():
    for x in cookies:
        threading.Thread(target=check_cookie_ver, args=(x,)).start()
    input()
    reboot()

def join_game(gameid):
    try:
        @requests.session()
        with sessions:
            sessions.cookies['.ROBLOSECURITY'] = random.choice(cookies)
            sessions.headers['x-csrf-token'] = sessions.post('https://auth.roblox.com/v1/authentication-ticket/').headers['x-csrf-token']
            sessions.headers['referer'] = 'https://www.roblox.com'
            auth = sessions.post('https://auth.roblox.com/v1/authentication-ticket/').headers['rbx-authentication-ticket']
            bbid = random.randint(1000000, 100000000)
            os.startfile(f'roblox-player:1+launchmode:play+gameinfo:{auth}+launchtime:{bbid}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{bbid}%26placeId%3D{gameid}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{bbid}+robloxLocale:en_us+gameLocale:en_us+channel:')
            print('- Instance | Finished')
    except:
        pass

def select_player_bot():
    print('- Please run a multi-instance')
    print('- Enter GameId: ')
    gameid = input('>>> ')
    print('- Enter Amount of Instances: ')
    instance_count = input('>>> ')
    for x in range(int(instance_count)):
        print('- Launching instance...')
        threading.Thread(target=join_game, args=(gameid,)).start()
        print('- Sent Instance!')
        time.sleep(15)
    input()
    reboot()

def send_pm(userid, message, title):
    try:
        proxy = {'http': random.choice(proxies), 'https': random.choice(proxies)}

        @requests.session()
        with session:
            session.cookies['.ROBLOSECURITY'] = random.choice(cookies)
            milliseconds = int(round(time.time() * 1000))
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
            send = session.post('https://privatemessages.roblox.com/v1/messages/send', data={'body': message, 'cacheBuster': milliseconds, 'recipientid': userid, 'subject': title}, proxies=proxy, timeout=500)
    except:
        pass

def select_pm_bot():
    print('- Enter Title: ')
    tit = input('>>> ')
    print('- Enter Body: ')
    body = input('>>> ')
    print('- Enter UserId: ')
    userid = input('>>> ')
    while True:  # inserted
        threading.Thread(target=send_pm, args=(userid, body, tit)).start()
        time.sleep(0.001)

def send_online(cookie):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfriend').headers['x-csrf-token']
            online = session.post('https://presence.roblox.com/v1/presence/register-app-presence')
            print(f'- Online | {online.status_code}')
    except:
        print('- Failed (cookie)')

def select_online_bot():
    for x in cookies:
        threading.Thread(target=send_online, args=(x,)).start()
    input()
    reboot()

def send_unfollow(cookie, userid):
    for x in range(50):
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = cookie
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
                unfollow = session.post(f'https://friends.roblox.com/v1/users/{userid}/unfollow', data={'targetUserId': userid})
                print(f'- Unfollow Bot | {unfollow.status_code}')
        except:
            pass

def select_unfollow_bot():
    print('- Enter UserId: ')
    userid = input('>>> ')
    for x in cookies:
        @threading.Thread(target=send_unfollow, args=(x, userid)).start()
        break
    input()
    reboot()

def create_cookie(username_prefix):
    try:
        with requests.session() as session:
            proxy = {'http': random.choice(proxies), 'https': random.choice(proxies)}
            agents = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36', 'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4']
            session.headers['user-agent'] = random.choice(agents)
            try:
                session.headers['x-csrf-token'] = session.post('https://auth.roblox.com/v2/signup').headers['x-csrf-token']
            except:
                session.headers['x-csrf-token'] = session.post('https://auth.roblox.com/v2/signup', proxies=proxy).headers['x-csrf-token']
            gender = random.randint(1, 3)
            username = username_prefix + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=5))
            password = f''.join(random.choices(string.ascii_letters + string.ascii_uppercase, k=10))
            forum = {'birthday': '21 Oct 2006', 'captchaProvider': '', 'captchaToken': '', 'isTosAgreementBoxChecked': True, 'gender': gender, 'displayAvatarV2': False, 'displayContextV2': False, 'password': password, 'username': username}
            create = session.post('https://auth.roblox.com/v2/signup', data=forum, proxies=proxy, timeout=500)
            if create.status_code == 200:
                cookie = session.cookies['.ROBLOSECURITY']
                with open('cookie_gen.txt', 'a') as gen:
                    gen.write(f'{cookie}\n')
                print(f'- Generated Cookie | {create.status_code}')
    except:
        return

def select_cookie_gen():
    print('- This could take a while depending on the Captchas.')
    print('- Enter Username Prefix: ')
    prefix = input('>>> ')
    while True:  # inserted
        threading.Thread(target=create_cookie, args=(prefix,)).start()

def apply_vote(cookie, asset, vote):
    with requests.session() as session:
        try:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
            vote = session.post('https://www.roblox.com/voting/vote', params={'assetId': asset, 'vote': vote}, proxies={'http': random.choice(proxies), 'https': random.choice(proxies)})
            print(f'- Applied Vote | {vote.status_code}')
        except:
            pass

def join_game_vote(cookie, gameid):
    try:
        with requests.session() as sessions:
            sessions.cookies['.ROBLOSECURITY'] = cookie
            sessions.headers['x-csrf-token'] = sessions.post('https://auth.roblox.com/v1/authentication-ticket/').headers['x-csrf-token']
            sessions.headers['referer'] = 'https://www.roblox.com'
            auth = sessions.post('https://auth.roblox.com/v1/authentication-ticket/').headers['rbx-authentication-ticket']
            bbid = random.randint(1000000, 100000000)
            os.startfile(f'roblox-player:1+launchmode:play+gameinfo:{auth}+launchtime:{bbid}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{bbid}%26placeId%3D{gameid}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{bbid}+robloxLocale:en_us+gameLocale:en_us+channel:')
            print('- Instance | Finished')
    except:
        pass

def select_vote_bot():
    print('- You will need verified cookies')
    print('[1]: Like Bot | [2]: Dislike Bot')
    sel = input('>>> ')
    if sel == '1':
        sel = True
    else:  # inserted
        sel = False
    print('- Enter GameId: ')
    gameid = input('>>> ')
    for x in cookies:
        threading.Thread(target=join_game_vote, args=(x, gameid)).start() + time.sleep(15)
        threading.Thread(target=apply_vote, args=(x, gameid, sel)).start()
    input()
    reboot()

def send_report(userId):
    while True:  # inserted
        try:
            with requests.session() as session:
                session.cookies['.ROBLOSECURITY'] = random.choice(cookies)
                proxy = {'http': random.choice(proxies), 'https': random.choice(proxies)}
                session.proxies = proxy
                session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/accept-friend-request').headers['x-csrf-token']
                token = session.get(f'https://www.roblox.com/abusereport/userprofile?id={userId}').text.split('<input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"')[1].split('\">')[0]
                report = session.post(f'https://www.roblox.com/abusereport/userprofile?id={userId}', data={'__RequestVerificationToken': token, 'ReportCategory': 1, 'Comment': '', 'Id': userId, 'RedirectUrl': 'https://www.roblox.com/Login', 'PartyGuid': '', 'ConversationId': ''})
                print(f'- Report Bot | {report.status_code}')
        except:
            pass

def select_mass_report_bot():
    print('- Enter UserId: ')
    userid = input('>>> ')
    for x in range(1000):
        threading.Thread(target=send_report, args=(userid,)).start()
    input()
    quit()

def check_whitelist():
    global loggedin  # inserted
    if loggedin == False:
        loggedin = True
        content = requests.get('https://pastebin.com/S1zNZ82S')
        content = bs4.BeautifulSoup(content.content, 'html.parser')
        content = content.find(class_='textarea').get_text().strip()
        uuid = subprocess.getoutput('wmic csproduct get uuid').split('UUID')[1].strip()
        for x in content.splitlines():
            if x == uuid:
                main()
        print('- You\'re not whitelisted.')
        input('>>> ')
        quit()

def main():
    print(colorama.Fore.WHITE + '========================================================================================')
    print(colorama.Fore.LIGHTBLUE_EX + f'\n                                 ___ _   _ _ _  __          _ \n                                / __| |_(_) | |/ _|_  _ ___| |\n                                \\__ \\ / / | | |  _| || / -_) |\n                                |___/_\\_\\_|_|_|_|  \\_,_\\___|_|\n\n                                - Developer: ssl#0002 \n - Leaked by Bling#9999 / GodBling \n                               - Cookies: {len(cookies)}\n                                - Proxies: {len(proxies)}\n                                - Version: 1.1\n\n')
    print(colorama.Fore.WHITE + '========================================================================================')
    print(colorama.Fore.WHITE + '\n    (1) - Cookie Checker           (11) - Game Join            (21) - Player Bot\n    (2) - Description Checker      (12) - Visit Bot            (22) - PM Spam\n    (3) - Proxies Checker          (13) - Social Network Bot   (23) - Set Online Bot\n    (4) - Dark/Light Theme Bot     (14) - Description Bot      (24) - Unfollow Bot\n    (5) - Proxy Scraper            (15) - Group Ally Bot       (25) - Cookie Gen (BETA)\n    (6) - Robux Checker            (16) - Model Bot            (26) - Like/Dislike Bot\n    (7) - Display Name Bot         (17) - Equip Bot            (27) - Report Bot\n    (8) - Friend Request Bot       (18) - Unequip Bot       \n    (9) - Follow Bot (BETA)        (19) - Cookie Killer\n    (10) - Favorite Bot            (20) - Verified Checker\n    ')
    print(colorama.Fore.WHITE + '========================================================================================')
    selections = [select_cookie_checker, select_check_description, select_proxies_checker, select_theme_change, select_proxy_scraper, select_robux_checker, select_display_name_bot, select_friend_request_bot, select_follow_bot, select_favorite_bot, select_game_joiner, select_roblox_visit_bot, select_promotion_bot, select_description_change, select_group_ally_bot, select_model_bot, select_equip_item_bot, select_dequip_item_bot, select_cookie_killer, select_verified_checker, select_player_bot, select_pm_bot, select_online_bot, select_unfollow_bot, select_cookie_gen, select_vote_bot, select_mass_report_bot]
    colorama.deinit()
    choice = input('>>> ')
    selections[int(choice) - 1]()
