# 来源协议

这是独立合成的大厅资料接入项目，不包含个人资料或真实政务凭据。来源入口样例为 `/odata/start?scope=east`，所有相对链接以响应 URL 为基准。来源账号、访问范围和允许访问的 origin 由调用配置提供；真实密钥不应保存在资料中。

OData JSON：value 为实体数组；id 为来源内实体键。nextLink 与 deltaLink 为来源生成的相对或绝对链接，必须保留原查询。@removed 的 reason=changed 表示退出本查询集合，reason=deleted 表示来源实体删除；本地只能在已核实的订阅范围应用。410 表示该订阅令牌失效。分页世代由 X-Collection-Epoch 标识。授权来源只允许配置的 origin。

## 已有接口

acquire.transport.fetch 保留 HTTP 状态、原始响应头与实体字节，不自动跟随重定向。一次读取最多 max_bytes，超出时报错；当前默认超时5秒，已有单次调用语义继续有效。Response.header 大小写不敏感，sha256 只描述响应实体字节，不证明业务完整性。

acquire.decode.decode(body,headers) 返回 key/value 数组，当前只解释 fixtures/response.bin 中的一份响应。acquire.store.Store 在一个本地事务中保存响应与当前 key/value，尚无协议进度和跨响应完整性解释。acquire.service.collect_one 绑定 URL、原件及已解读记录，兼容这些单次操作的返回字段。

来源回放程序支持任意 HTTP 路径、请求体条件、响应序列及字节原件，配置不等同于完整的远端系统。缺失路由不可当成协议承诺；使用者可按上述协议补充来源行为进行联调。样本内容不限定实际输入规模或异常组合。
