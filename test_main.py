# settings
from selenium_driver import initialize_driver
from preparation import preparation
# 1.0 ver.
from test_login import test_login
from test_prepare import test_prepare
from test_website_browsing import test_website_browsing
from test_banner import test_banner
from test_search_course import test_search_course
from test_news import test_news
from test_FAQ import test_FAQ
from test_featured_courses import test_featured_courses
from test_other_sites import test_other_sites
from test_download import test_download
from test_security_policy import test_security_policy
from test_privacy_policy import test_privacy_policy
from test_footer import test_footer
from test_change_language import test_change_language
from test_my_schedule import test_my_schedule
from test_study_record import test_study_record
from test_calendar import test_calendar
from test_school_qtn import test_school_qtn
from test_personal_data import test_personal_data
from admin_enter import admin_enter
from admin_person_management import admin_person_management
from admin_user_list import admin_user_list
from admin_add_account import admin_add_account
from admin_review_account import admin_review_account
from admin_admin_setting import admin_admin_setting
from admin_person_list import admin_person_list
from admin_class import admin_class
from admin_import_class import admin_import_class
from admin_course_center import admin_course_center
from admin_course_group import admin_course_group
from admin_course_setting import admin_course_setting
from admin_course_information import admin_course_information
from admin_teacher_setting import admin_teacher_setting
from admin_teacher_manage import admin_teacher_manage
from admin_management_center import admin_management_center
from admin_carousel import admin_carousel
from admin_weblink import admin_weblink
from admin_home_download import admin_homedownload
from admin_news import admin_news
from admin_FAQ import admin_FAQ
from admin_platform_setting import admin_platform_setting
from admin_home_file import admin_homefile
from admin_school_statistics import admin_school_statistics
from admin_questionbank import admin_questionbank
from admin_questionnaire import admin_questionnaire
from admin_resultsview import admin_resultsview
from teacher_enter import teacher_enter
from teacher_adddelete_student import teacher_adddelete_student
from teacher_course_statistics import teacher_course_statistics
from teacher_review_account import teacher_review_account
from teacher_export_stuinfo import teacher_export_stuinfo
from teacher_warning import teacher_warning
from teacher_rollcall_history import teacher_rollcall_history
from teacher_student_group import teacher_student_group
from teacher_setup_assistant import teacher_setup_assistant
from teacher_file_upload import teacher_file_upload
from teacher_file_management import teacher_file_management
from teacher_learning_path import teacher_learning_path
from teacher_course_setting import teacher_course_setting
from teacher_file_import import teacher_file_import
from teacher_file_statistics import teacher_file_statistics
from teacher_course_copy import teacher_course_copy
from teacher_discussion_management import teacher_discussion_management
from teacher_notice_board import teacher_notice_board
from teacher_chatroom_management import teacher_chatroom_management
from teacher_course_calendar import teacher_course_calendar
from teacher_hw_questionbank import teacher_hw_questionbank
from teacher_hw_maintenance import teacher_hw_maintenance
from teacher_hw_correct import teacher_hw_correct
from teacher_peer_maintenance import teacher_peer_maintenance
from teacher_peer_correct import teacher_peer_correct
from teacher_rating_management import teacher_rating_management
from teacher_exam_questionbank import teacher_exam_questionbank
from teacher_exam_maintenance import teacher_exam_maintenance
from teacher_exam_correct import teacher_exam_correct
from teacher_qnr_questionbank import teacher_qnr_questionbank
from teacher_qnr_maintenance import teacher_qnr_maintenance
from teacher_qnr_resultsview import teacher_qnr_resultsview
from teacher_score_management import teacher_score_management
from teacher_score_summary import teacher_score_summary
from course_enter import course_enter1
# from course_enter import course_enter2
from course_prepare import course_prepare
from course_chapter import course_chapter
from course_announcement import course_announcement 
from course_note import course_note
from course_forum import course_forum
from course_questionnaire import course_questionnaire
from course_homework import course_homework
from course_exam import course_exam
from course_attendance import course_attendance
from course_score import course_score
from course_chatroom import course_chatroom
from course_chatroom_history import course_chatroom_history
from course_addressbook import course_addressbook
from datetime import datetime
# 1.1 ver.
from test_course_note import test_course_note
from test_smart_note import test_smart_note
from test_personal_aiphoto import test_personal_aiphoto
from course_self_challenge import course_self_challenge
from course_read_club import course_read_club
from teacher_exam_aiquestion import teacher_exam_aiquestion
from teacher_course_aiphoto import teacher_course_aiphoto
from teacher_course_aiintro import teacher_course_aiintro
from teacher_video_list import teacher_video_list
from teacher_video_subtitle import teacher_video_subtitle
from teacher_video_IVQquestions import teacher_video_IVQquestions
from teacher_video_IVQstatistics import teacher_video_IVQstatistics

import time
import os
from dotenv import load_dotenv
nowdatetime = datetime.now().strftime("%Y-%m-%d %H:%M")

def main():

    #-----------------------------------------------------------1.0
    #-----------------------------------------------------------
    load_dotenv()
    print(f"\033[34m測試時間：{nowdatetime}\033[0m")
    print(f"\033[34m測試帳號：{os.getenv('XUMI_USERNAME')}\033[0m")
    driver = initialize_driver()

    # test_login(driver) #登入
    time.sleep(5)
    # preparation(driver) #測試帳號建置
    # test_prepare(driver) # 首頁資料建置
    # test_banner(driver) #Banner
    # test_change_language(driver) #切換語系
    # test_website_browsing(driver) #網站導覽
    # test_search_course(driver) #進階搜尋
    # test_news(driver) #最新消息
    # test_FAQ(driver) #常見問題
    # test_download(driver) #下載專區
    # test_featured_courses(driver) #精選課程
    # test_other_sites(driver) #相關網站連結
    test_security_policy(driver) #資訊安全政策
    test_privacy_policy(driver) #隱私權宣告
    # test_footer(driver) # 頁尾分享
    # test_my_schedule(driver) #我的課表
    # test_study_record(driver) #學習紀錄
    # test_calendar(driver) #行事曆
    # test_school_qtn(driver) #問卷調查
    # test_personal_data(driver) #個人資料
    #-----------------------------------------------------------
    # teacher_enter(driver) #進入辦公室
    # teacher_adddelete_student(driver) #辦公室-增刪學員
    # teacher_review_account(driver) #辦公室-審核學員
    # teacher_course_statistics(driver) #辦公室-到課統計
    # teacher_export_stuinfo(driver) #辦公室-匯出人員資料
    # teacher_warning(driver) #辦公室-預警通知
    # teacher_rollcall_history(driver) #辦公室-點名歷程
    # teacher_student_group(driver) #辦公室-學員分組
    # teacher_setup_assistant(driver) #辦公室-設定助教

    # teacher_file_upload(driver) #辦公室-教材上傳
    # teacher_file_management(driver) #辦公室-教材檔案管理
    # teacher_learning_path(driver) #辦公室-學習路徑管理
    # teacher_course_setting(driver) #辦公室-課程設定
    # teacher_file_import(driver) #辦公室-教材匯入
    # teacher_file_statistics(driver) #辦公室-教材統計
    # teacher_course_copy(driver) #辦公室-課程複製精靈

    # teacher_discussion_management(driver) #辦公室-討論區
    # teacher_notice_board(driver) #辦公室-課程公告板
    # teacher_chatroom_management(driver) #辦公室-聊天室管理
    # teacher_course_calendar(driver) #辦公室-課程行事曆

    # teacher_hw_questionbank(driver) #辦公室-作業題庫維護
    # teacher_hw_maintenance(driver) #辦公室-作業維護
    # teacher_hw_correct(driver) #辦公室-作業批改

    # teacher_peer_maintenance(driver) #辦公室-同儕作業維護
    # teacher_peer_correct(driver) #辦公室-同儕作業批改
    # teacher_rating_management(driver) #辦公室-評量表管理

    # teacher_exam_questionbank(driver) #辦公室-測驗題庫維護
    # teacher_exam_maintenance(driver) #辦公室-試卷維護
    # teacher_exam_correct(driver) #辦公室-試卷批改

    # teacher_qnr_questionbank(driver) #辦公室-問卷題庫維護
    # teacher_qnr_maintenance(driver) #辦公室-問卷維護
    # teacher_qnr_resultsview(driver) #辦公室-結果檢視

    # teacher_score_management(driver) #辦公室-成績管理
    # teacher_score_summary(driver) #辦公室-成績總表(yyytest/yqi)
    #-----------------------------------------------------------
    # admin_enter(driver) #進入管理者環境
    # admin_person_management(driver) #人員管理
    # admin_user_list(driver) #查詢人員
    # admin_add_account(driver) #新增帳號
    # admin_review_account(driver) #審核帳號(須有註冊功能)
    # admin_admin_setting(driver) #管理者設定

    # admin_person_list(driver) #人員管理
    # admin_class(driver) #群組管理
    # admin_import_class(driver) #匯入群組成員

    # admin_course_center(driver) #課程中心
    # admin_course_group(driver) #課程群組
    # admin_course_setting(driver) #課程設定
    # admin_course_information(driver) #課程資訊

    # admin_teacher_setting(driver) #教師設定
    # admin_teacher_manage(driver) #教師維護

    # admin_management_center(driver) #管理中心
    # admin_platform_setting(driver) #平台設定
    # admin_homefile(driver) #首頁檔案管理
    # admin_school_statistics(driver) #平台統計資料

    # admin_carousel(driver) #首頁活動輪播
    # admin_weblink(driver) #網頁連結
    # admin_homedownload(driver) #首頁下載專區
    # admin_news(driver) #最新消息
    # admin_FAQ(driver) #常見問題

    # admin_questionbank(driver) #題庫維護
    # admin_questionnaire(driver) #問卷維護
    # admin_resultsview(driver) #結果檢視
    #-----------------------------------------------------------
    # course_prepare(driver) #課程資料建置
    # course_enter1(driver) #進入課程-自動化測試主課程
    # course_chapter(driver) #課程章節
    # course_announcement(driver) #課程公告
    # course_note(driver) #課程筆記
    # course_forum(driver) #課程討論區
    # course_homework(driver) #作業
    # course_exam(driver) #測驗
    # course_questionnaire(driver) #問卷
    # course_attendance(driver) #出席紀錄
    # course_score(driver) #學習成績                                
    # course_chatroom(driver) #聊天室/讀書會
    # course_chatroom_history(driver) #聊天室紀錄/讀書會紀錄
    # course_addressbook(driver) #通訊錄
    #-----------------------------------------------------------1.1
    #-----------------------------------------------------------
    # test_course_note(driver) #筆記空間
    # test_personal_aiphoto(driver) #AI生成人像
    # course_enter1(driver) #進入課程-自動化測試主課程
    # course_read_club(driver) #讀書會
    #-----------------------------------------------------------
    # teacher_enter(driver) #進入辦公室
    # teacher_course_aiphoto(driver) #AI課程代表圖
    # teacher_course_aiintro(driver) #AI課程介紹
    # teacher_exam_aiquestion(driver) #AI智能出題
    # teacher_video_list(driver) #全能影像轉譯-影片列表
    # teacher_video_subtitle(driver) #全能影像轉譯-AI生成字幕與摘要
    # teacher_video_IVQquestions(driver) #全能影像轉譯-IVQ題庫
    # teacher_video_IVQstatistics(driver) #全能影像轉譯-IVQ統計
    #-----------------------------------------------------------1.2
    #-----------------------------------------------------------
    # test_smart_note(driver) #智匯筆記
    # course_self_challenge(driver) #自我挑戰

    return "result"

if __name__ == "__main__":
    main()