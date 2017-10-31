# opsdroid skill devtools

Some handy skills for use while developing for [opsdroid](https://github.com/opsdroid/opsdroid).

## Requirements

None.

## Configuration

```yaml
- name: devtools
```

## Usage

#### `reload`

Reloads all config.

> user: reload
>
> opsdroid: Reloading skills


#### `quit`

Exits opsdroid.

> user: quit
>
> opsdroid: Stopping opsdroid


#### `clear`
Clears terminal window (only works in shell)

> user: clear
>
> opsdroid: 


#### `help skills`
Get list of active skills

> user: help skills
>
>opsdroid: You have the following skills active: ['hello', 'dance', 'loudnoises', 'devtools']


#### `help`

Get useful information about opsdroid.

> user: help
>
> opsdroid:
>
>OpsDroid - An open source chat bot framework written in python.
>
>OpsDroid comes with a few simple commands out of the box. 
>With "Hello" Opsdroid will greet users when they say hello.
>With "Goodbye" Opsdroid will say goodbye to them when they leave. 
>With "when did you last see <user>" Opsdroid can tell you when the user was online.
>With "ALLCAPSTEXT" Opsdroid will complain with an image.
>With "Dance" Opsdroid will even dance!
>
>To see a list of all active skills just say:
>> help skills
>
>
>You can also add more skills to Opsdroid by uncommenting or adding new skills to the configuration file.
>A Configuration file can be found in:
>Path: ~/.opsdroid/configuration.yaml
>
>
>Official site: https://opsdroid.github.io
>Documentation files: http://opsdroid.readthedocs.io/en/latest/?badge=latest
>Blog:  https://medium.com/opsdroid
>Youtube: https://www.youtube.com/channel/UC0FeGkDF7FrshmzAsb9lDvw
>GitHub: https://github.com/opsdroid
>
>Get opsdroid working on your computer: 
>Opsdroid Desktop: https://github.com/opsdroid/opsdroid-desktop
