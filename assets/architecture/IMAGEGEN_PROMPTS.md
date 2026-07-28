# RuleGo 宣传结构图 ImageGen 提示词

本文档保存当前营销素材目录中五张结构图的完整生成提示词。统一使用内置 ImageGen，画面比例为 16:9，视觉基调为明亮、专业、具有科技感的企业级产品信息图。

## 代码分析依据

### RuleGo 核心引擎

- `README_ZH.md`
- `endpoint/README_ZH.md`
- `components/common`
- `components/filter`
- `components/transform`
- `components/action`
- `components/external`
- `components/flow`
- `engine`
- `api/types`
- `builtin/aspect`

### RuleGo Server

- `server/README_ZH.md`
- `server/bootstrap/bootstrap.go`
- `server/app`
- `server/internal/endpoint`
- `server/internal/modules`
- `server/internal/engine`
- `server/internal/store`
- `server/config/config.go`
- `server/cmd/server/with_*.go`

### RuleGo 前端编辑器

- `README.md`
- `docs/CLIENT_INTEGRATION.md`
- `packages/editor-core/src`
- `packages/editor-ui/src`
- `packages/editor-react/src`
- `packages/editor-vue/src`

## 1. AI 客服客户聊天端

```text
Use case: infographic-diagram
Asset type: high-resolution 16:9 Chinese marketing infographic for an AI customer-service product
Primary request: Create a polished functional architecture diagram for the customer-facing chat portal. It must communicate both product modules and the end-to-end interaction flow, suitable for an external product brochure or presentation.
Title text (verbatim): "AI 客服客户聊天端"
Subtitle text (verbatim): "一次接入，实时连接 AI 与人工服务"
Scene/backdrop: bright white to very pale cool-gray background, airy premium enterprise technology aesthetic, subtle fine grid and restrained luminous circuit lines, no dark background.
Style/medium: refined 2.5D isometric product infographic mixed with crisp flat UI cards, high-end Chinese SaaS launch visual, clean vector-like edges, realistic soft depth, not a webpage screenshot.
Composition/framing: wide 16:9 landscape. Center is a clean chat interface illustration showing a customer message, an AI reply, and an optional human-agent reply. Around it are six clearly separated functional modules with small relevant icons. Across the lower third is a left-to-right numbered interaction flow connected by elegant arrows.
Functional modules, exact Chinese labels:
1. "浏览器客户身份" — "自动生成唯一 ID，支持重置身份"
2. "会话管理" — "新会话与上下文隔离"
3. "快捷咨询" — "常见问题一键填入"
4. "发送状态" — "发送中、处理中、已回复、异常"
5. "实时连接" — "业务 WebSocket 状态同步"
6. "历史同步" — "AI 与人工回复统一归档"
Interaction flow, exact text and order:
"1 进入公开入口" → "2 输入并发送问题" → "3 规则链识别意图" → "4 AI 自动处理" → "5 必要时人工接入" → "6 回复与历史实时同步"
Supporting badges, exact text: "真实规则链", "实时状态", "客户隔离", "AI + 人工协作"
Color palette: white, ice blue, vivid cyan, fresh green, restrained coral accents, neutral graphite text. Use different colors for customer, AI, human, and system status.
Typography: modern Chinese sans-serif, excellent legibility, correct Simplified Chinese, generous spacing, no tiny body text. Preserve every required Chinese label exactly.
Constraints: show clear arrow direction and visual hierarchy; each icon must match its module; make the center chat product signal obvious in the first glance; balanced whitespace; professional external marketing quality.
Avoid: dark mode, black/navy full background, purple gradient dominance, excessive glassmorphism, decorative orbs, illegible microtext, random English, duplicated labels, garbled Chinese, watermark, logo, QR code, browser chrome, phone hardware mockup, dense technical code.
```

## 2. AI 客服工作台

```text
Use case: infographic-diagram
Asset type: high-resolution 16:9 Chinese marketing infographic for an AI customer-service operations platform
Primary request: Create a polished functional architecture diagram for the customer-service workbench. It must show AI-first service operations, human-agent collaboration, customer operations, and the complete cross-channel handling flow. Suitable for an external product brochure or conference presentation.
Title text (verbatim): "AI 客服工作台"
Subtitle text (verbatim): "AI 自动服务，人工按需协作，全链路实时可见"
Scene/backdrop: bright white to very pale cool-gray background, premium enterprise technology aesthetic, subtle fine grid, restrained cyan circuit lines and data-flow paths, no dark background.
Style/medium: refined 2.5D isometric product infographic combined with crisp operational UI panels, high-end Chinese SaaS launch visual, clean vector-like edges, realistic soft depth, not a literal webpage screenshot.
Composition/framing: wide 16:9 landscape. Center is a three-column workbench illustration: left customer queue, center live conversation and service state, right customer profile and AI analysis. Around the main workbench are six compact capability cards. Along the lower third, show a clear numbered left-to-right operating flow with arrows.
Capability cards, exact Chinese labels:
1. "实时客户队列" — "未读提醒、咨询置顶、最后消息时间"
2. "AI 智能处理" — "意图识别、上下文理解、Skill 调用"
3. "客户画像" — "分群、等级、风险、标签与备注"
4. "人工协作" — "接入、转接、接管、退回 AI"
5. "坐席与 Skill" — "专长匹配、个性配置、能力引用"
6. "运营洞察" — "会话、消息、意图与人工关注统计"
Interaction flow, exact text and order:
"1 客户发起咨询" → "2 实时进入客户队列" → "3 AI 识别意图与上下文" → "4 自动回复或建议人工" → "5 坐席接入与协作" → "6 双端同步与数据沉淀"
Service-state ribbon, exact text:
"AI 自动服务" · "等待人工" · "人工协作" · "人工接管" · "退回 AI"
Supporting badges, exact text: "实时 WebSocket", "会话隔离", "全程可审计", "AI + 人工闭环"
Visual details: customer queue cards with unread red dots and newest consultation on top; live conversation containing customer, AI, and human messages with distinct colors; right-side profile has tags, intent, risk, assigned agent; a subtle analytics chart and agent routing visual; every icon must directly match its capability.
Color palette: white, ice blue, vivid cyan, fresh green, controlled amber and coral for alerts, neutral graphite text. AI is cyan, customer is blue, human agent is orange, successful states are green, attention states are coral.
Typography: modern Chinese sans-serif, excellent legibility, correct Simplified Chinese, generous spacing, no tiny body text. Preserve every required Chinese label exactly.
Constraints: strong first-glance product signal; arrow directions must be unambiguous; clearly distinguish AI automatic service from optional human intervention; balanced whitespace; professional external marketing quality.
Avoid: dark mode, black/navy full background, purple gradient dominance, excessive glassmorphism, decorative orbs, illegible microtext, random English, duplicated labels, garbled Chinese, watermark, logo, QR code, dense source code, generic call-center stock imagery.
```

## 3. RuleGo 核心引擎

```text
Use case: infographic-diagram
Asset type: high-resolution 16:9 Chinese marketing infographic for the RuleGo core engine
Primary request: Create a deeply detailed but visually organized functional architecture diagram for the RuleGo core engine itself, not RuleGo Server and not the frontend editor. It must show protocol endpoints, rule-chain components, execution runtime, AOP, performance mechanisms, and integration outputs. Suitable for an external product brochure and visually consistent with a bright premium AI customer-service infographic series.
Title text (verbatim): "RuleGo 核心引擎"
Subtitle text (verbatim): "轻量嵌入，高性能执行，组件化编排万物"
Scene/backdrop: bright white to very pale cool-gray background, subtle fine grid and restrained cyan circuit paths, premium enterprise technology aesthetic, no dark background.
Style/medium: refined 2.5D isometric architecture infographic mixed with crisp flat system cards, clean vector-like edges, soft depth, high-end Chinese technology launch visual, not a code screenshot.
Composition/framing: wide 16:9 landscape. Center is a layered engine architecture. Left is heterogeneous input and Endpoint routing. Middle is rule-chain execution. Right is application integration. Around the engine are six compact capability cards. Across the lower third is a numbered message execution flow.
Left input column exact heading: "Endpoint 统一接入"
Input labels: "HTTP / WebSocket", "MQTT", "TCP / UDP", "Schedule", "扩展消息系统", "自定义 Endpoint"
Center architecture layers, exact labels:
"规则链 DSL" — "节点 · 连线 · 子规则链 · 变量 · 密钥"
"标准组件体系" — "通用 · 过滤 · 转换 · 动作 · 外部 · 流程"
"执行引擎" — "组件注册 · 生命周期 · 路由缓存 · 规则链实例池"
"运行上下文" — "消息隔离 · 分支汇聚 · 节点输出缓存 · 跨链调用"
"AOP 与运行时" — "校验 · 调试 · 指标 · 限流 · JS · Expr · 扩展脚本"
Right integration column exact heading: "应用与系统集成"
Integration labels: "宿主应用", "业务系统", "LLM 与智能体", "数据库与缓存", "消息队列", "IoT 与边缘设备"
Capability cards, exact Chinese labels:
1. "动态规则编排" — "整链热更新与节点级重载"
2. "丰富标准组件" — "过滤、转换、路由、动作与外部调用"
3. "子链与流程控制" — "嵌套、并行、循环、汇聚与引用"
4. "异构数据集成" — "统一 Endpoint DSL 与双向响应"
5. "高并发与稳定性" — "协程池、对象池、背压与优雅停止"
6. "开放扩展机制" — "自定义组件、插件、UDF、Endpoint 与切面"
Interaction flow, exact text and order:
"1 多源消息进入" → "2 Endpoint 路由与预处理" → "3 创建隔离执行上下文" → "4 按关系执行节点图" → "5 AOP 校验调试与指标" → "6 结果回传或联动外部系统"
Supporting badges, exact text: "嵌入式运行", "动态热更新", "上下文隔离", "全链路扩展"
Visual details: show an actual branching rule graph in the middle with filter, transform, action, join, sub-chain, and external-call nodes. Show a parallel branch joining back into one flow. Show an engine pool and component registry as visible supporting mechanisms. Endpoint and application arrows must be bidirectional where response is supported.
Color palette: white, ice blue, vivid cyan, fresh green, controlled amber and coral accents, neutral graphite text. Input is cyan, execution is blue, transforms are green, actions are amber, errors are coral.
Typography: modern Chinese sans-serif, excellent legibility, correct Simplified Chinese, generous spacing, no tiny body text. Preserve every required Chinese label exactly.
Constraints: clearly distinguish RuleGo core from server management functions; no login, user management, REST admin API, marketplace UI, or frontend editor controls. Strong first-glance engine signal, unambiguous arrows, balanced whitespace, professional external marketing quality.
Avoid: dark mode, black/navy full background, purple gradient dominance, excessive glassmorphism, decorative orbs, illegible microtext, random English, source code, duplicated labels, garbled Chinese, watermark, external URLs, QR code, generic server-rack stock imagery.
```

## 4. RuleGo Server 后端服务

```text
Use case: infographic-diagram
Asset type: high-resolution 16:9 Chinese marketing infographic for RuleGo Server
Primary request: Create a deeply detailed functional architecture diagram specifically for "RuleGo Server", the backend application platform built on the RuleGo core engine. Do not present it as the core engine itself and do not present the frontend editor. Show real API protocols, application container, business modules, per-user engine isolation, AI services, observability, storage, and build-time extension groups. Suitable for an external product brochure and visually consistent with a bright premium infographic series.
Title text (verbatim): "RuleGo Server 后端服务"
Subtitle text (verbatim): "开箱即用的规则链管理、执行与智能体服务平台"
Scene/backdrop: bright white to very pale cool-gray background, subtle fine grid and restrained cyan circuit paths, premium enterprise technology aesthetic, no dark background.
Style/medium: refined 2.5D isometric architecture infographic mixed with crisp flat system cards, clean vector-like edges, soft depth, high-end Chinese SaaS launch visual, not a webpage screenshot.
Composition/framing: wide 16:9 landscape. Center is a six-layer modular server stack. Left is access clients and protocols. Right is administration, AI, observability, and extension capabilities. Across the lower third is a numbered API execution lifecycle.
Left access heading exact text: "统一接入"
Access labels: "REST API", "调试 WebSocket", "MCP", "OpenAI 兼容接口", "嵌入式 Bridge", "静态编辑器"
Center architecture stack, exact labels from top to bottom:
"传输与安全层" — "路由 · CORS · 请求限制 · 认证授权 · 异常恢复"
"应用容器层" — "App 生命周期 · Container · Module · Hook"
"业务模块层" — "用户 · 规则链 · 节点 · 运行日志 · 国际化"
"智能与平台层" — "系统智能体 · Skill · 系统配置 · 组件市场 · MCP"
"用户引擎层" — "用户隔离引擎池 · 保存加载 · 启动停止 · 同步异步执行"
"存储与资源层" — "规则文件 · 用户数据 · bbolt / JSONL 日志 · 可替换 Store"
Capability cards, exact Chinese labels:
1. "规则链管理" — "列表、详情、保存、删除、启动与停止"
2. "多方式执行" — "同步、异步、指定起点、单节点与对话接口"
3. "组件与节点服务" — "组件目录、动态节点、共享节点与节点池"
4. "AI 平台能力" — "智能体、模型、提示词、Skill、MCP 与工具安全"
5. "日志与可观测性" — "运行记录、节点调试、实时日志与保留策略"
6. "可嵌入可扩展" — "Bridge、模块替换、存储替换与构建标签"
Build-extension ribbon, exact text:
"with_ai" · "with_iot" · "with_etl" · "with_ci" · "with_extend" · "with_diy"
Interaction flow, exact text and order:
"1 客户端请求" → "2 登录与权限校验" → "3 路由到业务模块" → "4 获取用户隔离引擎" → "5 执行规则链并记录日志" → "6 HTTP 响应或 WebSocket 回传"
Supporting badges, exact text: "独立运行", "嵌入宿主", "用户隔离", "按需构建"
Visual details: show a service container holding nine modules as individual blocks: user, rule, node, runlog, locale, skill, system, marketplace, mcp. Show a per-user engine pool with separate user A and user B lanes. Show RuleGo core engine as a distinct lower internal dependency block labeled "RuleGo 核心引擎", not mixed with server modules. Show storage providers and real-time debug event path.
Color palette: white, ice blue, vivid cyan, fresh green, controlled amber and coral accents, neutral graphite text. API is blue, AI is cyan, security is green, logs are amber, extension modules are coral.
Typography: modern Chinese sans-serif, excellent legibility, correct Simplified Chinese, generous spacing, no tiny body text. Preserve every required Chinese label exactly.
Constraints: clearly distinguish RuleGo Server from RuleGo core and frontend editor; use "启动 / 停止" in user-facing lifecycle wording, not "部署"; arrows must be unambiguous; balanced whitespace; professional external marketing quality.
Avoid: dark mode, black/navy full background, purple gradient dominance, excessive glassmorphism, decorative orbs, illegible microtext, random English beyond required technical names, source code, duplicated labels, garbled Chinese, watermark, external URLs, QR code, generic server-rack stock imagery.
```

## 5. RuleGo 前端编辑器

```text
Use case: infographic-diagram
Asset type: high-resolution 16:9 Chinese marketing infographic for the RuleGo visual frontend editor
Primary request: Create a deeply detailed functional architecture diagram for the RuleGo frontend editor. Show its package architecture, complete visual editing experience, safe save lifecycle, runtime debugging, AI assistant, and React/Vue/Vanilla integration. Suitable for an external product brochure and visually consistent with the bright premium RuleGo core and RuleGo Server infographic series.
Title text (verbatim): "RuleGo 前端编辑器"
Subtitle text (verbatim): "可视化编排，智能辅助，多框架开箱接入"
Scene/backdrop: bright white to very pale cool-gray background, subtle fine grid and restrained cyan circuit paths, premium enterprise technology aesthetic, no dark background.
Style/medium: refined 2.5D isometric product architecture infographic mixed with crisp flat editor UI panels, clean vector-like edges, soft depth, high-end Chinese SaaS launch visual, not a literal browser screenshot.
Composition/framing: wide 16:9 landscape. Center is a realistic visual rule-chain editor surface: searchable component sidebar, node graph canvas, compact icon toolbar, resizable right property drawer, bottom event/run log, and right-side AI assistant. Around it are six capability cards. At the top or lower middle, show the four-package architecture. Across the lower third, show a numbered edit-to-runtime interaction flow.
Package architecture, exact labels:
"editor-core" — "无框架核心、API、状态、事件与独立编辑器"
"editor-ui" — "纯 DOM 工具栏、侧边栏、属性面板"
"editor-react" — "React 组件与 Hooks 适配"
"editor-vue" — "Vue 3 组件与 Composables 适配"
Foundation label exact text: "LogicFlow 图形引擎"
Host integration labels exact text: "React", "Vue 3", "Vanilla JS / HTML"
Capability cards, exact Chinese labels:
1. "规则链工作台" — "搜索、新建、详情、复制、删除、启动与停止"
2. "可视化编排" — "组件拖拽、节点连线、分组、缩放、小地图与搜索"
3. "动态配置表单" — "节点、连线、变量、输入定义、应用集成与代码编辑"
4. "可靠保存" — "变更红点、JSON 校验、Diff、保存回读一致性校验"
5. "运行与调试" — "整链运行、从此节点、仅此节点、记录、事件与链路追溯"
6. "AI 助理" — "对话编排、模型配置、Skill 管理、历史提醒与可调宽度"
Platform badges, exact text: "多主题", "中英双语", "图标与插槽", "宿主认证接入"
Interaction flow, exact text and order:
"1 配置 API 与登录态" → "2 加载组件和规则链" → "3 拖拽编排与配置" → "4 校验并查看变更 Diff" → "5 保存并回读确认" → "6 启动或运行规则链" → "7 WebSocket 日志与链路追溯"
AI collaboration loop, exact text:
"AI 理解当前规则链" → "生成或修改编排" → "人工审查 Diff" → "保存并验证"
Visual details: left component categories include common, filter, transform, action, external, flow, AI, IoT. Canvas shows a clear branching flow with start, filter, transform, AI, external call, join, end. Toolbar uses compact icons. Property drawer shows searchable dynamic fields and code editor. AI assistant is docked beside the canvas and pushes/resizes the canvas rather than floating over it. Show run status and node trace colors.
Color palette: white, ice blue, vivid cyan, fresh green, controlled amber and coral accents, neutral graphite text. Canvas nodes use distinct category colors; AI is cyan; validation is green; unsaved changes are coral; logs are amber.
Typography: modern Chinese sans-serif, excellent legibility, correct Simplified Chinese, generous spacing, no tiny body text. Preserve every required Chinese label exactly.
Constraints: clearly show editor-core as the shared contract beneath React/Vue/Vanilla; distinguish host responsibility for API/auth from editor responsibility for UI and requests; use "启动 / 停止", not "部署"; professional external marketing quality; balanced whitespace; unambiguous arrows.
Avoid: dark mode, black/navy full background, purple gradient dominance, excessive glassmorphism, decorative orbs, illegible microtext, random English beyond required package/framework names, source-code wall, duplicated labels, garbled Chinese, watermark, external URLs, QR code, oversized hero art without functional detail.
```

## 输出文件

- `ai-customer-client-functional-architecture.png`
- `ai-customer-workbench-functional-architecture.png`
- `rulego-core-functional-architecture.png`
- `rulego-server-functional-architecture.png`
- `rulego-editor-functional-architecture.png`
