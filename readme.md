[PCRC](https://github.com/Fallen-Breath/PCRC) v1.0+ includes MCDR support already, so no need for this adaptor plugin if you are using MCDR >= 2.0

-------------

PCRC-MCDR
----------

[中文](https://github.com/TISUnion/PCRC-MCDR/blob/master/readme_cn.md)

Import [PCRC](https://github.com/Fallen-Breath/PCRC) as a [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) plugin!

## Usage

1. Put `PCRC-MCDR.py` into the `plugins/` folder of MCDR
2. Download universal release of PCRC with version not less than `0.9.0-alpha` in PCRC [release page](https://github.com/Fallen-Breath/PCRC/releases), extract it to `plugins/PCRC-xxx-universal/`
3. Rename `PCRC-xxx-universal/` folder in `plugins/` folder to `PCRC-MCDR/`
4. Install all [requirement modules](https://github.com/Fallen-Breath/PCRC#python-modules) of PCRC
5. At this time, the file structure of MCDR is roughly as follows

```
MCDReforged/
├─ plugins/
│  ├─ PCRC-MCDR/
│  │  ├─ PCRC.py
│  │  ├─ protocol.json
│  │  ├─ config.json
│  │  └─ ...
│  ├─ PCRC-MCDR.py
│  ├─ other_plugin.py
│  └─ ...
└─ ...
```

The PCRC configuration file will be `MCDReforged/plugins/PCRC/config.json`. Remember to fill it

The replay recording file will be stored in `MCDReforged/PCRC_recordings/`

## Command

- `!!PCRC start`: Start PCRC
- `!!PCRC stop`: Stop PCRC. Only works with console command input
