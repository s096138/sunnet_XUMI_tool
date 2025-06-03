from flask import Flask, render_template, request, jsonify, send_file
import subprocess
import os
import sys
import json
import logging
import traceback
from io import StringIO
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from datetime import datetime
import test_main

def setup_logger():
    """設置日誌記錄"""
    # 確保 logs 目錄存在
    os.makedirs('logs', exist_ok=True)
    
    # 創建日誌記錄器
    logger = logging.getLogger('XUMI_TEST')
    logger.setLevel(logging.DEBUG)
    
    # 移除所有現有的處理程序
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # 創建文件處理程序
    file_handler = RotatingFileHandler(
        'logs/xumi_test.log', 
        maxBytes=1024*1024,  # 1MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    
    # 創建控制台處理程序
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # 設置日誌格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加處理程序
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 設置日誌記錄器
logger = setup_logger()

# 設置 Flask 應用程式
app = Flask(__name__)
app.logger.handlers = logger.handlers
app.logger.setLevel(logging.DEBUG)

# 確保歷史紀錄目錄存在
HISTORY_DIR = os.path.join(os.path.dirname(__file__), 'test_history')
os.makedirs(HISTORY_DIR, exist_ok=True)
HISTORY_DIR = os.path.join(os.path.dirname(__file__), 'test_history')
os.makedirs(HISTORY_DIR, exist_ok=True)

# 測試檔案名稱對照表
TEST_NAME_MAPPING = {
    # 資料建置
    'preparation': '前置作業-測試帳號建置',
    'test_prepare': '前置作業-首頁資料建置',
    'course_prepare': '前置作業-課程資料建置',
    
    # 首頁
    'test_login': '首頁-登入',
    'test_banner': '首頁-Banner',
    'test_change_language': '首頁-切換語系',
    'test_website_browsing': '首頁-網站導覽',
    'test_search_course': '首頁-進階搜尋',
    'test_news': '首頁-最新消息',
    'test_FAQ': '首頁-常見問題',
    'test_download': '首頁-下載專區',
    'test_featured_courses': '首頁-精選課程',
    'test_other_sites': '首頁-相關網站連結',
    'test_security_policy': '首頁-資訊安全政策',
    'test_privacy_policy': '首頁-隱私權宣告',
    'test_footer': '首頁-頁尾分享',
    'test_my_schedule': '首頁-我的課表',
    'test_study_record': '首頁-學習紀錄',
    'test_calendar': '首頁-行事曆',
    'test_school_qtn': '首頁-問卷調查',
    'test_personal_data': '首頁-個人資料',
    
    # 教師環境 - 人員管理
    'teacher_enter': '教師環境-進入辦公室',
    'teacher_adddelete_student': '教師環境-增刪學員',
    'teacher_review_account': '教師環境-審核學員',
    'teacher_course_statistics': '教師環境-到課統計',
    'teacher_export_stuinfo': '教師環境-匯出人員資料',
    'teacher_warning': '教師環境-預警通知',
    'teacher_rollcall_history': '教師環境-點名歷程',
    'teacher_student_group': '教師環境-學員分組',
    'teacher_setup_assistant': '教師環境-設定助教',
    
    # 教師環境 - 課程管理
    'teacher_file_upload': '教師環境-教材上傳',
    'teacher_file_management': '教師環境-教材檔案管理',
    'teacher_learning_path': '教師環境-學習路徑管理',
    'teacher_course_setting': '教師環境-課程設定',
    'teacher_file_import': '教師環境-教材匯入',
    'teacher_file_statistics': '教師環境-教材統計',
    'teacher_course_copy': '教師環境-課程複製精靈',
    
    # 教師環境 - 教室管理
    'teacher_discussion_management': '教師環境-討論區',
    'teacher_notice_board': '教師環境-課程公告板',
    'teacher_chatroom_management': '教師環境-聊天室管理',
    'teacher_course_calendar': '教師環境-課程行事曆',
    
    # 教師環境 - 作業管理
    'teacher_hw_questionbank': '教師環境-作業題庫維護',
    'teacher_hw_maintenance': '教師環境-作業維護',
    'teacher_hw_correct': '教師環境-作業批改',

    # 教師環境 - 同儕作業管理
    'teacher_peer_maintenance': '教師環境-同儕作業維護',
    'teacher_peer_correct': '教師環境-同儕作業批改',
    'teacher_rating_management': '教師環境-評量表管理',
    
    # 教師環境 - 測驗管理
    'teacher_exam_questionbank': '教師環境-測驗題庫維護',
    'teacher_exam_maintenance': '教師環境-試卷維護',
    'teacher_exam_correct': '教師環境-試卷批改',
    
    # 教師環境 - 問卷管理
    'teacher_qnr_questionbank': '教師環境-問卷題庫維護',
    'teacher_qnr_maintenance': '教師環境-問卷維護',
    'teacher_qnr_resultsview': '教師環境-結果檢視',
    
    # 教師環境 - 成績管理
    'teacher_score_management': '教師環境-成績管理',
    'teacher_score_summary': '教師環境-成績總表',
    
    # 管理者環境
    'admin_enter': '管理者環境-進入管理者環境',
    'admin_person_management': '管理者環境-人員管理',
    'admin_user_list': '管理者環境-查詢人員',
    'admin_add_account': '管理者環境-新增帳號',
    'admin_review_account': '管理者環境-審核帳號',
    'admin_admin_setting': '管理者環境-管理者設定',
    'admin_person_list': '管理者環境-人員管理',
    'admin_class': '管理者環境-群組管理',
    'admin_import_class': '管理者環境-匯入群組成員',
    'admin_course_center': '管理者環境-課程中心',
    'admin_course_group': '管理者環境-課程群組',
    'admin_course_setting': '管理者環境-課程設定',
    'admin_course_information': '管理者環境-課程資訊',
    'admin_teacher_setting': '管理者環境-教師設定',
    'admin_teacher_manage': '管理者環境-教師維護',
    'admin_management_center': '管理者環境-管理中心',
    'admin_platform_setting': '管理者環境-平台設定',
    'admin_home_file': '管理者環境-首頁檔案管理',
    'admin_school_statistics': '管理者環境-平台統計資料',
    'admin_carousel': '管理者環境-首頁活動輪播',
    'admin_weblink': '管理者環境-網頁連結',
    'admin_home_download': '管理者環境-首頁下載專區',
    'admin_news': '管理者環境-最新消息',
    'admin_FAQ': '管理者環境-常見問題',
    'admin_questionbank': '管理者環境-題庫維護',
    'admin_questionnaire': '管理者環境-問卷維護',
    'admin_resultsview': '管理者環境-結果檢視',
    
    # 學生環境
    'course_enter1': '學生環境-進入課程-自動化測試主課程',
    'course_chapter': '學生環境-課程章節',
    'course_announcement': '學生環境-課程公告',
    'course_note': '學生環境-課程筆記',
    'course_forum': '學生環境-課程討論區',
    'course_homework': '學生環境-作業',
    'course_exam': '學生環境-測驗',
    'course_questionnaire': '學生環境-問卷',
    'course_attendance': '學生環境-出席紀錄',
    'course_score': '學生環境-學習成績',
    'course_chatroom': '學生環境-聊天室/讀書會',
    'course_chatroom_history': '學生環境-聊天室紀錄/讀書會紀錄',
    'course_addressbook': '學生環境-通訊錄',
    
    # 標配版
    'test_course_note': '標配版-筆記空間',
    'test_personal_aiphoto': '標配版-AI生成人像',
    'course_read_club': '標配版-讀書會',
    'teacher_course_aiphoto': '標配版-AI課程代表圖',
    'teacher_course_aiintro': '標配版-AI課程介紹',
    'teacher_exam_aiquestion': '標配版-AI智能出題',
    'teacher_video_list': '標配版-全能影像轉譯-影片列表',
    'teacher_video_subtitle': '標配版-全能影像轉譯-AI生成字幕與摘要',
    'teacher_video_IVQquestions': '標配版-全能影像轉譯-IVQ題庫',
    'teacher_video_IVQstatistics': '標配版-全能影像轉譯-IVQ統計',
    'test_smart_note': '標配版-智匯筆記',
    'course_self_challenge': '標配版-自我挑戰'
}

# 可用的測試模組清單
TEST_MODULES = list(TEST_NAME_MAPPING.keys())

@app.route('/')
def index():
    # 初始化 categories 變數
    categories = {
        'preparation': {'name': '前置作業', 'items': []},
        'homepage': {'name': '首頁', 'items': []},
        'teacher': {'name': '教師環境', 'items': []},
        'admin': {'name': '管理者環境', 'items': []},
        'student': {'name': '學生環境', 'items': []},
        'standard': {'name': '標配版', 'items': []},
        'other': {'name': '其他', 'items': []}
    }
    
    # 將測試模組按分類分組
    for module in TEST_MODULES:
        display_name = TEST_NAME_MAPPING.get(module, module)
        
        if display_name.startswith('前置作業'):
            categories['preparation']['items'].append((module, display_name))
        elif display_name.startswith('首頁'):
            categories['homepage']['items'].append((module, display_name))
        elif display_name.startswith('教師環境'):
            categories['teacher']['items'].append((module, display_name))
        elif display_name.startswith('管理者環境'):
            categories['admin']['items'].append((module, display_name))
        elif display_name.startswith('學生環境'):
            categories['student']['items'].append((module, display_name))
        elif display_name.startswith('標配版'):
            categories['standard']['items'].append((module, display_name))
        else:
            # 如果無法分類，則放入其他分類
            categories['other']['items'].append((module, display_name))
    
    # 確保所有分類都存在於字典中
    for category in categories.values():
        if 'items' not in category:
            category['items'] = []
    
    # 將分類轉換為列表，並過濾掉沒有項目的分類
    categories_list = []
    for cid, data in categories.items():
        if data['items']:  # 只保留有項目的分類
            categories_list.append({
                'id': cid, 
                'name': data['name'], 
                'items': data['items'],  # 這應該已經是一個列表
                'items_count': len(data['items'])  # 預先計算長度
            })
    
    return render_template('index.html', categories=categories_list)

@app.route('/run_tests', methods=['POST'])
def run_tests():
    logger.info("收到測試請求")
    
    # 初始化變數
    success = False
    returncode = 1
    output = ""
    target_url = ""
    selected_tests = []
    old_stdout = None
    old_stderr = None
    stdout_buffer = None
    stderr_buffer = None
    
    try:
        if not request.is_json:
            error_msg = '請求必須是 JSON 格式'
            logger.error(error_msg)
            return jsonify({'success': False, 'error': error_msg}), 400
            
        data = request.get_json()
        logger.debug(f"請求數據: {data}")
        
        if not data:
            error_msg = '未提供請求數據'
            logger.error(error_msg)
            return jsonify({'success': False, 'error': error_msg}), 400
            
        target_url = data.get('target_url', '').strip()
        selected_tests = data.get('selected_tests', [])
        
        logger.info(f"測試網址: {target_url}")
        logger.info(f"選擇的測試項目: {selected_tests}")
        
        if not isinstance(selected_tests, list):
            error_msg = 'selected_tests 必須是列表類型'
            logger.error(error_msg)
            return jsonify({'success': False, 'error': error_msg}), 400
        
        # 驗證測試網址是否提供
        if not target_url:
            error_msg = '測試網址為必填欄位'
            logger.error(error_msg)
            return jsonify({'success': False, 'error': error_msg}), 400
            
        # 驗證 URL 格式
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(target_url)
            if not all([parsed_url.scheme, parsed_url.netloc]):
                error_msg = f'無效的網址格式: {target_url}'
                logger.error(error_msg)
                raise ValueError(error_msg)
            logger.info(f"網址格式驗證通過: {target_url}")
        except Exception as e:
            error_msg = f'請輸入有效的網址 (例如: https://example.com): {str(e)}'
            logger.error(error_msg)
            return jsonify({'success': False, 'error': error_msg}), 400
        
        # 更新 .env 檔案中的測試網址
        try:
            logger.info("開始更新 .env 檔案...")
            env_vars = {}
            
            # 讀取現有的 .env 檔案（如果存在）
            if os.path.exists('.env'):
                logger.info("找到現有的 .env 檔案，讀取內容...")
                with open('.env', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            try:
                                key, value = line.split('=', 1)
                                key = key.strip()
                                value = value.strip()
                                env_vars[key] = value
                                logger.debug(f"讀取環境變數: {key}={value}")
                            except ValueError as ve:
                                logger.warning(f"跳過無效的行: {line}")
                                continue
            
            # 更新環境變數
            logger.info(f"更新環境變數: BASE_URL={target_url}")
            
            # 更新環境變數（記憶體中）
            os.environ['BASE_URL'] = target_url
            
            # 更新 .env 檔案中的變數
            env_vars['BASE_URL'] = target_url
            
            # 如果存在 TARGET_URL，則刪除它（遷移到 BASE_URL）
            if 'TARGET_URL' in env_vars:
                del env_vars['TARGET_URL']
            
            # 寫回 .env 檔案
            with open('.env', 'w', encoding='utf-8') as f:
                for key, value in env_vars.items():
                    f.write(f'{key}={value}\n')
                    
            logger.info("成功更新 .env 檔案")
            
        except Exception as e:
            error_msg = f'更新設定檔時發生錯誤: {str(e)}'
            logger.error(error_msg, exc_info=True)
            return jsonify({'success': False, 'error': error_msg}), 500
        
        # 更新 test_main.py 中的測試選項
        try:
            test_main_path = 'test_main.py'
            logger.info(f"開始更新測試檔案: {test_main_path}")
            
            if not os.path.exists(test_main_path):
                error_msg = f'找不到測試檔案: {test_main_path}'
                logger.error(error_msg)
                return jsonify({'success': False, 'error': error_msg}), 500
            
            # 讀取原始內容
            with open(test_main_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 創建一個字典來跟踪測試函數的狀態
            test_functions = {}
            
            # 分析檔案，找出所有測試函數調用
            for i, line in enumerate(lines):
                line = line.strip()
                # 匹配 test_ 開頭的函數調用
                if 'test_' in line and '(driver)' in line:
                    # 檢查是否被註解
                    is_commented = line.startswith('#')
                    # 獲取函數名
                    func_name = line.split('(')[0].replace('#', '').strip()
                    test_functions[func_name] = {
                        'line_num': i,
                        'is_commented': is_commented,
                        'original_line': lines[i]
                    }
            
            logger.info(f"找到 {len(test_functions)} 個測試函數")
            
            # 更新選中的測試函數
            updated = False
            # 先處理所有需要取消註解的行
            for func_name in selected_tests:
                if func_name in test_functions:
                    func_info = test_functions[func_name]
                    line_num = func_info['line_num']
                    original_line = lines[line_num].rstrip('\n')
                    
                    # 如果被註解了，就取消註解
                    if func_info['is_commented']:
                        # 保留縮進，只移除行首的 # 字符
                        leading_spaces = len(original_line) - len(original_line.lstrip())
                        indentation = ' ' * leading_spaces
                        content = original_line[leading_spaces:].lstrip('#').lstrip()
                        lines[line_num] = f"{indentation}{content}\n"
                        updated = True
                        logger.info(f"已取消註解: {func_name}")
            
            # 然後處理所有需要加上註解的行
            for func_name, func_info in test_functions.items():
                line_num = func_info['line_num']
                original_line = lines[line_num].rstrip('\n')
                
                # 如果這個函數沒有被選中，確保有註解
                if func_name not in selected_tests:
                    # 如果沒有被註解，就加上註解
                    if not func_info['is_commented']:
                        leading_spaces = len(original_line) - len(original_line.lstrip())
                        indentation = ' ' * leading_spaces
                        content = original_line[leading_spaces:].strip()
                        lines[line_num] = f"{indentation}# {content}\n"
                        updated = True
                        logger.info(f"已加上註解: {func_name}")
            
            # 寫回檔案
            if updated:
                with open(test_main_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                logger.info("成功更新測試檔案")
            else:
                logger.info("沒有需要更新的測試函數")
                    
        except Exception as e:
            error_msg = f'更新測試檔案時發生錯誤: {str(e)}'
            logger.error(error_msg, exc_info=True)
            return jsonify({'success': False, 'error': error_msg}), 500
        
        # 重定向標準輸出和標準錯誤
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        stdout_buffer = StringIO()
        stderr_buffer = StringIO()
        
        sys.stdout = stdout_buffer
        sys.stderr = stderr_buffer
        
        logger.info("開始執行測試...")
        success = False
        returncode = 1
        output = ""
        
        try:
            # 執行測試
            test_main.main()
            success = True
            returncode = 0
            logger.info("測試執行完成，返回碼: 0")
            
        except SystemExit as e:
            # 處理 sys.exit() 調用
            returncode = e.code if isinstance(e.code, int) else 1
            success = returncode == 0
            logger.info(f"測試執行完成，返回碼: {returncode}")
            
        except Exception as e:
            error_msg = f"執行測試時發生異常: {str(e)}"
            logger.error(error_msg, exc_info=True)
            print(traceback.format_exc(), file=sys.stderr)
            success = False
            returncode = 1
            
        finally:
            # 獲取輸出
            output = stdout_buffer.getvalue() + stderr_buffer.getvalue()
            
            # 恢復標準輸出和標準錯誤
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            
            # 記錄輸出
            logger.info(f"測試輸出:\n{output}")
            
            # 定義 ANSI 轉 HTML 的函數
            def ansi_to_html(text):
                if not text:
                    return ''
                # 替換 ANSI 顏色代碼
                text = text.replace('\033[0m', '</span>')
                text = text.replace('\033[34m', '<span style="color: blue">')
                text = text.replace('\033[32m', '<span style="color: green">')
                text = text.replace('\033[31m', '<span style="color: red">')
                text = text.replace('\033[33m', '<span style="color: yellow">')
                # 替換換行符
                text = text.replace('\n', '<br>')
                return f'<div style="font-family: monospace; white-space: pre-wrap;">{text}</div>'
            
            # 確保 WebDriver 被清理
            try:
                from selenium_driver import cleanup_drivers
                cleanup_drivers()
                logger.info("測試完成後清理 WebDriver 實例")
            except Exception as e:
                logger.warning(f"測試完成後清理 WebDriver 時發生警告: {str(e)}")
            
            # 保存測試結果到歷史紀錄
            try:
                # 檢查測試是否成功：
                # 1. 沒有標準錯誤輸出，或標準錯誤中不包含錯誤關鍵字
                # 2. 返回碼為0
                stderr_content = stderr_buffer.getvalue().strip()
                stdout_content = stdout_buffer.getvalue().strip()
                
                # 檢查標準輸出中是否包含失敗訊息
                has_failure_in_stdout = ('fail' in stdout_content.lower() or 
                                      'error' in stdout_content.lower() or 
                                      'exception' in stdout_content.lower())
                
                has_error_output = bool(stderr_content and 
                                     ('error' in stderr_content.lower() or 
                                      'fail' in stderr_content.lower() or
                                      'exception' in stderr_content.lower()))
                
                # 檢查輸出中是否包含 'WebDriver 錯誤' 字樣
                has_webdriver_error = ('webdriver 錯誤' in stdout_content.lower() or 
                                     'webdriver 錯誤' in stderr_content.lower())
                
                # 如果有 WebDriver 錯誤，則測試失敗
                test_success = (not has_error_output and 
                              not has_failure_in_stdout and 
                              not has_webdriver_error and 
                              returncode == 0)
                
                logger.info(f"測試成功狀態: {test_success}, 返回碼: {returncode}, "
                           f"錯誤輸出: {bool(stderr_content)}, 標準輸出包含失敗: {has_failure_in_stdout}")
                
                # 保存原始輸出，不包含 HTML 標籤
                history_entry = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'target_url': target_url,
                    'selected_tests': selected_tests,
                    'output': stdout_buffer.getvalue() or stderr_buffer.getvalue(),
                    'success': test_success
                }
                filename = f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(os.path.join(HISTORY_DIR, filename), 'w', encoding='utf-8') as f:
                    json.dump(history_entry, f, ensure_ascii=False, indent=2)
                logger.info(f"已保存測試結果到 {filename}")
            except Exception as e:
                logger.error(f"保存測試結果時發生錯誤: {str(e)}")
            
            # 返回測試結果
            result = {
                'success': test_success,  # 使用計算出的 test_success
                'output': output,
                'stdout': ansi_to_html(stdout_buffer.getvalue()),
                'stderr': ansi_to_html(stderr_buffer.getvalue()),
                'returncode': returncode
            }
            
            logger.info(f"測試執行完成，結果: {result}")
            return jsonify(result)
            
    except ImportError as e:
        error_msg = f"無法導入測試模組: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return jsonify({
            'success': False,
            'error': error_msg,
            'traceback': traceback.format_exc(),
            'exception_type': 'ImportError'
        }), 500
            
    except Exception as e:
        error_msg = f"執行測試時發生未預期的錯誤: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return jsonify({
            'success': False,
            'error': error_msg,
            'traceback': traceback.format_exc(),
            'exception_type': type(e).__name__
        }), 500

# 獲取測試歷史紀錄
@app.route('/get_test_history', methods=['GET'])
def get_test_history():
    try:
        # 獲取分頁參數，如果沒有提供則使用默認值
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 5))  # 每頁顯示5筆
        
        history_files = sorted(os.listdir(HISTORY_DIR), reverse=True)
        history = []
        
        # 計算分頁的起始和結束索引
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        
        # 只處理當前頁需要的檔案
        for filename in history_files[start_idx:end_idx]:
            if not filename.endswith('.json'):
                continue
                
            with open(os.path.join(HISTORY_DIR, filename), 'r', encoding='utf-8') as f:
                try:
                    entry = json.load(f)
                    history.append({
                        'timestamp': entry.get('timestamp', ''),
                        'target_url': entry.get('target_url', ''),
                        'selected_tests': entry.get('selected_tests', []),
                        'success': entry.get('success', False),
                        'filename': filename
                    })
                except json.JSONDecodeError:
                    continue
        
        # 計算總頁數
        total_items = len([f for f in history_files if f.endswith('.json')])
        total_pages = (total_items + per_page - 1) // per_page
                    
        return jsonify({
            'success': True, 
            'history': history,
            'pagination': {
                'current_page': page,
                'per_page': per_page,
                'total_items': total_items,
                'total_pages': total_pages
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# 獲取單個歷史紀錄的詳細內容
@app.route('/get_history_detail/<filename>', methods=['GET'])
def get_history_detail(filename):
    try:
        filepath = os.path.join(HISTORY_DIR, filename)
        if not os.path.exists(filepath) or '..' in filename or '/' in filename:
            return jsonify({'success': False, 'error': 'File not found'})
            
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 確保返回的數據結構與前端預期一致
            return jsonify({
                'success': True, 
                'output': data.get('output', ''),
                'target_url': data.get('target_url', ''),
                'selected_tests': data.get('selected_tests', []),
                'success_status': data.get('success', False),
                'timestamp': data.get('timestamp', '')
            })
    except Exception as e:
        logger.error(f"獲取歷史紀錄詳情時發生錯誤: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # 確保 templates 目錄存在
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, port=5000)
