# telegram-backup
* Python >= 3.7
* telegram-backup - 
***
# Data:
This simple script save data about:
- [x] Users
- [x] Channes
- [x] Groups

* For private groups or channels, it is not possible to create or get a save link, but the script saves the name, you can later find this group by name.


**Backup data schema:**
```
{
    users: [
        {
            name: string,
            username: string | null,
            phone: string | null,
            bot: boolean
        }
    ],
    channels: [
        {
            name: string,
            username: string,
            link: string,
            participants_count: number
        }
    ],
    groups: [
        {
            name: string,
            title: string,
            link: string
        }
    ],
    unsaved: {
        channels: [
            {
                name: string
            }
        ],
        groups: [
            {
                name: string
            }
        ]
    }
}
```
***
# Installation:
```console
git clone https://github.com/Normalizex/telegram-backup

python -m pip install telethon
```
***
# Usage:
These example values won't work. You must get your own api_id and
api_hash from https://my.telegram.org, under API Development.

```console
python main.py

#https://my.telegram.org
Api ID =>10923443
Api Hash =>7361e8795bf4563f453e3e30dbce8249

#only on first launch or on another account
Please enter your phone (or bot token): [your number]
Please enter the code you received: [code]#paste code from telegram notify service (in client)
Signed in successfully as [username]

#done
Saved into: backup-[time].json
````
