# Project Code Discipline

一个面向已有项目的 Codex Skill。它根据项目规则和源码学习架构、代码与配置风格，帮助 Codex 复用已有实现、控制改动范围，并用实际入口验证结果。

## 安装

在 Codex 中使用内置安装器：

```text
使用 $skill-installer 安装 https://github.com/GuiDI-666/project-code-discipline/tree/v1.8.0/skills/project-code-discipline
```

也可从 [Releases](https://github.com/GuiDI-666/project-code-discipline/releases) 下载 Skill 压缩包，将解压后的 `project-code-discipline` 目录放入 `~/.agents/skills/`。安装后确认该目录直接包含 `SKILL.md`。已安装旧版时，在同一安装位置更新即可。

## 使用

```text
使用 $project-code-discipline 审查当前项目，关注重复实现、失败后的实际状态和测试覆盖。只读审查。
```

```text
使用 $project-code-discipline 修改这个模块。先核对现有调用方和可复用的实现，再运行与改动相关的检查。
```

Codex 可按任务自动匹配该 Skill，也支持显式调用。将反复适用的项目规则写入项目的 `AGENTS.md`，可在新会话中重新读取。

Skill 包含项目分析、架构提炼、定义与用法核对、配置风格分析，以及代码复用和行为验证规则。具体语言、文件结构和工具链由目标项目决定。入口见 [SKILL.md](skills/project-code-discipline/SKILL.md)。

## 开发与贡献

从仓库根目录运行 `python scripts/validate.py`，检查 Skill 元数据、仓库内链接和许可证。规则修改请附上触发场景、预期行为和适用范围。通过结构校验后，按需用独立样本验证实际行为。详见 [贡献指南](CONTRIBUTING.md)。

本项目采用 [MIT 许可证](LICENSE)。
