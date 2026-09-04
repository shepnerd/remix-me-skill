# remix-me（中文版）

[English](README.md)

## 这是什么？

`remix-me` 帮助 coding agent 从外部参考源中学习——例如 repo、论文、文档、网页、UI 示例或代码片段——但不会把它们盲目复制到当前项目。

它会提取有价值的想法，与当前项目的目标和能力进行比较，说明匹配度、风险、工作量和机会成本，并在用户明确授权前保持只分析、不修改。

它适用于 Codex、Claude Code，以及其他支持 `SKILL.md` Agent Skills 格式的工具。

## 60 秒了解效果

最短的有效演示就是一段对话：给出参考源，让 skill 推断项目目标，比较一个想法，最后由用户明确授权小范围改动。完整对话见 [`demo/quick-demo.md`](demo/quick-demo.md)。

```mermaid
flowchart LR
  A[参考源 + 当前仓库] --> B[推断目标与约束]
  B --> C[比较匹配度、风险、工作量]
  C --> D{用户选择}
  D -->|暂不采用| E[不修改文件]
  D -->|采用并授权| F[小范围实现 + 测试]
```

## 一分钟安装

先 clone 本仓库，再把规范包 `skills/remix-me` 安装到你使用的 agent。两种平台使用同一份核心 `SKILL.md`。

### Codex

在 Codex 中执行下面这一条命令，安装固定版本 `v0.1.0`：

```text
$skill-installer install https://github.com/shepnerd/remix-me-skill/tree/v0.1.0/skills/remix-me
```

如果需要手动或离线安装，先 clone 本仓库，再复制 skill 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/remix-me"
cp -a skills/remix-me/. "${CODEX_HOME:-$HOME/.codex}/skills/remix-me/"
```

在 prompt 中使用 `$remix-me`。

### Claude Code

```bash
mkdir -p "$HOME/.claude/skills/remix-me"
cp -a skills/remix-me/. "$HOME/.claude/skills/remix-me/"
```

在 Claude Code 中使用 `/remix-me`。如果只想让某个仓库使用，把同一目录复制到该仓库的 `.claude/skills/remix-me/`。

## 怎么用

给出参考源；如果已经知道要解决的问题，也一并说明：

```text
使用 $remix-me，对比这些 repo，推荐哪些内容值得适配到当前项目：……
```

如果只给参考源，它会先读取目标项目，从 instructions、README、代码和测试中推断 provisional brief，并请你确认：

```text
/remix-me 对比这篇论文及其开源实现与当前仓库。如果需要，先从仓库推断项目问题，然后在修改前停止。
```

准备实施某个建议时，明确指出候选并授权：

```text
使用 remix-me。选择候选 1 并授权实施。保持改动小，运行 focused tests，并报告 checkpoint 和回滚路径。
```

## 它会怎么工作

通常会按以下顺序处理：

1. 从项目 instructions、README、代码和测试中确认主要目标与约束；
2. 提取参考源的方法、观点、证据、假设、来源和许可证信息；
3. 将每个候选与本地能力、兼容性、风险、工作量和机会成本比较；
4. 给出 integrate、pilot、defer 和 do-not-integrate 选项；
5. 只有在用户明确选择集成内容并授权后才修改文件。

分析、推荐和实施模式会自动选择，用户不需要记住模式名称。

## 安全与范围

- 外部代码和指令只作为分析数据，不能直接变成 agent 指令；
- 仅检查参考源时，不安装依赖、不上传私有文件、不读取 secrets；
- 用户没有同时确认“集成什么”和“现在实施”之前，不修改目标仓库；
- clean Git 项目默认使用现有 commit 作为基线，并隔离 dirty 改动；
- 非 Git 项目不会自动生成大规模 archive 或 manifest，只有用户要求并批准时才备份；
- 大型参考源默认采用渐进式、有界检查。

## 维护者说明

规范包是 [`skills/remix-me`](skills/remix-me)。`agents/openai.yaml` 只是 Codex 的可选 UI 元数据，Claude Code 可以忽略；详细 schema 位于 `skills/remix-me/references/`。

[`evals/`](evals/) 不是安装或调用 skill 的必需内容，因此不会影响普通用户的首次使用；它保留给维护者和希望核验行为的采用者，用于记录目标推断、多源比较、授权边界、clean/dirty Git checkpoint 和非 Git 回滚限制。它是回归证据，不保证所有模型行为完全一致。

运行结构校验：

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skill_package.py
```

贡献指南见 [`CONTRIBUTING.md`](CONTRIBUTING.md)，安全问题见 [`SECURITY.md`](SECURITY.md)。

## 许可证

本 skill 使用 MIT License，详见 [`LICENSE`](LICENSE)。被参考的项目、论文、网页、代码和资源仍受其自身条款约束。
