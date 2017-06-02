from opsdroid.matchers import match_regex


@match_regex(r'reload')
async def reload(opsdroid, config, message):
    await message.respond("Reloading skills")
    opsdroid.restart()
    await message.respond("Reloaded")

@match_regex(r'supertest')
async def reloadtest(opsdroid, config, message):
    await message.respond("Testytesttest")
