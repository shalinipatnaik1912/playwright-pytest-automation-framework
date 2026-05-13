import subprocess
import webbrowser
import os
from datetime import datetime

def run_tests_and_generate_report():
    """Run tests and automatically open the HTML report"""
    
    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)
    
    # Generate timestamp for report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"reports/report_{timestamp}.html"
    
    print("🧪 Running Playwright tests...")
    
    # Run pytest with HTML report
    result = subprocess.run([
        "pytest",
        "--html=" + report_path,
        "--self-contained-html",
        "-v"
    ])
    
    # Check if tests ran
    if os.path.exists(report_path):
        print(f"✅ Tests completed! Report generated: {report_path}")
        
        # Automatically open report in browser
        print("📊 Opening report in browser...")
        webbrowser.open(f"file://{os.path.abspath(report_path)}")
        
        return result.returncode
    else:
        print("❌ Report generation failed!")
        return 1

if __name__ == "__main__":
    exit_code = run_tests_and_generate_report()
    exit(exit_code)