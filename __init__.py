from opsdroid.matchers import match_regex


@match_regex(r'reload')
async def reload(opsdroid, config, message):
    await message.respond("Reloading skills")
    opsdroid.restart()


@match_regex(r'quit')
async def reload(opsdroid, config, message):
    await message.respond("Stopping opsdroid")
    opsdroid.stop()
