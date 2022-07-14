from telethon import TelegramClient, events, functions

import time
import json
import asyncio

async def main():
	api_id = int(input('Api ID =>'))
	api_hash = input('Api Hash =>')
	client = TelegramClient('client', api_id, api_hash)
	await client.start()
	dialogs = await client.get_dialogs()

	data = { "users": [], "channels": [], "groups": [], "unsaved": { "channels": [], "groups": [] } }

	for dialog in dialogs:
		if dialog.is_user and not (dialog.name == '' and not dialog.entity.phone and not dialog.entity.phone):
			data['users'].append({
				"name": dialog.name,
				"username": dialog.entity.username,
				"phone": dialog.entity.phone,
				"bot": dialog.entity.bot
			})
		elif dialog.is_group:
			try:
				result = await client(functions.messages.ExportChatInviteRequest(dialog.entity.id))
				data['groups'].append({
					"name": dialog.name,
					"title": dialog.entity.title,
					"link": result.link
				})
			except:
				data['unsaved']['groups'].append({
					"name": dialog.name,
				})
		elif dialog.is_channel:
			if not dialog.entity.username:
				data['unsaved']['channels'].append({
					"name": dialog.name
				})
			else:
				data['channels'].append({
					"name": dialog.name,
					"username": dialog.entity.username,
					"link": f'https://t.me/{dialog.entity.username}',
					"participants_count": dialog.entity.participants_count
				})


	filename = f'backup-{round(time.time())}.json'
	with open(filename, "w") as fs:
		fs.write(json.dumps(data, indent=4))

	print(f'Saved into: {filename}')

asyncio.run(main())