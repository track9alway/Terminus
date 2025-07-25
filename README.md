# Terminus
# Terminus Dominus v5.0 - Dominus Edition

> "To forge an unbreakable shield, one must master the art of the unstoppable spear."

> "For true security is born from understanding absolute destruction."

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Terminus Dominus** is a hyper-advanced adversary emulation and stress-testing framework designed for elite Red Team operations and building anti-fragile systems. It's an educational and professional tool designed to test, not to obliterate.

---

### ⚠️ Legal & Ethical Disclaimer

**This tool is intended for professional, educational, and research purposes only.**

Unauthorized use of Terminus Dominus against any system you do not own or have explicit, written permission to test is **illegal**. Using this tool for malicious purposes constitutes a cybercrime and will lead to severe legal consequences. The author is not responsible for any damage caused by the misuse of this tool. **Use it to fortify, not to obliterate.**

---

### ✨ Key Features

Terminus Dominus is not just another DDoS script. It's a sophisticated framework that simulates a multi-phased cyber-attack.

*   **🛡️ Advanced WAF/JS Challenge Bypassing:** Utilizes a real browser engine (`Playwright`) to solve complex JavaScript challenges (like Cloudflare's "I'm Under Attack Mode"), harvesting valid session cookies to make subsequent attacks appear legitimate.
*   **🗺️ Autonomous Attack Surface Mapping:** The `recon_and_destroy` strategy deploys a recursive crawler to map the entire target website, discovering all possible attack vectors (pages, forms, APIs) instead of just hitting the homepage.
*   **💣 Multi-Vector Attack Capabilities:** Equipped with a diverse arsenal of "warheads":
    *   **HTTP Flood:** A classic, high-volume GET/POST request flood with randomized, realistic payloads.
    *   **Slow Read (Slowloris-like):** Exhausts the target's connection pool by keeping connections open and reading responses at an extremely slow pace.
    *   **HTTP/2 Stream Exhaustion:** Simulates the highly effective **HTTP/2 Rapid Reset** vulnerability (CVE-2023-44487), overwhelming modern servers by rapidly opening and canceling streams.
*   **🧠 Intelligent Assault Strategies:** Move beyond simple attacks with dynamic strategies that mix and match warheads against all discovered targets, making the attack pattern unpredictable and harder to mitigate.
*   **🕶️ Hyper-Realistic Evasion:** Generates highly realistic HTTP headers, user agents, referers, and even spoofs source IPs in headers like `X-Forwarded-For` to mimic real user traffic.
*   **💻 Live C2-Style Battlefield Reporting:** A clean and professional Command & Control (C2) panel provides a real-time report of the operation, including RPS, data transmitted, success/fail codes, and perimeter breach status.

---

### 🆚 Comparison with Other Tools

Terminus Dominus was built to overcome the limitations of traditional tools in the face of modern web defenses.

| Feature                      | Terminus Dominus                 | LOIC / HOIC         | Slowloris           | GoldenEye / HULK    |
| ---------------------------- | -------------------------------- | ------------------- | ------------------- | ------------------- |
| **WAF/JS Challenge Bypass**  | ✅ **Excellent** (via Playwright) | ❌ **None**         | ❌ **None**         | ❌ **None**         |
| **Attack Surface Discovery** | ✅ **Excellent** (Crawler)       | ❌ **None**         | ❌ **None**         | ❌ **None**         |
| **Attack Diversity**         | **High** (Flood, Slow, HTTP/2)   | Low (Flood only)    | Low (Slow only)     | Medium (Flood variants) |
| **HTTP/2 Rapid Reset Sim**   | ✅ **Yes**                       | ❌ **No**           | ❌ **No**           | ❌ **No**           |
| **Realism & Evasion**        | **High**                         | Very Low            | Medium              | Medium              |
| **Primary Use Case**         | Advanced Stress-Testing          | Simple DDoS         | Connection Exhaustion | Advanced Flood      |

---



### ❤️ Support the Mission

This framework is the result of months of dedicated research and development, offered to the security community for free. If you find Terminus Dominus valuable for your research, professional work, or educational purposes, please consider supporting its future development.

Your contribution, no matter the size, fuels the evolution of this tool and ensures it remains at the cutting edge.

**TON:** UQBlAOUM1NLDbupA5FEIw1GZakBos_gXbl7XBYLoqrV5Ewe-

Thank you for being a part of this mission.


