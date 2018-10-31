from opsdroid.matchers import match_regex
import textwrap


@match_regex(r'reload')
async def reload(opsdroid, config, message):
    await message.respond("Reloading skills")
    await opsdroid.reload()


@match_regex(r'quit')
async def stop_opsdroid(opsdroid, config, message):
    await message.respond("Stopping opsdroid")
    opsdroid.exit()


@match_regex(r'help$')
async def help(opsdroid, config, message):
    await message.respond(textwrap.dedent("""\
    OpsDroid - An open source chat bot framework written in python.

OpsDroid comes with a few simple commands out of the box.
With "Hello" Opsdroid will greet users when they say hello.
With "Goodbye" Opsdroid will say goodbye to them when they leave.
With "when did you last see <user>" Opsdroid can tell you when the user was online.
With "ALLCAPSTEXT" Opsdroid will complain with an image.
With "Dance" Opsdroid will even dance!

To see a list of all active skills just say:
> help skills


You can also add more skills to Opsdroid by uncommenting or adding new skills to the configuration file.
A Configuration file can be found in:
Path: ~/.opsdroid/configuration.yaml


-------
Official site: https://opsdroid.github.io
Documentation files: http://opsdroid.readthedocs.io/en/latest/?badge=latest
Blog:  https://medium.com/opsdroid
Youtube: https://www.youtube.com/channel/UC0FeGkDF7FrshmzAsb9lDvw
GitHub: https://github.com/opsdroid

Get opsdroid working on your computer:
Opsdroid Desktop: https://github.com/opsdroid/opsdroid-desktop
"""))


@match_regex(r'^help skill(.*?)$')
async def help_skill(opsdroid, config, message):
    skill_names = []

    for i in range(len(opsdroid.skills)):
        if opsdroid.skills[i]['config']['name'] not in skill_names:
            skill_names.append(opsdroid.skills[i]['config']['name'])

    await message.respond("You have the following skills active: {}".format(skill_names))


@match_regex(r'clear$')
async def clear_screen(opsdroid, config, message):
    """Only works on the shell connector"""
    await message.respond("\033c")
