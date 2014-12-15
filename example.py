from autoconf import AutoConf

foo = {'one': 'blah one', 'two': { 'three': 'blah three'}}
bar = {'one': 'blah override', 'two' :{ 'seven': 'fart'}}
arg = {'two' :{ 'seven': 'override'}}

merged_config = AutoConf(foo, bar, arg)

print merged_config.output_yaml()
