PCRC-MCDR
----------

[English](https://github.com/TISUnion/PCRC-MCDR/blob/master/readme.md)

将 [PCRC](https://github.com/Fallen-Breath/PCRC/blob/master/readme_cn.md) 作为一个插件导入至 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)!

## 使用方法

1. 将 `PCRC-MCDR.py` 放入 MCDR 的 `plugins/` 文件夹
2. 在 PCRC 的 [Release 页面](https://github.com/Fallen-Breath/PCRC/releases) 下载不低于 `0.9.0-alpha` 版本的 universal 版 PCRC，将压缩包解压至 `plugins/PCRC-xxx-universal/`
3. 将 `plugins/` 文件夹中 `PCRC-xxx-universal/` 文件夹重命名为 `PCRC-MCDR/` 文件夹
4. 安装 PCRC 的所有[依赖库](https://github.com/Fallen-Breath/PCRC/blob/master/readme_cn.md#python-模块)
5. 此时 MCDR 的文件结构大致如下

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

PCRC 的配置文件将为 `MCDReforged/plugins/PCRC/config.json`，记得去填写

录像文件将会存放至 `MCDReforged/PCRC_recordings/`

## 指令

- `!!PCRC start`: 启动 PCRC
- `!!PCRC stop`: 关闭 PCRC。仅在控制台可用
