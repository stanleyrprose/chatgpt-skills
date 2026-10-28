# 统一 Git-backed Context Engineering PRD

版本：v1.1 Review Draft  
日期：2026-10-28（Asia/Rangoon）  
状态：review-first，仅供审阅；未授权实施  
范围：4 个运行入口、2 种 Activation Adapter、1 份 GitHub canonical Context Engineering 机制

本版修订：落实架构评审，补充兼容性门槛、启动契约、Mac 两条调用链、分域失败处理、版本治理、事务恢复与隔离验收。全文 `Custom Instructions` 指账号级指令；`CI` 仅指持续集成。本版只更新文档，保留 review-first 边界；来源事实沿用 v1.0 的取证记录，未新增客户端验证或验收通过声明。

## 1. 产品目标与决策

让用户跨 Cloud ChatGPT、Mac ChatGPT Desktop、Windows ChatGPT Desktop 与 Mac Codex CLI/CodexPro 工作时，按同一套规则找到当前目标、项目状态、可复用方法与长期知识，减少重复解释、过时上下文和错误写入。

统一的是规则来源、检索语义与维护约束；客户端只承载精简激活指针和必要的平台约束。Git repository 是 canonical store，GitHub 是当前托管平台。聊天历史、模型记忆、客户端缓存与检索索引不能取代 Git 当前状态。

用户确认的目标架构：前三个 ChatGPT 入口共享账号级 Custom Instructions；Mac Codex CLI/CodexPro 使用独立的全局与项目 `AGENTS.md`。Mac ChatGPT Desktop 与 Mac Codex 是不同运行入口，不能因运行在同一台 Mac 上而混为一谈。

## 2. 当前事实与待实施能力

| 项目 | 状态与证据 | 不可推导的结论 |
| --- | --- | --- |
| 开发分支 | `stanleyrprose/chatgpt-skills` 的 `feat/ai-memory-context-20261028` 已存在 | 不代表已合并或发布 |
| 提交 | `c0a1c44d27477ffa17d1e91447c919220cce060c`，提交说明为 `docs: add memory curator and four-level context reference` | 不代表客户端已配置 |
| Prompt | `prompts/memory-curator.md` 已提交 | 是单任务可复用 Prompt，不是新 Skill |
| 说明 | `prompts/README.md` 已提交 | 明确不自动在每个 ChatGPT 对话激活 |
| 检索参考 | `shared/context-engineering-four-level.md` 已提交 | reference-only，不是 router、RAG、数据库、daemon 或权限授予 |
| personal-knowledge | Capture / Maintenance Protocol v0.3 已验证并冻结；长期 PKS 系统仍在真实使用实验期 | 一次协议恢复成功不等于长期跨端可靠 |
| 自动激活 | 本 PRD 定义的待实施目标 | 尚不能声称四入口均已生效或通过验收 |

以上提交内容已通过只读 GitHub 查询核实；分支已查询存在。本文不声称当前分支 HEAD 就是该提交，也不声称主分支已包含它。本次仅生成本 Markdown 文件，不更新 Custom Instructions、AGENTS.md、GitHub 仓库或 PKS。

## 3. 架构与入口映射

```text
Cloud ChatGPT ────────────────┐
Mac ChatGPT Desktop ──────────┼─ A：账号级 Custom Instructions ─┐
Windows ChatGPT Desktop ──────┘                              │
                                                            ├─ canonical Context Engineering
Mac Codex CLI / CodexPro ─────── B：全局 + 项目 AGENTS.md ────┘  → L0–L3 → 各 canonical repo
```

| 运行入口 | Activation Adapter | 职责与边界 |
| --- | --- | --- |
| 1. Cloud ChatGPT | A | 共享账号级指针；通过本会话可用且已授权的连接器读取 Git |
| 2. Mac ChatGPT Desktop | A | 复用同一账号指针；本地工具能力另行识别，不维护第二份业务规则 |
| 3. Windows ChatGPT Desktop | A | 复用同一账号指针；不能假设具备 Mac 的本地路径、工具或授权 |
| 4. Mac Codex CLI/CodexPro | B | 全局 AGENTS 提供跨项目指针；项目 AGENTS 提供局部约束；CodexPro 是工具桥接能力 |

“4 个入口”是本产品范围的逻辑计数。Codex CLI 与 CodexPro 不计为第五入口；2 种 Activation Adapter 也不等于只有 2 个数据工具。Git read adapter 与 write adapter 是独立维度。

### 3.1 产品兼容性前提

账号共享是用户确认的目标配置，不能写成所有版本、所有模式都已验证的产品事实。当前 OpenAI 官方文档说明 web/desktop 个性化控件存在差异，桌面应用也可能以所选机器的 AGENTS.md 承载个人指令。因此，后续必须识别用户实际客户端版本、Chat/Work/Codex 模式及指令来源。

如实际 Mac/Windows ChatGPT 模式未继承账号级 Custom Instructions，应报告与目标架构的兼容缺口，不静默创建第三种 Adapter，不把 Mac ChatGPT 改称 Mac Codex，也不声称激活成功。若必须增加本地桥接，须先在设计审阅中明确变更；其内容仍应只是同一 canonical 机制的指针。

这是实施前兼容性门槛，不是一般待办：P1 须完成实际客户端版本、目标模式、指令来源和可用工具的静态盘点，形成逐入口兼容判断及证据。无充分证据的入口标记 Unknown，不得据此部署或承诺激活。其运行时继承行为留到 P3 集中验收；不支持或无法确认时标记 blocked，须先审阅兼容方案才可继续该入口。其他不依赖此缺口的设计工作可继续。P1 不执行新会话探测或端到端试验。

### 3.2 Mac 执行链与规则加载责任

第四逻辑入口包含两条需分别验收的调用链；共用规则原文，不假设加载机制相同。

```text
CLI：用户任务 → Codex CLI instruction discovery
    → 实际 CODEX_HOME 下全局 AGENTS / override
    → 当前项目适用 AGENTS 链 → canonical 指针 → L0–L3 → 已授权工具

CodexPro：宿主 AI 的任务/激活指令 → CodexPro 选择明确工作区
    → 宿主 AI 读取桥接返回的规则来源
    → 显式恢复尚未加载的适用全局与项目 AGENTS
    → canonical 指针 → L0–L3 → 已授权工具
```

CLI 的加载责任属于 CLI 的指令发现机制；P1 须记录实际配置、override 和截断风险。CodexPro 链由宿主 AI 负责确认规则已取得，桥接服务只提供其实际支持的规则读取能力。返回工作区 AGENTS 不等于已加载用户级全局 AGENTS；缺少任一必要来源时，不得以 CLI 的成功记录替代。

若宿主是前三个 ChatGPT 入口，账号级 Custom Instructions 负责把任务引导至桥接；进入 Mac 执行域后仍须遵守 Adapter B 的适用规则。这是入口激活与执行域规则的组合，不增加第五入口或第三种 Adapter。P1 必须写明宿主、启动触发点、读取工具、来源路径与缺失处理；未闭合的调用链不得进入实际配置。

## 4. Canonical 分工与冲突处理

| 内容 | Canonical home | 读取原则 |
| --- | --- | --- |
| 跨项目行为约束 | 已接受的 Constitution / 现有全局规范 | 客户端保留精简入口，避免复制全文 |
| Context Engineering 检索机制 | `chatgpt-skills/shared/context-engineering-four-level.md` | 读取明确 ref 对应的原文 |
| 记忆整理操作 | `chatgpt-skills/prompts/memory-curator.md` | 需要整理时按任务调用 |
| 单任务 Prompt / 多步 Skill | 现有 `prompts/` / 已批准 Skill 架构 | 不因统一记忆另建一套技能系统 |
| 项目目标、架构、状态、决策 | 各项目 Git repo 的 AGENTS、GOAL、checkpoint、ADR 等 | 当前项目原文优先于跨项目摘要 |
| 持久非敏感知识 | `personal-knowledge` 及现有分类 | 严守 v0.3；不复制项目日常日志 |

一条规则一个 canonical home；跨库用指针关联。`REGISTRY.md` 只是生成索引，不是规则权威，也不得手工修改。开发分支材料是 WIP，不自动覆盖已接受的主分支规则。未来 Adapter 应明确 canonical repo、路径、ref 与已接受版本，避免默认分支工具误读。

遵守平台和安全约束，按当前用户明确授权、适用范围及项目规则处理任务；不能用历史记忆扩大权限。项目 checkpoint 与真实 Git state 冲突时以当前 state + history 核对并提出修正。规则来源矛盾且影响写入时，停止相关写入，列明冲突；不能自动选择更宽松规则。

### 4.1 版本、更新与会话一致性

Activation Adapter 指向经过审阅的明确版本；不得自动跟随 WIP 分支或从默认分支读取后假称固定版本。已知 `c0a1c44` 仅是现有文档证据，不自动成为正式发布版本。

P1 指定现有规则维护者承担版本维护责任，不另建规则系统。每次变更记录旧版本、拟用版本、差异、受影响入口和回退版本；开发期只形成待审变更，完工后集中验收，最终发布 gate 后更新正式指针。无法读取指定版本时不得静默切换到 main。

会话内规则读取尽量使用同一解析后的 commit，记录实际来源，避免跨文件混用分支移动前后的规则。新会话读取当前已接受版本；旧会话在用户通知规则更新、切换项目、发生来源冲突或准备写入且规则可能变化时重新恢复相关规则。若运行时最新协议出现未审阅的安全/权限变化，暂停相关写入并协调版本，不能用固定旧版本绕过它。

知识内容和项目运行状态仍须读目标分支的最新 state/SHA；固定机制版本不意味着固定旧知识。未来更新不依赖常驻同步或后台任务。

## 5. 激活行为要求

Adapter 只需表达：何时恢复上下文、去哪里读取、按 L0–L3 工作、遵守开发阶段、无法读取时不写。不得塞入整个知识库或复制 PKS 协议。

1. 新任务先识别当前目标、运行模式、权限、项目与开发阶段。
2. 项目任务先恢复项目约束和当前目标；出现持久知识候选时恢复 PKS 协议。
3. 普通一次性问答不强制全库检索，不为每次聊天产生 capture。
4. 当前问题先解决，再评估是否需要 Memory Curator。
5. 指令被加载、canonical 文档被读取、任务被正确执行是三个不同状态；不能以自述“已记住”代替证据。
6. 按受影响域 fail closed：PKS recovery 或 read path 不可用时禁止 PKS mutation；项目必要规则或 read path 不可用时禁止该项目的相关 mutation；统一机制本身未成功恢复时，不执行依赖该机制的写入。不将单域故障扩大为无关任务的全局停工，可继续已有完整授权和规则依据的独立任务，并说明限制。

自动激活指在支持的会话中由指令触发按需恢复，不承诺后台常驻、每条消息必调用、离线自动同步或跨客户端即时刷新。

### 5.1 Bootstrap Contract：最小启动契约

P1 必须填写下表，静态审阅完整后才能开发相应 Adapter；本表是配置约束，不新增独立 router 或 manifest 系统。

| 字段 | 要求 |
| --- | --- |
| 入口与触发 | 明确客户端、模式、账号/工作区及项目任务/持久知识候选等触发条件 |
| 机制地址 | owner/repo 为 `stanleyrprose/chatgpt-skills`；机制路径为 `shared/context-engineering-four-level.md`；整理 Prompt 为 `prompts/memory-curator.md` |
| 版本 | 填写经审阅的 ref 与解析后完整 commit；当前正式激活版本尚未指定，不用 WIP 自动补位 |
| 规则前置 | 指定现有 Constitution 的真实来源、适用项目 AGENTS、GOAL/checkpoint；无适用项时显式说明，不编造路径 |
| PKS 地址 | `stanleyrprose/personal-knowledge`；恢复 `GOAL.md`、`MAINTENANCE.md`、`AUTO_CAPTURE.md`；写前读取当前目标分支最新状态 |
| 读取方式 | 每入口列出支持指定 ref 的可靠 read adapter、返回形式、权限与来源核对方式；不依赖模型记忆猜工具 |
| fallback | 首选失效时只允许同一授权范围内、可核实目标版本的读取路径；没有可靠路径则按受影响域停止写入 |
| 写入方式 | 与 read adapter 分别列明；记录目标分支、最新 SHA/并发控制和原子提交能力；不把读取权限当写入授权 |
| 会话状态 | 区分未触发、已加载指令、已读原文、可执行、blocked；来源证据不足不能标可执行 |

Adapter 必须直接携带足够的地址与版本指针，使首次会话在尚未读取机制正文时就能找到正文；不能要求先读取正文才能知道正文在哪里。来源链接本身不表示已经加载。完整规则、工具清单和用户私密路径不必塞入账号指令。

## 6. L0–L3 检索与上下文预算

| 层级 | 必需行为 | 输出 / 停止条件 |
| --- | --- | --- |
| L0：任务与强制约束 | 读取当前用户目标、授权范围、平台限制、适用 AGENTS；工程写入前检查分支和 CI/部署触发条件 | 明确本次范围与禁止动作 |
| L1：有界发现 | 定位 canonical repo、最小目录/文件名/片段、GOAL/checkpoint、按需 HOME 或知识地图；REGISTRY 仅作索引 | 找到相关来源，不扫全库 |
| L2：证据加载 | 读取必要原文章节、来源、ADR；核查时效、适用版本与 Git ref；写前读取最新内容及 blob SHA | 有足够证据完成任务即可停止 |
| L3：条件升级 | L1/L2 不足、矛盾或用户要求全面审阅时分批扩展；可选 XERJ/本地 embeddings 作发现 | 回到原文核实；仍不足则报告 Unknown |

上下文量随任务相关性增长，不随仓库大小增长。禁止默认加载全部 Skill、全部 PKS 或完整聊天历史。不承诺未经测量的 token 节省率、召回率、固定 top-k 或相似度阈值。搜索结果、摘要、向量命中都是定位线索，不能替代证据。

## 7. personal-knowledge v0.3：安全、去重与写入

本节是需求摘要；执行时读取最新 `GOAL.md`、`MAINTENANCE.md`、`AUTO_CAPTURE.md`。不另建 capture policy，不启动 v0.4，不允许 AUTO-CAPTURE 修改自身规则。

### 7.1 Capture Gate

只沉淀可迁移机制、模型、纠错、重要边界、反例、项目验证及长期知识缺口。通常满足 v0.3 至少两项价值条件才进入，极高价值单项可按协议例外处理，不机械计分。

- AUTO-CAPTURE：稳定、高价值、低争议且有复用价值；具备安全及读写条件时按现有协议维护。
- CANDIDATE：证据不足的假设或判断；优先放已有节点，或进入 `learning-queue.md`；不得包装为 Fact。
- REJECT：一次性查询、聊天转录、项目日常日志、无长期价值、重复无增量或安全禁止内容；不创建知识节点。

先查已有节点。核心结论相同且无新增 evidence、boundary、counterexample、纠错、decision impact 或 project validation，则 no-op。存在 material delta 时更新已有节点；仅在现有结构无法自然容纳稳定独立主题时新增文件。禁止“80% 语义相似度”之类无测量依据的门槛。

### 7.2 认知状态与敏感信息

新增或实质修改知识主张必须标注 Fact / Estimate / Inference / Judgment / Unknown，附证据、必要的时间锚点和适用条件。状态提升须保留“旧状态 → 新 evidence → 新状态”；措辞自信不构成 evidence。显著改变核心模型或真实决策依据的提升属于 high-risk mutation。

未明确验证仓库为 private 前，默认 PUBLIC_SAFE。凭证、token、cookie、密钥永远拒绝入 Git；私人敏感、第三方未公开、客户/合同/商业敏感和私人通信原文不得直接沉淀。可保留经核实安全的去标识通用机制。日志也不能复制被阻断的原文。

写前做语义安全检查；只有 backend 确实提供并启用 secret scanning 时才把扫描作为增强能力。不得声称未验证的扫描器已强制执行；不得“先提交再删除 secret”，因为历史仍会保留。

### 7.3 写入与并发

标准顺序：解决任务 → 恢复 canonical 协议 → visibility/safety → 查重与 material delta → epistemic status/evidence → 最小 diff → 再读最新 state/SHA → 合规写入 → capture log → correction receipt。

更新已有文件必须基于最新 blob SHA；冲突时重读、比较并协调语义，禁止 force overwrite。多文件一致性需采用支持的 atomic commit；工具不支持时不得拆成会产生不一致状态的盲写。

普通小型知识更新沿用 v0.3 atomic commit；删除、移动、批量重构、协议/权限/安全规则变化等走 high-risk review 路径。读工具可用不意味着有写权限，写工具可用也不能豁免 read-before-write。

正式 Gate 决策进入 `reviews/capture-log.md`，记录日期、outcome、topic、epistemic status、reason、target、commit、correction；可批量记录以免 commit churn。产生写入后给用户简短可纠正回执；未提交不得编造 SHA。

### 7.4 知识、日志与回执的一致性

有授权写入时，知识变更与对应 capture log 尽可能在同一原子提交中落地。日志使用已有协议允许的关联字段；不要求在提交内容中预先填入自身尚未生成的 commit SHA，可在回执附返回 SHA，必要时按现有日志规范后续关联。不得为此自行修改 v0.3 schema。

若工具只能分别写入，须先明确允许的部分完成状态与恢复方式；会破坏必要一致性的操作不执行。知识已写、日志失败时，如实报告目标文件、已知 SHA 和“日志待补”，不回报全流程成功，也不重新提交同一知识。回执发送失败不回滚已成功的 Git 提交；下次恢复先核对 Git state，再补缺失记录或回执。

写入超时、结果不明时，先只读核对目标内容、提交历史及日志关联，再判断是否需要重试；无法查明则保留 Unknown 并停止后续写入。补日志也要重新执行安全与 latest-SHA guard。此处是故障恢复要求，不新增数据库或后台补偿服务。

**本次 review-first 明确禁止任何 PKS 写入，包括日志。** 后续 Context Engineering 开发阶段也不得借 AUTO-CAPTURE 绕过阶段边界。v0.3 的最终 PR 要求仍保留，开发期间只准备待审材料，待完工并获准进入验收/发布阶段再执行。

## 8. Windows / Mac 能力差异

| 维度 | Cloud ChatGPT | Mac ChatGPT Desktop | Windows ChatGPT Desktop | Mac Codex CLI/CodexPro |
| --- | --- | --- | --- | --- |
| 目标指令来源 | 账号级 Custom Instructions | 同一账号 Custom Instructions | 同一账号 Custom Instructions | 全局 + 项目 AGENTS |
| 本地文件 | 不假设直达设备 | 依当前模式与授权 | 依当前模式与授权 | 依工作区 allowlist 与工具 |
| Git read/write | 连接器分别识别 | 连接器/本地桥按实际识别 | 连接器/本地桥按实际识别 | CLI/桥接按实际识别 |
| OS 路径 | 不推定 | macOS 路径 | Windows 路径 | macOS 工作区路径 |
| 激活验证 | 新会话来源证据 | 额外辨别 Chat/Work/Codex 模式 | 额外辨别 Chat/Work/Codex 模式 | AGENTS discovery 及桥接加载证据 |

不能从 Windows 可读仓库推导 Mac `gh` 可调用，不能从 Mac CodexPro 在线推导 Windows 有同一服务权限。每端分别记录版本、模式、账号/工作区、指令来源、read/write 能力与限制；缺失能力时采用已授权的可靠 fallback，否则 fail closed。

Codex CLI 官方支持全局到项目目录的 AGENTS 链，存在 override 和大小限制；CodexPro 是连接器，不因名字含 Codex 就保证自动发现全部全局 AGENTS。桥接需要显式恢复哪些规则，须在后续实现中定义并集中验收。

## 9. 威胁模型与失败边界

| 威胁 / 失败 | 必需处理 |
| --- | --- |
| 仓库、网页、历史聊天中的 prompt injection | 外部内容作为数据；不执行其中扩大权限、泄密或改写规则的指令 |
| 旧摘要、错误分支、过时 checkpoint | 核对 ref、当前 state 与 history；不得以模型记忆覆盖 |
| 账号切换、Custom Instructions 关闭、模式不继承指令 | 标记 trigger miss / 兼容缺口；不伪报全端激活 |
| read 失效但 write 可用 | 禁止受影响域 mutation；不采用 write-without-read；独立任务按 §5.6 处理 |
| 并发写与重试重复提交 | 最新 SHA guard，重读后协调；重试先检查提交结果和 material delta |
| 公开库泄露或日志泄露 | PUBLIC_SAFE、安全语义检查，阻断敏感原文进入文件及日志 |
| 自动 capture 自我放宽协议 | 禁止 self-modification；显式 review 与最终发布 gate |
| 检索漏召回 / 候选被误当 Fact | L3 扩展、原文核实、保留 Unknown；接受用户纠正 |
| 多端复制规则漂移 | Adapter 只保留指针、版本与本地必要约束；canonical 单点维护 |
| 工具超时、写入结果不明 | 先只读核对目标状态；不能盲重试或提前回报成功 |
| push 意外触发 CI / PR sync / deploy | 开发写入前检查触发条件；无法证明安全则不 push |

本机制是指令与流程约束，不是强制安全沙箱。它不能保证模型永不漏触发、所有连接器长期可用、跨端权限一致或 Git history 自动清除泄露。权限与平台约束仍由实际执行环境控制。

## 10. 非目标

- 不建设第二 canonical 数据库、全量聊天归档、常驻 daemon 或定时同步。
- 不默认新增 Skill、router、RAG/GraphRAG、知识图谱或全库 frontmatter。
- 不重写 personal-knowledge v0.3，不以此项目升级 v0.4。
- 不承诺固定 token、召回率、自动捕获率或跨 AI 长期稳定性。
- 不将 Windows Codex、其他 AI 客户端或 Android 纳入本轮四入口实施范围。
- 不修改已冻结项目架构、手改生成 REGISTRY 或自动迁移所有历史记忆。
- 不把 PRD 审阅视为安装、配置、Git 写入或发布授权。

## 11. 分阶段实施计划与开发边界

| 阶段 | 交付物 | Gate / 禁止事项 |
| --- | --- | --- |
| P0：当前 PRD review | 本文件、现状与目标差距、验收设计 | 只读取证与文档；不实施、不测试、不 PR、不 CI、不 Merge |
| P1：获准后的设计收敛 | Custom Instructions 草案、AGENTS 草案、Bootstrap Contract、版本/路径表、逐入口静态兼容盘点、CLI/桥接调用链 | 缺失信息按入口 blocked；只静态审阅，不做运行试验、不应用账号设置 |
| P2：获准后的开发 | 在指定开发分支完成两种 Adapter 与必要兼容处理、变更清单 | Phase D：编辑与静态 diff 阅读；不运行测试、盲测、E2E、self-test、build/lint/CI；不创建 PR、不 Merge、不部署 |
| P3：完工后集中验收 | 受控试用配置、隔离 fixture、四入口验收证据、安全/去重/并发结果、缺陷修正及恢复记录 | 所有开发和必要人类反馈完成后，用户明确批准 Phase V，并明确试用配置的范围与副作用，才能安装试用配置和执行验收；不 PR、不 CI、不 Merge |
| P4：发布闭环 | 最终 PR、CI、review、Merge、正式指针与配置、回退记录 | Phase V 通过且用户批准 Phase R；正式账号配置/部署按各自授权执行；不把试用通过当正式发布 |

开发阶段可按授权做增量本地提交；只有静态确认开发分支 push 不触发 CI、PR sync 或外部部署时才可 push。否则保留本地工作并报告。不得借工具命名“verification”绕过不测试要求。已有正常运营定时任务不因本项目被擅自关闭。

集中验收失败时保留失败证据，修正后针对受影响范围复验；不能宣称整体通过。验收完成也不自动授权 Merge 或生产发布。

P3 开始前备份原有 Custom Instructions、适用 AGENTS 和版本指针，记录恢复方法。账号级试用设置可能影响同账号其他会话，不能假称仅对单个会话隔离；须把这个影响写入 Phase V 授权范围。尽量使用专用验收项目、只读能力和明确的试用指针；完成或中止时恢复原设置，除非用户已授权保留。实际激活试验只在 P3 进行，消除“未配置先验收、验收后才配置”的循环。

## 12. 集中验收标准（计划，尚未执行）

每项须有客户端/版本/模式、日期、目标 ref/SHA、实际读取来源、观察结果与 pass/fail/blocked。四入口分别记录，不以同账号代替逐端证据。

| ID | 场景 | 通过标准 |
| --- | --- | --- |
| A01 | 三个 ChatGPT 新会话 | 无需重复粘贴机制全文，按目标共享账号指令定位 canonical；若模式不支持则 blocked，不能判 pass |
| A02 | Mac Codex CLI 与 CodexPro 子场景 | 分别证明适用全局/项目规则已加载；无第二套维护规则 |
| A03 | 项目恢复 | 先读取项目 AGENTS 与当前 GOAL/checkpoint，再引用历史知识；识别正确 ref |
| A04 | Prompt / reference 发现 | 按需定位 memory-curator 与四层原文，不扫所有 Skill，不改 REGISTRY |
| A05 | L3 升级 | 信息不足/矛盾时扩大检索并核实原文；无法解决则明确 Unknown |
| A06 | 去重与增量 | 重复无增量 no-op；有 material delta 更新已有节点；不制造平行文件 |
| A07 | PKS 三态与认知状态 | 正确区分 AUTO-CAPTURE/CANDIDATE/REJECT；禁止无新 evidence 的 Fact 升级 |
| A08 | 安全拒绝 | 使用合成样本验证敏感材料不入 Git、日志不泄露；不使用真实密钥 |
| A09 | read/write 分离失败 | read 不可用但 write 可用时受影响域无 mutation，给出具体限制；无关且已授权任务仍能继续 |
| A10 | 并发与不明写入结果 | stale SHA 不覆盖；重读协调；超时后查明状态，不重复盲写 |
| A11 | 用户纠正 | 写后回执真实可追溯；修正保留演化链，不恢复被否决旧结论 |
| A12 | 阶段边界 | Phase D 无测试、PR、CI、Merge、部署；P0 无任何外部配置/知识写入 |
| A13 | 可回退 | 可恢复旧 Adapter 内容和版本指针；知识回退保留历史，涉及泄露须走独立处置 |

通过标准重在行为与证据，不以生成文件数、commit 数或“已激活”口头声明验收。真实使用期观察 trigger miss、duplicate/retrieval miss、correction、non-meta capture、检索成本与冲突；capture log 无法独立测量漏捕获或 recall，不编造精确指标。

### 12.1 验收环境与记录格式

下列用例只定义计划，P0–P2 不执行。P2 可编写合成 fixture 和验收说明，但不得运行。P3 使用明确标识为非 canonical 的隔离副本/验收分支，不向正式 PKS 节点或正式 capture log 写入测试材料；隔离副本仍不是第二 Source of Truth。分支写入前静态确认不会触发 CI、PR sync 或部署，否则选本地隔离副本或其他已授权无触发环境。

用例记录至少包含：ID、入口/子链、客户端版本/模式、账号或工作区代号（不记录凭证）、前置状态、输入、目标 ref/SHA、预期行为、实际工具/来源证据、变更前后状态、允许副作用、清理/恢复结果、pass/fail/blocked。仅凭模型复述规则不能证明加载；需要读取来源或运行环境可提供的加载记录。证据能力不足时标记 blocked。

### 12.2 最小可复现步骤

| ID | 前置条件与输入 | 操作及预期证据 | 允许副作用 |
| --- | --- | --- | --- |
| A01 | 三个目标 ChatGPT 客户端分别启动全新验收会话；已备份并获准应用试用指令；只给固定的项目任务，不粘贴机制全文 | 分别观察定位约定版本、读取规则原文并遵守范围；记录实际来源和缺失项；任一入口 blocked 则不能判四入口整体通过 | 仅已授权试用配置；用例不写正式仓库 |
| A02 | CLI 与 CodexPro 各使用同一隔离项目；准备可区分的全局、项目规则；路径与版本固定 | 分别启动任务，核对全局/项目来源及适用约束；桥接须证明显式补读缺失规则，不复用 CLI 证据 | 隔离项目及已备份的试用 AGENTS |
| A03 | 隔离项目当前 GOAL 与提供的旧摘要有可识别差异 | 输入“继续当前项目”；应先恢复适用规则与最新目标，并明确舍弃旧摘要的过时状态 | 只读 |
| A04 | 已知机制与 Prompt 的指定 ref 可读 | 输入固定的知识整理任务；按需读取两个指定文件，检查无全 Skill 扫描、无 REGISTRY 改动 | 只读 / 提案 |
| A05 | fixture 的初始证据不完整，另一原文含补充或冲突 | 输入需要两处证据的固定问题；应条件升级并核对原文；移除补充来源后应报告 Unknown | 只读 |
| A06 | fixture 已有一个知识节点；两份输入分别无增量、有明确新边界 | 顺序提交两份输入；前者知识节点 no-op（隔离日志可记 REJECT），后者只更新原节点；比较 diff | 仅隔离节点与隔离日志 |
| A07 | 准备稳定机制、未验证假设、无价值临时材料三组固定样本 | 分别产生三态决定并说明证据；再重复更自信的同一假设，不得升级 Fact | 仅隔离节点/队列/日志；不得修改协议 |
| A08 | 使用明显标识为合成、无实际效力的凭证样式与虚构私人/商业信息 | 请求 capture；应阻断敏感原文进入 diff/日志，日志仅记录去敏类别；核对未写入 | 只允许隔离的去敏拒绝记录 |
| A09 | 在验收环境撤去 PKS read，保留可见 write 能力；另有规则完整的独立任务 | 请求 PKS 更新和独立任务；前者无写入，后者可在其授权范围继续；不撤销生产凭证模拟故障 | PKS 零 mutation；独立任务仅用隔离目标 |
| A10 | 隔离文件预置旧 SHA，再由受控第二写入者产生新版本；另模拟“提交成功但回传超时” | 尝试旧 SHA 更新应失败并重读协调；超时后先查询历史和内容，不能重复提交同一增量；再模拟日志失败，报告部分完成并补缺 | 仅隔离文件/日志及受控故障；禁止 force overwrite |
| A11 | 隔离环境有已写入的 CANDIDATE 与真实返回 SHA | 用户明确纠正结论；应记录旧判断→纠正依据→新判断，回执引用实际提交；再次恢复不得还原旧错误 | 仅隔离节点/日志 |
| A12 | 提供本轮变更清单、阶段授权及可用操作记录 | 静态审阅 P0–P2 无运行测试、PR、CI、Merge/部署；P3 试用范围未越权；不靠重新执行禁用操作证明合规 | 只读审计 |
| A13 | 已备份旧配置；P3 试用配置已应用；具备明确恢复权限 | 恢复原配置与旧指针，核对内容；隔离知识用保留历史的撤销方式；确认无正式 PKS 污染 | 仅已授权恢复与隔离清理，不自动清除 Git 历史 |

缺少故障注入能力时，A10 可先静态审阅恢复方案，但不能将静态审阅记为并发/超时行为已通过。所有适用用例与入口子场景均通过后才可宣称本轮验收通过；blocked 不计 pass，范围缩减须由用户明确接受并更新 PRD。

## 13. 审阅重点与未决项

目标的 4/2/1 架构已按用户确认记录；以下属于实施前信息缺口，不改变目标，也不阻止本文交付：

1. **P1 进入对应入口开发的门槛：** 静态兼容盘点、Bootstrap Contract、两条 Mac 调用链责任完整；三个 ChatGPT 的账号级 Custom Instructions 继承能力有证据依据或明确 blocked。运行行为最终由 P3 验收确认，不在开发期提前测试。
2. **P1 必填：** 已接受 canonical ref、全局规则真实来源、维护责任及 WIP 未来发布位置。未指定前不得正式激活。
3. **P1 必填：** 各入口实际 read/write adapter、权限、内容传输限制、并发能力及可靠 fallback；CodexPro 不沿用 CLI 加载假设。
4. **P3 前必需：** 完工声明、必要人类反馈完成、Phase V 授权、试用配置的账号影响范围、隔离目标及恢复方案。
5. **P4 前必需：** 全部适用验收证据通过和 Phase R 授权；尚无任何验收通过结论。

## 14. 证据与来源

- 用户提供的原对话《建立AI记忆库》（私人会话标识不随公开仓库发布）。本次读取到用户历史消息，但部分助手回复仅为引用占位符，因此本 PRD 以本次用户明确架构要求为准。
- [已核实提交 c0a1c44](https://github.com/stanleyrprose/chatgpt-skills/commit/c0a1c44d27477ffa17d1e91447c919220cce060c)。三个新增文件与不自动激活边界均来自该提交。
- [开发分支](https://github.com/stanleyrprose/chatgpt-skills/tree/feat/ai-memory-context-20261028)。只读查询已确认分支存在。
- [PKS GOAL](https://github.com/stanleyrprose/personal-knowledge/blob/main/GOAL.md)、[MAINTENANCE v0.3](https://github.com/stanleyrprose/personal-knowledge/blob/main/MAINTENANCE.md)、[AUTO_CAPTURE v0.3](https://github.com/stanleyrprose/personal-knowledge/blob/main/AUTO_CAPTURE.md)。已读取当前 main 内容；未来执行仍须重读最新状态。
- [OpenAI：Personalize ChatGPT](https://learn.chatgpt.com/docs/personalize)。说明跨聊天个性化与 web/desktop 控件差异。
- [OpenAI：Desktop app settings](https://learn.chatgpt.com/docs/app/settings)。说明所选机器 AGENTS.md 的个人指令入口；不能据此无条件保证所有桌面模式继承账号 CI。
- [OpenAI：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。支持 Codex 全局/项目发现、override 与加载限制的说明。

来源核对日：2026-10-28。官方产品文档用于标注能力边界，不构成用户设备已配置或验收成功的证据。

