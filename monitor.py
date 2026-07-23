[09/02/48 04:36 م] VII: wafaalkhaildi96@outlook.com
[09/02/48 05:39 م] VII: Predictive IT monitoring system for hospital devices
[09/02/48 05:46 م] VII: # Copyright (c) 2026 Wafaa Al-Khalidi. All rights reserved.
# This code is proprietary and unauthorized copying is strictly prohibited.

from datetime import datetime
import time
import random

# قائمة الأجهزة الحيوية في المستشفى مع عناوينها الشبكية
DEVICES = {
    "Printer_ER_01": "192.168.1.50",
    "XRay_Machine_02": "192.168.1.55",
    "Server_Core": "192.168.1.1",
    "ICU_Monitor_04": "192.168.1.80"
}

print("=== بدء نظام مراقبة المستشفى الاستباقي والذكي (Predictive IT Monitoring) ===")

def predict_failure_risk():
    """خوارزمية محاكاة تنبؤية تحسب نسبة خطر التعطل بناءً على عشوائية سرعة الاستجابة"""
    response_time_ms = random.randint(10, 350) # محاكاة وقت الاستجابة بالمللي ثانية
    
    if response_time_ms > 250:
        risk_status = "⚠️ تحذير: خطر تعطل وشيك (High Risk)"
    elif response_time_ms > 150:
        risk_status = "⚡ تنبيه: أداء بطيء (Medium Risk)"
    else:
        risk_status = "✅ مستقر (Stable)"
        
    return response_time_ms, risk_status

def run_monitoring_cycle():
    """تنفيذ دورة الفحص وتوليد السجلات للأجهزة"""
    for name, ip in DEVICES.items():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        latency, risk_eval = predict_failure_risk()
        
        # طباعة السجلات بتنسيق يدعم التصدير وتغذية لوحات المؤشرات
        print(f"[{current_time}] فحص الجهاز: {name} ({ip}) | الاستجابة: {latency}ms | الحالة والتقييم: {risk_eval}")
        time.sleep(0.5)

if name == "__main__":
    run_monitoring_cycle()
    print("\n--- تم الانتهاء من دورة الفحص الاستباقي وتوليد السجلات بنجاح لتغذية Power BI ---")
