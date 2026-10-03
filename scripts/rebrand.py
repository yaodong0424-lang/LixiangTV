from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

def replace(path, old, new):
    target = root / path
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"expected text not found in {path}: {old[:80]!r}")
    target.write_text(text.replace(old, new), encoding="utf-8")

replace("backend/cmd/desktop/wails.json", '"name": "BeefTV"', '"name": "LixiangTV"')
replace("backend/cmd/desktop/wails.json", '"outputfilename": "BeefTV"', '"outputfilename": "LixiangTV"')
replace("backend/cmd/desktop/wails.json", '"name": "BeefTV Contributors"', '"name": "理想TV Contributors"')
replace("backend/cmd/desktop/main.go", 'Title:  "BeefTV"', 'Title:  "理想TV"')
replace("backend/cmd/desktop/main.go", 'filepath.Join(root, "BeefTV")', 'filepath.Join(root, "LixiangTV")')

appearance = "web/src/stores/use-appearance-store.ts"
replace(appearance, 'brandName: "BeefTV"', 'brandName: "理想TV"')
replace(appearance, 'brandSlug: "beeftv"', 'brandSlug: "lixiang-tv"')
replace(appearance, 'logoUrl: "/beef-logo.png"', 'logoUrl: "/lixiangtv-logo.svg"')
replace(appearance, 'darkLogoUrl: "/beef-logo.png"', 'darkLogoUrl: "/lixiangtv-logo.svg"')
replace(appearance, 'seoTitle: "BeefTV"', 'seoTitle: "理想TV"')
replace(appearance, 'seoDescription: "BeefTV，本地优先的开源 AI 视频创作工作台。"', 'seoDescription: "理想TV，本地优先的 AI 视频创作工作台。"')
replace(appearance, 'footerCopyright: `© ${new Date().getFullYear()} BeefTV. Open source video studio.`', 'footerCopyright: `© ${new Date().getFullYear()} 理想TV. AI video studio.`')

replace("web/index.html", '<meta name="description" content="AI 影视与短剧创作工作台" />', '<meta name="description" content="理想TV · AI 影视与短剧创作工作台" />')
replace("web/index.html", '<link rel="icon" href="/beef-logo.png" type="image/png" />', '<link rel="icon" href="/lixiangtv-mark.svg" type="image/svg+xml" />')
replace("web/index.html", "<title>正在加载</title>", "<title>理想TV</title>")
replace("web/src/pages/home/home-dashboard.tsx", 'aria-label="BeefTV 首页"', 'aria-label="理想TV 首页"')
# Upstream Agent copy changes frequently; product branding is supplied by appearance settings.
replace("web/src/components/channel-headers-editor.tsx", 'const DEFAULT_USER_AGENT = "BeefTV/1.0 (+https://github.com/glanderness/BeefTV)";', 'const DEFAULT_USER_AGENT = "LixiangTV/1.0";')

replace("scripts/build-beeftv-release.sh", 'echo "Building BeefTV $VERSION_VALUE ($COMMIT_VALUE)"', 'echo "Building 理想TV $VERSION_VALUE ($COMMIT_VALUE)"')
replace("scripts/build-beeftv-release.sh", 'APP_BUNDLE="$DESKTOP_DIR/build/bin/BeefTV.app"', 'APP_BUNDLE="$DESKTOP_DIR/build/bin/LixiangTV.app"')
replace("scripts/build-beeftv-windows-release.ps1", '$exePath = Join-Path $binDir "BeefTV.exe"', '$exePath = Join-Path $binDir "LixiangTV.exe"')
replace("scripts/build-beeftv-windows-release.ps1", 'Write-Step "Building BeefTV $versionValue ($commitValue) for windows/amd64"', 'Write-Step "Building 理想TV $versionValue ($commitValue) for windows/amd64"')
replace("scripts/build-beeftv-windows-release.ps1", '%AppData%\\BeefTV', '%AppData%\\LixiangTV')
replace("scripts/build-beeftv-windows-release.ps1", 'launch BeefTV.exe', 'launch LixiangTV.exe')

mark = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="理想TV">
<defs><linearGradient id="g" x1="8" y1="7" x2="57" y2="58"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs>
<rect width="64" height="64" rx="16" fill="#0b0d14"/><path d="M17 17h8v23h22v8H17V17Z" fill="url(#g)"/><path d="m32 20 17 10-17 10V20Z" fill="#fff"/>
</svg>
"""
logo = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 96" role="img" aria-label="理想TV">
<defs><linearGradient id="g" x1="8" y1="8" x2="84" y2="88"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs>
<rect x="4" y="4" width="88" height="88" rx="23" fill="#0b0d14"/><path d="M27 26h11v34h31v11H27V26Z" fill="url(#g)"/><path d="m47 29 27 16-27 16V29Z" fill="#fff"/>
<text x="112" y="63" fill="currentColor" font-family="Inter, PingFang SC, Microsoft YaHei, sans-serif" font-size="43" font-weight="750">理想TV</text>
</svg>
"""
(root / "web/public/lixiangtv-mark.svg").write_text(mark, encoding="utf-8")
(root / "web/public/lixiangtv-logo.svg").write_text(logo, encoding="utf-8")
print("LixiangTV branding applied.")
